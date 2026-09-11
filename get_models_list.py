import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["API_KEY"], # задавать в .env
    base_url="https://foundation-models.api.cloud.ru/v1"
)

models = client.models.list()

for model in models.data:
    print(model.id)

"""
ai-sage/GigaChat3.5-432B-A28B
GigaChat/GigaChat-2-Max
ai-sage/GigaChat3-10B-A1.8B
hivetrace/HiveTraceGuard-Pro
zai-org/GLM-5.1
moonshotai/Kimi-K2.6
deepseek-ai/DeepSeek-V4-Pro
MiniMaxAI/MiniMax-M3
MiniMaxAI/MiniMax-M2.5
zai-org/GLM-4.7
openai/gpt-oss-120b
Qwen/Qwen3.5-397B-A17B
Qwen/Qwen3.6-35B-A3B
Qwen/Qwen3-Coder-Next
Qwen/Qwen3-Embedding-0.6B
Qwen/Qwen3-VL-Embedding-2B
Qwen/Qwen3-VL-Embedding-8B
BAAI/bge-m3
Qwen/Qwen3-Reranker-0.6B
Qwen/Qwen3-VL-Reranker-2B
Qwen/Qwen3-VL-Reranker-8B
BAAI/bge-reranker-v2-m3
deepseek-ai/DeepSeek-OCR-2
openai/whisper-large-v3
openai/gpt-5.5-pro
openai/gpt-5.5
openai/gpt-5.4-pro
openai/gpt-5.4
openai/gpt-5.4-mini
openai/gpt-5.4-nano
openai/gpt-5.3-codex
openai/gpt-5.3-chat
openai/gpt-5.2-codex
openai/gpt-5.2-chat
openai/gpt-5.2
openai/gpt-5.1-chat
openai/gpt-5.1
openai/gpt-5-chat
openai/gpt-5
openai/gpt-5-mini
openai/gpt-5-nano
openai/gpt-4.1
openai/gpt-4.1-mini
openai/gpt-4.1-nano
openai/chatgpt-4o-latest
openai/gpt-4o-mini
openai/o3-deep-research
openai/gpt-oss-20b
openai/text-embedding-3-large
openai/text-embedding-3-small
anthropic/claude-opus-4.8
anthropic/claude-opus-4.7
anthropic/claude-opus-4.6
anthropic/claude-opus-4.5
anthropic/claude-opus-4.1
anthropic/claude-sonnet-4.6
anthropic/claude-sonnet-4.5
anthropic/claude-haiku-4.5
anthropic/claude-sonnet-4
google/gemini-3.1-pro-preview
google/gemini-3.1-flash-lite
google/gemini-3.1-flash-image-preview
google/gemini-3-pro-image-preview
google/gemini-3-flash-preview
google/gemini-2.5-pro
google/gemini-2.5-flash-image
google/gemini-2.5-flash
google/gemini-embedding-001
qwen/qwen3-235b-a22b
zai-org/GLM-5.2
z-ai/glm-5
z-ai/glm-4.6
z-ai/glm-4.6v
z-ai/glm-4.5-air
xiaomi/mimo-v2.5
xiaomi/mimo-v2.5-pro
qwen/qwen3-max-thinking
qwen/qwen3-vl-235b-a22b-instruct
qwen/qwen3-vl-235b-a22b-thinking
qwen/qwen3-vl-30b-a3b-instruct
qwen/qwen3-vl-30b-a3b-thinking
qwen/qwen3-vl-8b-instruct
qwen/qwen3-vl-8b-thinking
moonshotai/kimi-k2.5
moonshotai/kimi-k2-thinking
moonshotai/kimi-k2-0905
meta-llama/llama-3.3-70b-instruct
deepseek/deepseek-v3.2-speciale
deepseek/deepseek-v3.2
deepseek/deepseek-chat-v3-0324
deepseek/deepseek-r1-distill-llama-70b
deepseek-ai/DeepSeek-V4-Flash
deepseek-ai/DeepSeek-V3.1-Terminus
deepseek-ai/DeepSeek-V3
deepseek-ai/DeepSeek-R1-0528
Qwen/Qwen3-30B-A3B
Qwen/Qwen3-32B
meituan-longcat/LongCat-Flash-Chat
"""