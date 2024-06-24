from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Paths to model and data files
USER_FINAL_RATING_PATH = 'models/user_final_rating.pkl'
DF_CLEANED_DATA_PATH = 'models/df_cleaned_data.pkl'
LOGREG_TUNED_MODEL_PATH = 'models/logreg_tuned_model.pkl'
TFIDF_VECTORIZER_PATH = 'models/tfidf_model.pkl'

# Load the models and data files
with open(USER_FINAL_RATING_PATH, 'rb') as f:
    user_final_rating = pickle.load(f)

with open(DF_CLEANED_DATA_PATH, 'rb') as f:
    df_cleaned_data = pickle.load(f)

with open(LOGREG_TUNED_MODEL_PATH, 'rb') as f:
    logreg_tuned_model = pickle.load(f)

with open(TFIDF_VECTORIZER_PATH, 'rb') as f:
    tfidf = pickle.load(f)

def get_sentiment_recommendations(user):
    if user in user_final_rating.index:
        # Get top 20 rated item IDs for the user
        top_rated_ids = list(user_final_rating.loc[user].sort_values(ascending=False)[0:20].index)
        # Filter data based on the top 20 rated item IDS
        top_items_data = df_cleaned_data[df_cleaned_data.id.isin(top_rated_ids)]
        
        # Next, Predict the sentiment for these items
        
        # Transform reviews of these items using TF-IDF
        reviews_tfidf = tfidf.transform(top_items_data["cleaned_review"].values.astype(str))
        # Predict sentiment for the reviews using the tuned logistic regression model
        top_items_data["predicted_sentiment"] = logreg_tuned_model.predict(reviews_tfidf)
        
        # Group by item name to count positive reviews
        grouped_data = top_items_data.groupby('name', as_index=False).count()
        # Calculate positive review count, total review count, and percentage of positive reviews
        grouped_data["pos_review_count"] = grouped_data.name.apply(
            lambda x: top_items_data[(top_items_data.name == x) & (top_items_data.predicted_sentiment == 1)]["predicted_sentiment"].count()
        )
        grouped_data["total_review_count"] = grouped_data['predicted_sentiment']
        grouped_data['pos_sentiment_percent'] = np.round(grouped_data["pos_review_count"] / grouped_data["total_review_count"] * 100, 2)
    
        # Get top 5 recommendations based on positive sentiment percentage
        top_5_recommendations = grouped_data.sort_values('pos_sentiment_percent', ascending=False).head(5)['name'].tolist()
        return top_5_recommendations
    else:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/recommend', methods=['GET'])
def recommend():
    username = request.args.get('username')
    if username:
        recommendations = get_sentiment_recommendations(username)
        if recommendations:
            return jsonify({
                "username": username,
                "products": recommendations
            })
        else:
            return jsonify({
                "username": username,
                "products": [],
                "error": "User not found or no recommendations available."
            })
    else:
        return jsonify({
            "error": "No username provided"
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
