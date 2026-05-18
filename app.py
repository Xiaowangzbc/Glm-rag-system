import streamlit as st
from core.parser import read_file
from core.rag import rag_ask

# ===== 模拟用户数据库 =====
USERS = {
    "admin": "admin",
    "test": "admin"
}

# ===== 初始化登录状态 =====
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ===== 登录函数 =====
def login():
    st.title("🔐 用户登录")

    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")

    if st.button("登录"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.success("登录成功！")
            st.rerun()
        else:
            st.error("用户名或密码错误")

# ===== 主界面 =====
def main_app():
    st.title("🧠 AI 知识库问答系统")

    if st.button("退出登录"):
        st.session_state.logged_in = False
        st.rerun()

    uploaded_file = st.file_uploader("上传文档", type=["txt", "pdf"])

    if uploaded_file:
        text = read_file(uploaded_file)
        st.success("文档加载成功")

        question = st.text_input("请输入问题")

        if question:
            answer = rag_ask(text, question)
            st.write("🤖 回答：")
            st.write(answer)

# ===== 路由控制 =====
if st.session_state.logged_in:
    main_app()
else:
    login()