# Movie-Recommendation-System

# 🎬 Movie Recommendation System
## 📌 Project Overview

This project implements a Content-Based Movie Recommendation System using movie metadata from the TMDB dataset.
The system recommends movies similar to a given movie by analyzing textual features such as overview, genres, keywords, cast, and crew.

The recommendation logic is built using Natural Language Processing (NLP) techniques and cosine similarity.

# 🧠 Recommendation Technique Used

Content-Based Filtering

Core Idea:

Movies are represented as text vectors

Similarity between movies is calculated

Movies with the highest similarity scores are recommended

# 📊 Dataset

Source: TMDB Movies Dataset

Attributes Used:

Movie title

Overview

Genres

Keywords

Cast

Crew

These attributes are combined into a single feature called tags for similarity computation.

# ⚙️ Workflow

Load the TMDB dataset

Data cleaning and preprocessing

Feature extraction from text columns

Text vectorization using CountVectorizer

Similarity calculation using Cosine Similarity

Recommend top similar movies

# 🛠️ Technologies & Libraries

Language: Python

# Libraries Used:

Pandas

NumPy

Scikit-learn

NLTK

# 📂 Project Structure
recommendation-system/
│
├── Recommendation System.ipynb
├── tmdbdf.csv
├── README.md
└── requirements.txt
🔍 Feature Engineering

Combined multiple text columns into a single tags column

Removed stopwords

Applied stemming using PorterStemmer

Converted text data into vectors using CountVectorizer

# 🧮 Similarity Measure

Cosine Similarity is used to measure similarity between movie vectors

Higher cosine value → More similar movies

### ▶️ How to Run the Project
 

### 1️⃣ Install Required Libraries
pip install -r requirements.txt
### 2️⃣ Run the Notebook

Open Recommendation System.ipynb in Jupyter Notebook and run all cells sequentially.

### 🎯 Example Recommendation
Input Movie: Avatar

### Recommended Movies:
- John Carter
- Guardians of the Galaxy
- Star Trek
- Aliens
🚀 Key Features

### Content-based movie recommendations

- Efficient similarity computation

- Clean and modular code

- Easy to extend to other domains (books, products, courses)



# 👨‍💻 Author

Vamshi Kandela

GitHub: https://github.com/Vamshikandela

LinkedIn:https://www.linkedin.com/in/kandela-vamshi-2b4457258
