import pandas as pd
import pickle
import nltk
import re

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')
nltk.download('wordnet')

print("Loading dataset...")
df = pd.read_csv('C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/data/IMDB Review Dataset.csv')

print("Cleaning data...")

df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

df['review'] = df['review'].str.replace('<br />', ' ', regex=False)
df['review'] = df['review'].apply(lambda x: re.sub(r'[^a-zA-Z]', ' ', x.lower()))

stop_words = set(stopwords.words('english'))
stop_words -= {'not', 'no', 'never'}

lemmatizer = WordNetLemmatizer()

def preprocess(text):
    words = text.split()
    words = [w for w in words if w not in stop_words]
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)

df['review'] = df['review'].apply(preprocess)

print("Vectorizing...")

tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['review'])
y = df['sentiment']

print("Splitting data...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = MultinomialNB()
model.fit(X_train, y_train)

print("Saving model...")

pickle.dump(model, open('C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/models/sentiment_model.pkl', 'wb'))
pickle.dump(tfidf, open('C:/Users/Admin/Desktop/Dynamic Review Driven - Recommendation System/models/vectorizer.pkl', 'wb'))

