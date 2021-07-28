import numpy as np
import pandas as pd
import sklearn as sk
import sqlite3 as sql
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


data=pd.read_csv('data/data.csv', index_col=False)
data['title'] = data['original_title']
tfidf = TfidfVectorizer(stop_words='english')
data['overview'] = data['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(data['overview'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data.index, index=data['title']).drop_duplicates()
#ROOT =path.dirname(path.relpath((__file__)))

def get_result (title):
    df=data.loc[data['title'] == title]
    df = df['original_title']
    return df

def get_recommendations(title, cosine_sim=cosine_sim):
    df=data.loc[data['title'] == title]
    df = df['original_title']
    return df
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    rec = data['title'].iloc[movie_indices]
    return rec.dropna()
