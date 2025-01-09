import pickle



def predict_emotion(dream_text):
    with open('emotion_models_regressor.pkl', 'rb') as f:
        emotion_models = pickle.load(f)

    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    dream_tfidf = vectorizer.transform([dream_text])

    prediction = {}
    for label in ['happiness', 'anger', 'sadness', 'fear']:
        prediction[label] = emotion_models[label].predict(dream_tfidf)[0]
    
    return prediction



dream = """ It's dark at night and I'm driving my car in the rain. I stop and all the sudden I'm at 
the front door of someone's house (I've never seen this doorway before). This girl I work with at Beach City 
named Mary answers the door. She starts talking and says something like, Im so glad you're finally asking me out.
Talking to you at work was getting so awkward. For some reason I can't tell her that I don't like her at all,
and next we're both in my car driving to the mall. Now we're walking around a whole bunch of different food courts
and I keep thinking, This girl really likes me. I could easily get a piece, then never talk to her again. But I know 
this would be wrong. While Im debating this, I wake up. """
predicted_emotions = predict_emotion(dream)
print("Predykcja emocji:", predicted_emotions)
