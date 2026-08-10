import sys
import re

def restore_3rd_card():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/host.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    pgrid_match = re.search(r'<div class="pgrid" id="pgrid">([\s\S]*?)</div>\s*</section>', content)
    if not pgrid_match:
        print("Could not find pgrid")
        return

    pgrid_content = pgrid_match.group(1)
    cards = re.findall(r'(<div class="fw reveal"[\s\S]*?</div>\s*</div>\s*</div>)', pgrid_content)
    
    if len(cards) == 2:
        # Duplicate the first card to make 3
        new_card = cards[0].replace('float-a', 'float-c').replace('delay:0s', 'delay:1.2s')
        new_pgrid_content = pgrid_content + "\n" + new_card
        content = content.replace(pgrid_content, new_pgrid_content)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Restored 1 card to make a complete row of 3.")
    else:
        print(f"Expected 2 cards, found {len(cards)}.")

if __name__ == "__main__":
    restore_3rd_card()
