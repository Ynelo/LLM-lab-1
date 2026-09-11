import os
import time
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url="https://foundation-models.api.cloud.ru/v1"
)

models = [
    "anthropic/claude-sonnet-4.6"
    "anthropic/claude-sonnet-4"
    "openai/gpt-5.4-nano"
    "openai/gpt-4.1-nano"
    "deepseek-ai/DeepSeek-V4-Flash"
    "deepseek-ai/DeepSeek-V3"
    "ai-sage/GigaChat3-10B-A1.8B"
    "google/gemini-3.1-flash-lite"
    "google/gemini-2.5-flash"
]

prompts = [
    "Расскажи рецепт домашних сырников"
]

results = []

for model in models:
    for i, prompt in enumerate(prompts, start=1):
        start_time = time.time()

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=1200
            )

            answer = response.choices[0].message.content
            status = "ok"
            error = ""

        except Exception as e:
            answer = ""
            status = "error"
            error = str(e)

        latency = time.time() - start_time

        results.append({
            "model": model,
            "prompt_id": i,
            "prompt": prompt,
            "answer": answer,
            "status": status,
            "error": error,
            "latency_sec": round(latency, 2),
            "answer_length": len(answer)
        })

output_dir = os.environ.get("PATH_OUTPUT") 
full_path = os.path.join(output_dir, "test_result.csv") 

os.makedirs(output_dir, exist_ok=True)
df = pd.DataFrame(results)
df.to_csv(full_path, index=False, encoding="utf-8-sig")

df