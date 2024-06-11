import pickle
import streamlit as st
import pandas as pd

# Load the DataFrame
popular_df = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Book_Recommendation\popular_df.pkl', 'rb'))

# Streamlit app setup
st.title("Popular Books Recommendation System")

# CSS to control the layout of the book display
st.markdown("""
    <style>
    .book {
        width: 100%;
        margin: 10px auto;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .book img {
        width: 100px;
        height: 150px;
        object-fit: cover;
        margin-bottom: 10px;
    }
    .book-title {
        font-weight: bold;
        font-size: 14px;
        margin: 10px 0 5px;
    }
    .book-author {
        font-size: 14px;
        color: #555;
        margin-bottom: 5px;
    }
    .book-ratings {
        font-size: 14px;
        color: #0073e6; /* Blue color for ratings */
    }
    .book-num-ratings {
        font-size: 14px;
        color: #ff4500; /* Orange color for number of ratings */
    }
    </style>
    """, unsafe_allow_html=True)

# Function to display a book's information
def display_book(col, row):
    col.markdown(f"""
    <div class="book">
        <img src="{row['Image-URL-M']}" alt="Book cover">
        <div class="book-title">{row['Book-Title']}</div>
        <div class="book-author">by {row['Book-Author']}</div>
        <div class="book-ratings">Avg Rating: {row['avg_ratings']}</div>
        <div class="book-num-ratings">Ratings: {row['num_ratings']}</div>
    </div>
    """, unsafe_allow_html=True)

# Display books in a scrollable format, 5 per row
num_books_per_row = 5

# Iterate through the DataFrame and display books
for i in range(0, len(popular_df), num_books_per_row):
    cols = st.columns(num_books_per_row)
    for col, idx in zip(cols, range(i, min(i + num_books_per_row, len(popular_df)))):
        row = popular_df.iloc[idx]
        display_book(col, row)
