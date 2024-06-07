# Recommendation Systems

## Introduction
Recommendation systems are algorithms designed to provide suggestions to users based on their preferences or past interactions. These systems are widely used in various domains such as e-commerce, social media, streaming platforms, and more to enhance user experience, increase engagement, and drive revenue. By analyzing user behavior and item features, recommendation systems help in predicting the likelihood of a user's interest in a particular item. These kinds of systems improve user experiences, boost user involvement, and proper corporate expansion.

## Applications
- E-commerce platforms: E-commerce platforms like Amazon, Flipkart Recommend products based on user purchase history and browsing behavior.
- Streaming services: Netflix, Youtube, Disney Hotstar suggest movies or TV shows based on user preferences and viewing history.
- Social media platforms: Facebook, Instagram Recommend friends, groups, or content based on user interests and connections.
- Music streaming platforms: Provide personalized playlists or song recommendations based on user listening history and preferences for spotify, wynk, e.t.c
- News websites: Recommend articles or news stories based on user interests and reading behavior.

## Types of Recommendation Systems
There are several types of recommendation systems, including:
1. Collaborative Filtering
2. Content-Based Filtering
3. Hybrid Recommendation Systems

## Collaborative Filtering
Collaborative filtering recommends items by leveraging the preferences and behaviors of similar users. There are two main approaches to collaborative filtering:
- User-based collaborative filtering
- Item-based collaborative filtering

![Collaborative Filtering](images/collaborative_filtering.png)

## Content-Based Filtering
Content-based filtering recommends items based on their features or attributes. It analyzes the properties of items that a user has interacted with in the past and recommends similar items.It is supervised machine learning used to induce a classifier to discriminate between interesting and uninteresting items for the user.In a content-based recommendation system, first, we need to create a profile for each item, which represents the properties of those items. The user profiles are inferred for a particular user. We use these user profiles to recommend the items to the users from the catalog.
![3-Figure1-1](https://github.com/MahendraMedapati27/Recommendation-Systems/assets/153280887/2ba3636f-a1f0-40f7-a848-0a9c19c89bd4)

# Item Profile

In a content-based recommendation system, building a profile for each item is crucial. This profile contains the significant properties of each item. For example, in the case of movies, important properties include actors, directors, release year, and genre. Similarly, for documents, the important property could be the type of content and a set of keywords within it.

## Creating an Item Profile

To create an item profile, we first perform TF-IDF vectorization. **TF (term frequency)** represents how often a term appears in a document, while **IDF (inverse document frequency)** measures the significance of that term across the entire corpus.

### TF-IDF Vectorizer

**Term Frequency (TF):**
Term frequency, or TF, is a fundamental concept in information retrieval and natural language processing. It quantifies the frequency with which a term appears in a text corpus or document. TF helps rank terms in a document based on their importance. For a variety of text analysis tasks, such as information retrieval, document classification, and sentiment analysis, the yielded TF value can be used to identify important terms in a document. It offers a framework for figuring out how relevant a word is in a particular situation.

**Inverse-Document Frequency (IDF):**
The measure known as Inverse Document Frequency (IDF) is employed in text analysis and information retrieval to evaluate the significance of phrases within a set of documents. IDF measures how uncommon or unique a term is in the corpus. To compute it, take the reciprocal of the fraction of documents that include the term and logarithmize it. Common terms have lower IDF values, while rare terms have higher values. IDF is an essential part of the TF-IDF (Term Frequency-Inverse Document Frequency) method, which uses it to assess the relative importance of terms in different documents. To improve information representation and retrieval from massive text datasets, IDF is used in tasks including document ranking, categorization, and text mining.

**TF-IDF Score:**
The TF-IDF score combines TF and IDF to determine the importance of a term within a document relative to the entire corpus. It is computed by multiplying TF and IDF together.

## User Profile

The user profile is a vector that describes the user's preferences. It is created based on a utility matrix that captures the relationship between users and items. Aggregating the profiles of items liked by the user helps in determining their preferences.

## Advantages and Disadvantages

**Advantages:**
- No need for data on other users when applying to similar users.
- Able to recommend to users with unique tastes.
- Can recommend new and popular items.
- Provides explanations for recommended items.

**Disadvantages:**
- Finding the appropriate features can be challenging.
- Does not recommend items outside the user's profile.


## Hybrid Recommendation Systems
Hybrid recommendation systems combine multiple recommendation techniques to provide more accurate and diverse recommendations. They leverage the strengths of both collaborative filtering and content-based filtering approaches.
![Hybrid Recommendation Systems](images/hybrid_recommendation_systems.png)
