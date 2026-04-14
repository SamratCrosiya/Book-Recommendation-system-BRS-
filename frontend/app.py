import os
import pickle
from pathlib import Path

import numpy as np
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent


def load_pickle(filename):
    with (BASE_DIR / filename).open('rb') as file:
        return pickle.load(file)


def format_rating(value):
    return f'{np.floor(float(value) * 100) / 100:.2f}'


popular_df = load_pickle('popular.pkl')
pt = load_pickle('pt.pkl')
books = load_pickle('books.pkl')
similarity_scores = load_pickle('similarity_scores.pkl')

app = Flask(__name__, template_folder=str(BASE_DIR))


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name = list(popular_df['Book-Title'].values),
        author    = list(popular_df['Book-Author'].values),
        image     = list(popular_df['Image-URL-M'].values),
        votes     = list(popular_df['num_ratings'].values),
        rating    = [format_rating(value) for value in popular_df['avg_rating'].values],
    )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input', '').strip()
    book_title = user_input

    if user_input and user_input not in pt.index:
        matches = [title for title in pt.index if title.lower() == user_input.lower()]
        if matches:
            book_title = matches[0]

    if not book_title or book_title not in pt.index:
        return render_template('recommend.html', data=[], error="Book not found. Please try another title.")

    index = np.where(pt.index == book_title)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        temp_df = temp_df.drop_duplicates('Book-Title')
        item = [
            temp_df['Book-Title'].values[0],
            temp_df['Book-Author'].values[0],
            temp_df['Image-URL-M'].values[0],
        ]
        data.append(item)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
