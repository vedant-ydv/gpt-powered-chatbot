"""Configuration management for the AI chatbot."""
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

DEFAULT_MODEL = "gpt-3.5-turbo"
MAX_HISTORY = 10 