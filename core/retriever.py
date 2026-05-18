#检索
def split_text(text, chunk_size=300):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def retrieve(chunks, query):
    # 简单关键词匹配（可升级embedding）
    scored = []
    for chunk in chunks:
        score = sum([1 for word in query if word in chunk])
        scored.append((chunk, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return [c[0] for c in scored[:3]]