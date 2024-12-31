import requests
# from ollama import generate

OLLAMA_URL = "http://ollama:11434"  # Ollama container endpoint

def call_ollama(prompt, model="llama3.2:1b"):
    """
    Calls the Ollama LLM with a given prompt and returns the response.
    """
    # print("<><>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<>>>>>>>><<<<<<<<<<>>>>>>>>>>><<<<<<<<<>>>>>>><<<<<<<>>>>><")
    response = requests.post(
        f"{OLLAMA_URL}/api/generate/",
        json={"model": model, "prompt": prompt, "stream":False},
        stream=False
    )
    response.raise_for_status()
    # print(response.json()["response"])
    # # print(type(response.json()["response"]))
    # print("<><>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<>>>>>>>><<<<<<<<<<>>>>>>>>>>><<<<<<<<<>>>>>>><<<<<<<>>>>><")

    return response.json()["response"]
