import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["API_KEY"],
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