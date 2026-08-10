import sys

def search_html():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/host.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # Search for the string 'namecard' but ensure we get the HTML part, not the CSS part
    # CSS usually is inside <style>, HTML is inside <main> or <body>
    html_start = content.find('</style>')
    if html_start != -1:
        idx = content.find('namecard', html_start)
        if idx != -1:
            print(content[idx-100:idx+1000])
        else:
            print("NOT FOUND in HTML body")
    else:
        print("Could not separate CSS from HTML")

if __name__ == "__main__":
    search_html()
