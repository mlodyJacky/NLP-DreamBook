import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
import pickle

with open('dreams/dreams_with_emotions.json', 'r', encoding='utf-8') as f:
    dreams_data = json.load(f)

data = pd.DataFrame(dreams_data)

labels = ['happiness', 'anger', 'sadness', 'fear']

X = data['dream_content']
y = data[labels]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)

X_train_tfidf = vectorizer.fit_transform(X_train)

emotion_models = {}

for label in labels:
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_tfidf, y_train[label])
    emotion_models[label] = model

with open('emotion_models_regressor.pkl', 'wb') as f:
    pickle.dump(emotion_models, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)



X_test_tfidf = vectorizer.transform(X_test)
y_pred = {}

for label in labels:
    y_pred[label] = emotion_models[label].predict(X_test_tfidf)

for label in labels:
    rmse = root_mean_squared_error(y_test[label], y_pred[label])
    print(f"Emotion: {label}")
    print(f"Root Mean Squared Error: {rmse}")

def predict_emotion(dream_text):
    dream_tfidf = vectorizer.transform([dream_text])
    prediction = {}
    for label in labels:
        prediction[label] = emotion_models[label].predict(dream_tfidf)[0]
    return prediction

# new_dream = "My dream was about flying and being free. I felt so happy and joyful. I was also scared and angry"
# predicted_emotions = predict_emotion(new_dream)
# print("Predykcja emocji:", predicted_emotions)
