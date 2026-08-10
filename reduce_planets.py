import sys

def reduce_planets():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/comercial_nuevo.v1.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The loop creating the particles (planets) in the orbit animation is:
    # for (let i = 0; i < 60; i++) {
    
    # We replace 60 with 7
    new_content = content.replace("for (let i = 0; i < 60; i++) {", "for (let i = 0; i < 7; i++) {")

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Replaced 60 with 7 successfully.")
    else:
        print("Could not find the target string to replace.")

if __name__ == "__main__":
    reduce_planets()
