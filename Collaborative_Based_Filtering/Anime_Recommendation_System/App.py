import requests
import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the dataframes and similarity matrix from pickle files
anime_df = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Anime_Recommendation\anime_df.pkl', 'rb'))
pt = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Anime_Recommendation\pt.pkl', 'rb'))
similarity_matrix = pickle.load(open(r'C:\Users\Hp\OneDrive\Desktop\MRS\Anime_Recommendation\similarity_matrix.pkl', 'rb'))

# Function to get the anime poster using the Jikan API
def get_anime_poster(anime_id):
    # Jikan API endpoint to fetch anime pictures
    api_url = f"https://api.jikan.moe/v4/anime/{anime_id}/pictures"
    
    # Sending GET request to the API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            # Return the first image URL
            return data['data'][0]['jpg']['image_url']
    return None

# Function to recommend anime based on collaborative filtering
def recommend(anime_name):
    # Strip any leading/trailing whitespace from the anime name
    anime_name = anime_name.strip()
    
    # Check if the anime is in the pivot table index
    if anime_name not in pt.index:
        print(f"The anime '{anime_name}' is not in the dataset.")
        return
    
    # Get the index of the specified anime in the pivot table
    index = np.where(pt.index == anime_name)[0][0]
    
    # Get the similarity scores for the anime
    similarity_scores_for_anime = similarity_matrix[index]
    
    # Enumerate over the similarity scores and sort them in descending order
    similar_items = sorted(list(enumerate(similarity_scores_for_anime)), key=lambda x: x[1], reverse=True)[1:11]
    
    # Get the indices of recommended anime
    recommended_anime = []
    for j in similar_items:
        similar_anime_index = j[0]
        recommended_anime.append(pt.index[similar_anime_index])  # Append recommended anime to list
    
    return recommended_anime

# Streamlit app title
st.title("Collaborative Filtering Based Anime Recommendation System")

# Dropdown to select an anime from the list
selected_anime_name = st.selectbox('Select the name of anime from the below list', anime_df['name'])

# When the 'Recommend' button is clicked
if st.button('Recommend'):
    # Get the list of recommended anime
    recommended_anime = recommend(selected_anime_name)
    
    recommended_anime_ids = []
    for anime in recommended_anime:
        # Get the anime ID from the dataframe
        anime_row = anime_df[anime_df['name'] == anime]
        ids = anime_row.iloc[0]['anime_id']
        recommended_anime_ids.append(ids)
        
    # Display the recommended anime posters and titles in two rows of 5 columns each
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            anime_title = recommended_anime[i]
            image_url = get_anime_poster(recommended_anime_ids[i])
            st.image(image_url, caption=anime_title, width=100, output_format='PNG')
    
    cols = st.columns(5)
    for i in range(5, 10):
        with cols[i - 5]:
            anime_title = recommended_anime[i]
            image_url = get_anime_poster(recommended_anime_ids[i])
            st.image(image_url, caption=anime_title, width=100, output_format='PNG')
