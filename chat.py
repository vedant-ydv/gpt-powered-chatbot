"""Core chat functionality for the AI chatbot."""
from typing import List, Dict
from openai import OpenAI
from .config import OPENAI_API_KEY, DEFAULT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

class ChatBot:
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model
        self.history: List[Dict] = []
    
    def chat(self, message: str) -> str:
        """Send a message to the chatbot and get a response."""
        self.history.append({"role": "user", "content": message})
        
        response = client.chat.completions.create(
            model=self.model,
            messages=self.history,
            temperature=0.7,
        )
        
        assistant_message = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def clear_history(self):
        """Clear the conversation history."""
        self.history = [] 