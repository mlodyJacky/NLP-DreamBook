import pickle
import os

import pickle
import os

def predict_emotion(dream_text):
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
    resources_dir = os.path.join(parent_dir, "resources")

    model_path = os.path.join(resources_dir, "emotion_models_regressor.pkl")
    vectorizer_path = os.path.join(resources_dir, "vectorizer.pkl")

    with open(model_path, 'rb') as f:
        emotion_models = pickle.load(f)

    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)

    dream_tfidf = vectorizer.transform([dream_text])
    prediction = {}
    for label in ['happiness', 'anger', 'sadness', 'fear']:
        prediction[label] = emotion_models[label].predict(dream_tfidf)[0]
    
    return prediction


# dream = """
#         I was being pursued by someone in a vehicle trying to run me down. Being in an orchard,
#         I was able to duck behind whatever tree was nearby. Then I found myself far from any tree trunk, 
#         but I managed to leap up, grab a branch, and pull myself to safety. However, the driver skidded the vehicle
#         to a stop and aimed a pistol at me. The click I heard which wakened me came from an alarm clock.
#         My heart was racing when I awoke.
#     """

# predicted_emotions = predict_emotion(dream)

# print("Predykcja emocji:", predicted_emotions)
