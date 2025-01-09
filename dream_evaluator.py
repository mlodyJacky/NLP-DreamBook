from transformers import pipeline
import json

def chunk_text(text, max_length=512):
    words = text.split()
    chunks = []
    chunk = []
    for word in words:
        chunk.append(word)
        if len(" ".join(chunk)) > max_length:
            chunks.append(" ".join(chunk[:-1]))
            chunk = [chunk[-1]]
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks

if __name__ == "__main__":
    with open("dreams/dreamsall.json", "r", encoding="utf-8") as f:
        dreams = json.load(f)

    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

    for dream in dreams:
        text = dream["dream_content"]
        chunks = chunk_text(text)

        emotions = {'joy': 0, 'anger': 0, 'sadness': 0, 'fear': 0}
        
        for chunk in chunks:
            result = classifier(chunk)
            chunk_emotions = {emotion['label']: emotion['score'] for emotion in result[0]}
            for emotion, score in chunk_emotions.items():
                if emotion in emotions:
                    emotions[emotion] += score

        total_score = sum(emotions.values())
        if total_score > 0:
            dream['happiness'] = int((emotions.get('joy', 0) / total_score) * 100)
            dream['anger'] = int((emotions.get('anger', 0) / total_score) * 100)
            dream['sadness'] = int((emotions.get('sadness', 0) / total_score) * 100)
            dream['fear'] = int((emotions.get('fear', 0) / total_score) * 100)
        else:
            dream['happiness'] = 0
            dream['anger'] = 0
            dream['sadness'] = 0
            dream['fear'] = 0
    with open("dreams/dreams_with_emotions.json", "w", encoding="utf-8") as f:
        json.dump(dreams, f, ensure_ascii=False, indent=4)

    print("Done")
