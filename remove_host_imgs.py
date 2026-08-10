import sys
import re

def remove_last_row_imgs():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/host.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # Find the pgrid section
    pgrid_match = re.search(r'<div class="pgrid" id="pgrid">([\s\S]*?)</div>\s*</section>', content)
    if not pgrid_match:
        print("Could not find pgrid")
        return

    pgrid_content = pgrid_match.group(1)
    
    # Find all .fw.reveal divs which contain the cards
    cards = re.findall(r'(<div class="fw reveal"[\s\S]*?</div>\s*</div>\s*</div>)', pgrid_content)
    
    print(f"Found {len(cards)} cards in pgrid.")
    
    if len(cards) >= 4:
        # Keep all but the last 4 (assuming 4 per row, or just remove the last 4)
        new_pgrid_content = pgrid_content
        for card in cards[-4:]:
            new_pgrid_content = new_pgrid_content.replace(card, "")
        
        # Replace back in the main content
        content = content.replace(pgrid_content, new_pgrid_content)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Removed the last 4 image cards successfully.")
    else:
        print("Not enough cards to remove a row of 4.")

if __name__ == "__main__":
    remove_last_row_imgs()
