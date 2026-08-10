import sys

def debug_html():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/host.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    html_start = content.find('</style>')
    if html_start != -1:
        idx = content.find('namecard', html_start)
        if idx != -1:
            with open("debug.txt", "w", encoding="utf-8") as out:
                out.write(content[idx-100:idx+2000])
            print("Wrote to debug.txt")
        else:
            print("NOT FOUND in HTML body")
    else:
        print("Could not separate CSS from HTML")

if __name__ == "__main__":
    debug_html()
