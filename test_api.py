from zhipuai import ZhipuAI

client = ZhipuAI(api_key="91e73209c8cc486c961f6ba82a5556b9.piM9HkUIU1VrP7j1")

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "user", "content": "你好"}
    ]
)

print(response.choices[0].message.content)