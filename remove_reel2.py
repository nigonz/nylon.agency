import sys
import re

def remove_reel2():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find and remove the REEL 2 block
    # Pattern to match from <!-- REEL 2 --> to the closing </div> of that block.
    # We know the block has a comment <!-- REEL 2 --> followed by a div with class fw reveal, and it ends right before <!-- BLACKSALE -->
    
    reel2_pattern = r'<!-- REEL 2 -->[\s\S]*?(?=<!-- BLACKSALE -->)'
    content = re.sub(reel2_pattern, '', content)

    # Note: If there are dynamic CSS entries for REEL 2 (1209354393) we should leave them or remove them. The prompt says "elimina reel2 ese video no va". 
    # Let's remove its ID from the CSS aspect-ratio as well if we find it.
    content = re.sub(r'\s*\.vcard\[data-video-id="1209354393"\].*?/\*\s*REEL 2 16:9\s*\*/,?', '', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    remove_reel2()
