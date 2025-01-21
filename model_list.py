import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

config_list_openai_4o_mini = [
    {
        "model": "gpt-4o-mini",
        "api_key": OPENAI_API_KEY,
    }
]


config_list_deepseek_chat = [
    {
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
        "api_key": DEEPSEEK_API_KEY,
        "api_type": "deepseek",
        "tags": ["deepseek"],
    }
]

config_list_deepseek_reasoner = [
    {
        "model": "deepseek-reasoner",
        "base_url": "https://api.deepseek.com/v1",
        "api_key": DEEPSEEK_API_KEY,
        "api_type": "deepseek",
        "tags": ["deepseek"],
    }
]
