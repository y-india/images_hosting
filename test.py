import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {"role": "user", "content": "Give me roadmap to learn python programming from scratch."}
        ]
    })
)

print(response.json()["choices"][0]["message"]["content"])
