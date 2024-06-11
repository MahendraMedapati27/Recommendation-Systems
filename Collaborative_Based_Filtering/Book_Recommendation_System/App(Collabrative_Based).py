import pickle
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load precomputed data
similarity_matrix = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Book_Recommendation\similarity_matrix.pkl', 'rb'))
pt = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Book_Recommendation\pivot_table.pkl', 'rb'))
books_df = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Book_Recommendation\books_df.pkl', 'rb'))

# Set the title of the Streamlit app
st.title("Collaborative Filtering Based Book Recommendation System")

def recommend(book_name):
    # Strip any leading/trailing whitespace from the book name
    book_name = book_name.strip()
    
    # Check if the book is in the pivot table index
    if book_name not in pt.index:
        st.write(f"The book '{book_name}' is not in the dataset.")
        return None
    
    # Get the index of the specified book in the pivot table
    index = np.where(pt.index == book_name)[0][0]
    
    # Get the similarity scores for the book
    similarity_scores_for_book = similarity_matrix[index]
    
    # Enumerate over the similarity scores and sort them in descending order
    similar_items = sorted(list(enumerate(similarity_scores_for_book)), key=lambda x: x[1], reverse=True)[1:11]
    
    # Get the indices of recommended books
    recommended_books = []
    for j in similar_items:
        similar_book_index = j[0]
        recommended_books.append(pt.index[similar_book_index])  # Append recommended book to list
    
    return recommended_books

# Display a dropdown to select a book
selected_book_name = st.selectbox('Select the book from the below list', books_df['Book-Title'])

# When the "Recommend" button is clicked
if st.button('Recommend'):
    recommended_books = recommend(selected_book_name)
    
    # Initialize a list to store URLs of recommended books
    recommended_books_urls = []
    for book in recommended_books:
        book_row = books_df[books_df['Book-Title'] == book]
        url = book_row.iloc[0]['Image-URL-M']
        recommended_books_urls.append(url)
    
    # Create two rows of columns to display the recommended books
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            book_title = recommended_books[i]
            image_url = recommended_books_urls[i]
            st.image(image_url, caption=book_title, use_column_width=True, output_format='PNG')
    
    cols = st.columns(5)
    for i in range(5, 10):
        with cols[i - 5]:
            book_title = recommended_books[i]
            image_url = recommended_books_urls[i]
            st.image(image_url, caption=book_title, use_column_width=True, output_format='PNG')
