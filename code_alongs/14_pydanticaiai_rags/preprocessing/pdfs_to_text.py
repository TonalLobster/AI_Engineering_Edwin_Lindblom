from pypdf import PdfReader

all_text =""

reader = PdfReader(path)

for page in reader.pages:
    text = page.extract_text()

    all_text += text + "\n"
 return all_text

def export_text(text, export_path):
    with open(export_path, "w", encoding="utf-8") as f:
        f.write(text)