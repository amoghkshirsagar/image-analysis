from src.utils.promptHandle import promptHandle
import ollama

class Agent():
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def get_name(self):
        return self.name
    
    def get_model(self):
        return self.model
    
    def sendCommandAndGetResponse(self, command, image):
        prompt = f"""Given image, analyze and answer the following question:
    {command}

    Answer only question in short, clear and concise.
    Do not include any additional information.
    """
        response = promptHandle(prompt, self.model, image)
        return response