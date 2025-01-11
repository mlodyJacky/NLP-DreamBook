from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def generate_dream_title(dream_description):
    template = """
        You are a skilled writer. 
        You have read the following dream description.
        Based on it, produce a short, original "title" for the dream. 
        It should be no more than 3 words.

        Dream: {dream}

        Title:
    """

    model = OllamaLLM(model="llama3.2-vision")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    
    result = chain.invoke({
        "dream": dream_description,
    })

    return result

# dream_description = """
#     I was running from someone in an empty parking lot. It was seriously terrifying. It was dark, he was wearing a mask, and I could hear his footsteps behind me. I was running as fast as I could, but I couldn't seem to get away. I woke up in a cold sweat.
# """

# print(generate_dream_title(dream_description))