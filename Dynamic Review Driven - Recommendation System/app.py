from flask import Flask, render_template, request
import pandas as pd
import os

from utils.recommendation import get_top_movies
from utils.sentiment import predict_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', movies=None, genre=None)

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    movies = get_top_movies(genre)

    return render_template('index.html', movies=movies, genre=genre)

@app.route('/submit_review', methods=['POST'])
def submit_review():

    movie_name = request.form['movie_name']
    imdb_id = request.form['imdb_id']
    review = request.form['review']
    genre = request.form['genre']

    sentiment = predict_sentiment(review)

    new_review = pd.DataFrame([{
        'imdb_id': imdb_id,       
        'movie_name': movie_name,
        'review': review,
        'sentiment': sentiment
    }])

    file_path = 'C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/user_data/reviews.csv'

    new_review.to_csv(
        file_path,
        mode='a',
        header=not os.path.exists(file_path),  
        index=False
    )
    
    movies = get_top_movies(genre)

    return render_template('index.html', movies=movies, genre=genre)


if __name__ == '__main__':
    app.run(debug=True)
