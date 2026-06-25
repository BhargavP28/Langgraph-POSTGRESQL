from dotenv import load_dotenv
import os

# Load environment variables at import time so all modules get them
load_dotenv()

# LLM configuration (Groq)
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0
MAX_TOKENS = 2000
TIMEOUT = None
MAX_RETRIES = 2

# Database configuration
POSTGRES_URL = os.getenv("POSTGRES_URL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
