import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["API_KEY"], # задавать в .env
    base_url="https://foundation-models.api.cloud.ru/v1"
)

response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4",
    messages=[
        {
            "role": "user",
            "content": "Объясни, что такое промпт-инженерия простыми словами."
        }
    ],
    temperature=0.3,
    max_tokens=1000
)

print(response.choices[0].message.content)