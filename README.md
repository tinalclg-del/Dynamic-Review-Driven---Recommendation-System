This project is a dynamic Movie Recommendation System that suggests movies based on user-selected genres and 
enhances recommendations using Sentiment Analysis of user reviews.

The system first provides top movie recommendations according to the chosen genre. 
Users can then submit reviews for any movie, and the system analyzes the sentiment (positive/negative) to refine future recommendations.

It also includes interactive features like voice toggle, review submission, and a user-friendly interface built using web technologies.

FOLDER STRUCTURE:

movie-recommendation-system/

├── app.py                     # Main Flask backend (server)

├── requirements.txt          # Python dependencies



│
├── data/                     # All CSV datasets
│   ├── IMDB Bollywood Movie Dataset.csv
│   ├── IMDB Ratings.csv
|   ├── IMDB Review Dataset.csv
│   └── Award dataset.csv
│
├── models/                   # Saved ML models
│   ├── vectorizer.pkl
│   └── sentiment_model.pkl
│
├── utils/                    # Helper functions
│   ├── preprocess.py         # Text cleaning, tokenization
│   ├── recommendation.py     # Recommendation logic + formula
│   └── sentiment.py          # Sentiment prediction function
│   
│
├── templates/                # HTML files (Flask uses this)  
│   └── index.html            
│
├── user_data/                # Dynamic data storage
│   └── reviews.csv           # Updated when user submits review
│
└── notebooks/                
    └── train_model.py
    

NOTE:
The csv file named " IMDB Review Dataset.csv " is on the drive as it exceeds the limit of size to upload on GitHub. Which actually should be in the data folder.
