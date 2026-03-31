import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
stop_words.discard('not')
stop_words.discard('no')
stop_words.discard('never')

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.replace('<br />', ' ')
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.lower() not in stop_words]
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    return " ".join(tokens)
