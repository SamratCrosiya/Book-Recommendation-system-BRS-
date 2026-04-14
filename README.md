--

# 📚 BookLens – Book Recommendation System

#### #  In Short #

BookLens is a Flask-based web application that recommends books using #item-based collaborative filtering# and #cosine similarity#.

Users can:

* View #Top 50 Popular Books#
* Get #similar book recommendations# based on user ratings

The system uses #preprocessed pickle files#, ensuring fast performance without reprocessing large datasets.

---

####  BAse FOundation

* Recommendation technique: #Collaborative Filtering#
* Similarity metric: #Cosine Similarity#
* Data processing: Done offline in Jupyter Notebook
* Runtime: Uses `.pkl` files for fast inference 

---

# Tech Stack#

* Backend: Flask
* Data: pandas, NumPy
* Deployment: gunicorn
* Frontend: HTML (Jinja templating)

---

#### # Project Structure#

```
Book Recommendation/
│
├── frontend/
│   ├── app.py
│   ├── index.html
│   ├── recommend.html
│   ├── popular.pkl
│   ├── pt.pkl
│   ├── books.pkl
│   ├── similarity_scores.pkl
│
├── Books.csv
├── Ratings.csv
├── Users.csv
├── book-recommender-system.ipynb
├── requirements.txt
└── Procfile
```

---

#### # Run Locally#

```bash
py frontend\app.py
```

Open:

```
http://127.0.0.1:5000/
```

---

#### 🔁 System Architecture Flow

```mermaid
graph TB
    subgraph "Client Layer"
        A[🌐 Browser]
    end

    subgraph "Flask Server"
        B[🚀 Flask App]
        C[🔄 Routes]
        D[📄 Template Engine]
    end

    subgraph "Recommendation Engine"
        E[📊 Pivot Table]
        F[📈 Similarity Matrix]
        G[🧠 Recommendation Logic]
    end

    subgraph "Data Layer"
        H[💾 Pickle Files]
    end

    A --> B
    B --> C
    C --> D
    C --> G
    G --> E
    G --> F
    E --> H
    F --> H
    D --> A

    style B fill:#339933,color:#fff
    style D fill:#667eea,color:#fff
    style H fill:#f59e0b,color:#fff
```

---

### # Application Flow (ASCII)#

```
┌───────────────────────────────────────────────┐
│               APPLICATION FLOW                │
├───────────────────────────────────────────────┤
│                                               │
│  Client → Flask → Routes → Logic → Data       │
│     ↑                              ↓          │
│  HTML Render  ← Template Engine ← Result      │
│                                               │
└───────────────────────────────────────────────┘
```

---

###                #                   🌐 Request Lifecycle #

```mermaid
graph LR
    A[👤 User] --> B[GET /]
    B --> C[Flask Route]
    C --> D[Load popular.pkl]
    D --> E[Render HTML]
    E --> F[Browser UI]

    F --> G{User Action}

    G -->|Search Book| H[POST /recommend_books]
    H --> I[Check pt.pkl]
    I --> J[Find Similarity]
    J --> K[Fetch Book Details]
    K --> L[Render Result]
    L --> F

    style C fill:#339933,color:#fff
    style E fill:#667eea,color:#fff
    style L fill:#10B981,color:#fff
```

---

### # CRUD-like Flow (Mindmap)#

```mermaid
mindmap
  root((📚 BookLens))
    READ
      Show Popular Books
      Render HTML
    SEARCH
      Input Book
      Validate Title
    RECOMMEND
      Find Similar Books
      Sort by Similarity
      Return Top Results
    DATA
      Pivot Table
      Similarity Matrix
      Pickle Storage
    API
      Flask Routes
      POST Handling
      Error Handling
```

---

### # Recommendation Logic#

```
User Input
    ↓
Find Index in pt.pkl
    ↓
Read similarity_scores
    ↓
Sort by similarity
    ↓
Skip same book
    ↓
Return Top 4 books
```

---

### # Data Pipeline#

```mermaid
graph TD
    A[Books.csv] --> D[Data Processing]
    B[Ratings.csv] --> D
    C[Users.csv] --> D

    D --> E[Pivot Table]
    D --> F[Popular Books]
    D --> G[Similarity Matrix]

    E --> H[pt.pkl]
    F --> I[popular.pkl]
    G --> J[similarity_scores.pkl]

    H --> K[Flask App]
    I --> K
    J --> K
```

---

### # Limitations#

* Only works for books in dataset
* No real-time learning
* No content-based filtering
* Static recommendations

---

### # Key Takeaways#

* Fast runtime using #pickle files#
* Scalable architecture (separate training + serving)
* Clean separation:

  * Data Processing (Notebook)
  * Backend (Flask)
  * Frontend (HTML)

---

### # Summary#

BookLens transforms raw rating data into a #real-time recommendation system# by:

* Precomputing similarity
* Serving via Flask
* Rendering dynamic HTML

---



---


