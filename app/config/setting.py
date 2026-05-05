from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    groq_api_key=os.getenv("GROQ_API_KEY")
    tavily_api_key=os.getenv("TAVILY_API_KEY")

    multi_model=[
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "openai/gpt-oss-120b"
    ]

setting=Settings()