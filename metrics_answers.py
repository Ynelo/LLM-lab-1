import re
import pandas as pd
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def count_links(text):
    return len(re.findall(r"https?://\S+", text))

def count_years(text):
    return len(re.findall(r"\b(19|20)\d{2}\b", text))

def count_numbers(text):
    return len(re.findall(r"\b\d+[\d.,]*\b", text))

def count_caution_markers(text):
    markers = [
        "возможно",
        "вероятно",
        "нужно проверить",
        "нужно уточнить",
        "недостаточно данных",
        "зависит от",
        "требуется проверка",
        "скорее всего",
        "по всей видимости",
        "по-видимому",
        "предположительно",
        "судя по всему",
        "насколько мне известно",
        "насколько я понимаю",
        "если не ошибаюсь",
        "не уверен",
        "не уверена",
        "сложно сказать однозначно",
        "трудно сказать",
        "не могу утверждать наверняка",
        "по некоторым данным",
        "по имеющимся данным",
        "в определённой степени",
        "отчасти",
        "частично",
        "условно",
        "как мне кажется",
        "на мой взгляд",
        "требует дополнительной проверки",
        "требует дополнительного анализа",
        "требует уточнения",
        "нужны дополнительные данные",
        "нужно больше информации",
        "есть вероятность",
        "существует вероятность",
        "не исключено",
        "не исключено, что",
        "допустим",
        "предположим",
        "гипотетически",
        "в теории",
        "теоретически",
        "ориентировочно",
        "примерно",
        "приблизительно",
        "порядка",
        "условно говоря",
        "грубо говоря",
        "если я правильно понимаю",
        "вроде бы",
        "кажется",
        "похоже",
        "похоже, что",
        "видимо",
        "по идее",
        "в принципе",
        "как минимум",
        "как максимум",
        "в лучшем случае",
        "в худшем случае",
        "под вопросом",
        "остаётся открытым",
        "нет однозначного ответа",
        "нельзя утверждать с уверенностью",
        "нельзя исключать"
    ]
    text_lower = text.lower()
    return sum(text_lower.count(marker) for marker in markers)

file_name_import = "test_result.csv" # Указать файл CSV !!!
output_dir = os.environ.get("PATH_OUTPUT") # задавать в .env
full_path = os.path.join(output_dir, file_name_import) 
df = pd.read_csv(full_path)

df["links_count"] = df["answer"].apply(count_links)
df["years_count"] = df["answer"].apply(count_years)
df["numbers_count"] = df["answer"].apply(count_numbers)
df["caution_markers_count"] = df["answer"].apply(count_caution_markers)

df.to_csv(f"{full_path[:-4]}_with_metrics.csv", index=False, encoding="utf-8-sig")

df
