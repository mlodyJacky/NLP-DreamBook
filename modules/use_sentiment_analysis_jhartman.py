from transformers import pipeline
import math

def predict_emotions(dream_description):
    classifier = pipeline("text-classification", 
                          model="j-hartmann/emotion-english-distilroberta-base", 
                          top_k=None)
    predictions = classifier(dream_description)
    emotion_scores = {emotion['label'].lower(): emotion['score'] * 100 for emotion in predictions[0]}
    mapped_emotions = {
        "happiness": math.ceil(emotion_scores.get("joy", 0)),
        "anger": math.ceil(emotion_scores.get("anger", 0)),
        "sadness": math.ceil(emotion_scores.get("sadness", 0)),
        "fear": math.ceil(emotion_scores.get("fear", 0)),
        
    }
    return mapped_emotions

# if __name__ == '__main__':
#     dream_description = """
#         I was being pursued by someone in a vehicle trying to run me down. Being in an orchard,
#         I was able to duck behind whatever tree was nearby. Then I found myself far from any tree trunk, 
#         but I managed to leap up, grab a branch, and pull myself to safety. However, the driver skidded the vehicle
#         to a stop and aimed a pistol at me. The click I heard which wakened me came from an alarm clock.
#         My heart was racing when I awoke.
#     """

#     emotions = predict_emotions(dream_description)
#     print("Predicted Emotions:", emotions)
