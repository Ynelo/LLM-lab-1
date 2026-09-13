import os
import time
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["API_KEY"], # задавать в .env 
    base_url="https://foundation-models.api.cloud.ru/v1"
)

with open("prompt.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

models = [
    "anthropic/claude-sonnet-4.6",
    "anthropic/claude-sonnet-4",
    "openai/gpt-5.4-nano",
    "openai/gpt-4.1-nano",
    "deepseek-ai/DeepSeek-V4-Flash",
    "deepseek/deepseek-v3.2"
]

prompts = [
    file_content + "\nКратко перескажи текст приведённый в этом запросе",
    file_content + "\nСоставть хронологический план по событиям текста приведённого в этом запросе",
    file_content + "\nОбъясни основную идею текста приведённого в этом запросе",
    file_content + "\nСократи текст приведённый в этом запросе",
    file_content + "\nСделай рюземе текста приведённого в этом запросе"

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
                max_tokens=1600
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

output_dir = os.environ.get("PATH_OUTPUT") # задавать в .env
full_path = os.path.join(output_dir, "result-of-prompts.csv") 

os.makedirs(output_dir, exist_ok=True)
df = pd.DataFrame(results)
df.to_csv(full_path, index=False, encoding="utf-8-sig")

df