import streamlit as st
from recommendation_system import recommend

st.set_page_config(page_title="Course Recommender System", layout="centered")

st.title("🎓 Educational Course Recommendation System")
st.write("Enter your interests to find matching courses across various fields!")

# 1. Input field for interests
user_interest = st.text_input(
    "What are you interested in?",
    placeholder="e.g., nursing, python, cooking, music, accounting..."
)

# 2. Input field for number of recommendations
num_recommendations = st.number_input(
    "How many recommendations do you want?",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

# 3. Get recommendations button
if st.button("Get Recommendations"):
    if user_interest.strip():
        results = recommend(user_interest, int(num_recommendations))
        
        if not results.empty:
            st.subheader(f"Top Recommendations for: '{user_interest}'")
            st.dataframe(results)  # Displays the matching courses table
        else:
            st.warning("No matching courses found. Try entering different keywords!")
    else:
        st.error("Please enter your interest first.")