from transformers import pipeline


generator = pipeline("text-generation", model="gpt-3.5-turbo")

#Jak to mozna zrobic np. mozna tak zrobic z podsumowaniem lub interpretacja, ale poki co sprobuje rekomendacje zrobic recznie
def generate_recommendation_with_gpt(user_message):
    prompt = f"Analizuj ten sen: {user_message}. Podaj medyczne porady na temat poprawy jakości snu lub napisz że wszystko jest w porządku jeśli sen nie ma problemów."
    response = generator(prompt, max_length=500, num_return_sequences=1)
    return response[0]['generated_text']