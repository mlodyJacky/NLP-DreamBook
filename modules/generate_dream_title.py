from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def generate_dream_title(dream_description):
    template = """
        You are a creative writer. 
        Your job is to create a short, interesting title for the dream below. 
        It should be no more than 3 words.

        Dream Description:
        {dream}

        Dream Title:
    """

    model = OllamaLLM(model="mistral")
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