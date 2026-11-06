import os
from dotenv import load_dotenv
load_dotenv()
if not os.environ.get("OPENROUTER_API_KEY"):
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set. Copy .env.example to .env in this folder and add your key."
    )
print("Environment configuration loaded successfully.")