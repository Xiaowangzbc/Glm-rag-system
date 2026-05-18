from zhipuai import ZhipuAI
from config import ZHIPU_API_KEY

client = ZhipuAI(api_key=ZHIPU_API_KEY)

def ask_llm(messages):
    try:
        print("发送内容：", messages)  # 👈 打印看看
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=messages
        )
        return response.choices[0].message.content

    except Exception as e:
        print("❌ API报错：", e)
        return "出错了"
