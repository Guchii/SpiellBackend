import pickle
from flask import jsonify, Response
from pandas import DataFrame

movies = pickle.load(open("model/movie_list.pkl", "rb"))
movies = DataFrame(movies)

similarity = pickle.load(open("model/similarity.pkl", "rb"))


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(
            {"title": movies.iloc[i[0]].title, "id": int(movies.iloc[i[0]].movie_id)}
        )

    return recommended_movies

