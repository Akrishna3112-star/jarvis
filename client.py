#pip install openai
from openai import OpenAI
client = OpenAI(
    api_key= "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",
)
completion  = client.chat.completions.create(
    model="gpt-4o",  # or another valid model
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

print(completion.choices[0].message.content)