# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate

# def create_summary(interpretation, recommendation, predicted_emotion):
#     # Definiowanie szablonu promptu
#     template = """
#         You are an expert at summarizing dream analysis, here is the interpretation, recommendation, and feelings on a 
#         scale of 0 to 100. Summarize these three parameters in up to 500 characters in up to three sentences where each
#         sentence is about a separate parameter. Do not divide the answer into three sections, just write everything in one
#         paragraph. Maximum three sentences: the first sentence refers to the interpretation, the second to the recommendation, 
#         and the third to the user's feelings.

#         Interpretation: {interpretation}
#         Recommendation: {recommendation}
#         Predicted emotions: {predicted_emotion}

#         Summary:
#     """

#     # Inicjalizacja modelu
#     model = OllamaLLM(model="llama3.2-vision")

#     # Tworzenie promptu
#     prompt = ChatPromptTemplate.from_template(template)
#     chain = prompt | model

#     # Wywołanie modelu z odpowiednimi danymi
#     inputs = {
#         "interpretation": interpretation.strip(),
#         "recommendation": recommendation.strip(),
#         "predicted_emotion": predicted_emotion.strip()
#     }

#     # Zwracanie wyniku
#     result = chain.invoke(inputs)
#     return result

# # Przykładowe dane wejściowe
# interpretation = """
#     This dream suggests feelings of being overwhelmed or threatened in your waking life, possibly related to stress or anxiety. 
#     The orchard represents growth and vulnerability, while the vehicle's pursuit symbolizes internalized pressure to perform or 
#     achieve goals. Grabbing the branch signifies seizing control over your circumstances, but the pistol aimed at you indicates
#     lingering fear of failure or consequences. The alarm clock's click suggests a sudden awareness of time running out.
# """

# recommendation = """
#     Here is what you can do to improve your sleep:
#     Try to establish a regular sleep schedule, reduce caffeine and alcohol before bed, and ensure a comfortable sleeping environment,
#     e.g., a quiet and dark room.
#     Ensure the right room temperature, a comfortable mattress, and reduce stress during the day.
#     Try to reduce stress and tension during the day, and ensure proper sleep. Regular physical exercise can help improve sleep quality.
#     Ensure the right temperature in the bedroom, comfortable sleepwear, and avoid alcohol and caffeine before bed. If the problem persists, consult a doctor.
# """

# predicted_emotions = "{'happiness': 11.63, 'anger': 25.3, 'sadness': 19.31, 'fear': 48.64}"

# # Wywołanie funkcji i wyświetlenie wyniku
# print(create_summary(interpretation, recommendation, predicted_emotions))
