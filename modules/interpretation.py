from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def create_interpretation(dream_description):
    template = """
        You are an expert in dream interpretation. Based on symbolism, psychology, and medicine, interpret the dream and provide its hidden meaning. Your response should be short, maximum 500 characters long. Give only the interpretation.
        Dream: {dream}

        Interpretation:
    """
    
    model = OllamaLLM(model="mistral")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    result = chain.invoke({"dream": dream_description})
    return result

# dream_description = """
#     I was being pursued by someone in a vehicle trying to run me down. Being in an orchard,
#     I was able to duck behind whatever tree was nearby. Then I found myself far from any tree trunk, 
#     but I managed to leap up, grab a branch, and pull myself to safety. However, the driver skidded the vehicle
#     to a stop and aimed a pistol at me. The click I heard which wakened me came from an alarm clock.
#     My heart was racing when I awoke.
# """

# print(create_interpretation(dream_description))
