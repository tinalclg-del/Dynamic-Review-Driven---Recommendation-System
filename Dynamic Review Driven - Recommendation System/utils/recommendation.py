import pandas as pd

def load_data():
    movies = pd.read_csv('C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/data/IMDB Bollywood Movie Dataset.csv')
    ratings = pd.read_csv('C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/data/IMDB Ratings.csv')
    awards = pd.read_csv('C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/data/Award dataset.csv')

    df = movies.merge(ratings, on='imdb_id', how='left')

    df = df.merge(awards[['imdb_id']], on='imdb_id', how='left')
    df['award'] = df['imdb_id'].notna().astype(int)

    df['rating'] = df['rating'].fillna(0)
    return df

def load_reviews():
    try:
        return pd.read_csv('C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/user_data/reviews.csv')
    except:
        return pd.DataFrame(columns=['imdb_id','movie_name', 'review', 'sentiment'])

def calculate_score(row, user_sentiment=0):
    return (0.5 * row['rating']) + (0.3 * row['award'] * 10) + (0.2 * user_sentiment * 10)


def get_top_movies(genre):

    df = load_data()              
    reviews_df = load_reviews() 

    df = df[df['genre'].str.contains(genre, case=False, na=False)]

    results = []

    for _, row in df.iterrows():
        movie_id = row['imdb_id']
        movie_name = row['movie_name']         

        user_reviews = reviews_df[reviews_df['imdb_id'] == movie_id]['sentiment']
        
        sentiment_score = user_reviews.mean() if not user_reviews.empty else 0

        score = calculate_score(row, sentiment_score)

        results.append({
            'title': movie_name,
            'imdb_id': movie_id,
            'score': round(score, 2)
        })

    results = sorted(results, key=lambda x: x['score'], reverse=True)

    return results[:10]








