#文件解析
import PyPDF2

def read_file(file):
    filename = file.name  # 👈 获取文件名

    if filename.endswith(".pdf"):
        text = ""
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    else:
        return file.read().decode("utf-8", errors="ignore")