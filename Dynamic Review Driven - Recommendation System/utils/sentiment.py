import pickle
from utils.preprocess import preprocess_text

model = pickle.load(open('models/sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

def predict_sentiment(review):
    review = preprocess_text(review)
    vec = vectorizer.transform([review])
    return model.predict(vec)[0]
