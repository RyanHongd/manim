from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = api_key
)

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant that only returns Python code."},
        {"role": "user", "content": """現在有題目是:小名有30塊錢，曉華拿走他8塊錢，剩下的錢要分給4個人，每個人可以拿到幾塊錢?
        """},
    ]

)





