from langchain.chat_models import init_chat_model
from . import config
ai_model = init_chat_model(
    "auto",
    model_provider="openrouter",
    max_tokens=3000
)
print("Model ready.")
