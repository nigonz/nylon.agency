import sys
import io

def extract_top():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    idx = content.find('<section class="vsec">')
    if idx != -1:
        print(content[:idx])
    else:
        print('Could not find <section class="vsec">')

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    extract_top()
