import sys
import re

def remove_videos():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/comercial_nuevo.v1.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_promocional = """promocional: [
        {
          id: '1209355971',
          title: 'Ferrari',
          subtitle: 'Nylon · Marketing',
        },
        {
          id: '1203649082',
          title: 'Blacksale',
          subtitle: '9x16 · 15"',
        },
        {
          id: '1203649545',
          title: 'Desmontable Trekking',
          subtitle: 'Ripstop',
        }
      ]"""
      
    # Replace the promocional array exactly
    # Since we know the previous content, we can match from "promocional: [" to "]" before "};"
    pattern = r'promocional:\s*\[[\s\S]*?\](?=\s*\};)'
    
    new_content = re.sub(pattern, new_promocional.replace('\\', '\\\\'), content, count=1)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated successfully.")
    else:
        print("Could not find the target string to replace.")

if __name__ == "__main__":
    remove_videos()
