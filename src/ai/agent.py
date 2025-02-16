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
    
    def getResponse(self, prompt, image):
        response = promptHandle(prompt, self.model, image)
        return response