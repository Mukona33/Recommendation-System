import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(user_interest, num_recommendations=3):
    """
    Recommends courses based on user interest query.
    """
    courses = pd.read_csv("courses.csv")
    
    if not str(user_interest).strip():
        return pd.DataFrame()

    # Combine text columns to build features
    # (Adjust column names if your courses.csv uses different titles)
    text_columns = [col for col in ['course_name', 'category', 'skills', 'description'] if col in courses.columns]
    courses['combined_features'] = courses[text_columns].astype(str).agg(' '.join, axis=1)
    
    # Vectorize text using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    course_vectors = tfidf.fit_transform(courses['combined_features'])
    query_vector = tfidf.transform([user_interest])
    
    # Calculate similarity scores
    similarity_scores = cosine_similarity(query_vector, course_vectors).flatten()
    courses['match_score'] = similarity_scores
    
    # Sort and filter results
    recommended = courses.sort_values(by='match_score', ascending=False)
    recommended = recommended[recommended['match_score'] > 0]
    
    return recommended.head(num_recommendations)