#向量
from core.llm import ask_llm
from core.retriever import split_text, retrieve

def ask_with_context(text, question):
    chunks = split_text(text)
    top_chunks = retrieve(chunks, question)

    context = "\n".join(top_chunks)

    messages = [
        {"role": "system", "content": "你是一个专业的知识库问答助手"},
        {"role": "user", "content": f"基于以下内容回答问题：\n{context}\n\n问题：{question}"}
    ]

    return ask_llm(messages)