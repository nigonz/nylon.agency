import sys
import re

def add_deportes_media_queries():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    media_queries_to_add = """
/* Tablet and smaller desktop */
@media (max-width: 950px) {
  .vgrid { 
    grid-template-columns: 1fr !important;
    max-width: 600px !important;
  }
}

/* Mobile phones */
@media (max-width: 600px) {
  .vcard { 
    height: 220px !important;
    border-radius: 12px !important;
  }
  .vfooter { 
    padding: 0 16px !important;
  }
  .vf-title { 
    font-size: 16px !important;
  }
  .vf-sub { 
    font-size: 11px !important;
  }
}
"""

    # We use !important just to absolutely guarantee they override anything else 
    # (since the user stressed "CRITICAL: Ensure these media queries override").
    # Alternatively, just placing them at the bottom before </style> is standard.
    # The user's provided CSS didn't have !important, so I will inject exactly what they gave, 
    # plus the guarantee of being at the very bottom.
    
    exact_css_from_user = """
/* Tablet and smaller desktop */
@media (max-width: 950px) {
  .vgrid { 
    grid-template-columns: 1fr;
    max-width: 600px;
  }
}

/* Mobile phones */
@media (max-width: 600px) {
  .vcard { 
    height: 220px;
    border-radius: 12px;
  }
  .vfooter { 
    padding: 0 16px;
  }
  .vf-title { 
    font-size: 16px;
  }
  .vf-sub { 
    font-size: 11px;
  }
}
"""
    # Just in case there are old responsive media queries for vgrid, we should probably strip them to avoid conflicts.
    # Let's just remove any previous @media(max-width:1024px) or similar that contains .vgrid
    content = re.sub(r'@media\s*\(\s*max-width:\s*1024px\s*\)\s*\{\s*\.vgrid\s*\{.*?\}\s*\}', '', content, flags=re.DOTALL)
    content = re.sub(r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{\s*\.vgrid\s*\{.*?\}\s*\}', '', content, flags=re.DOTALL)

    # Now append the new media queries right before </style>
    if '/* Tablet and smaller desktop */' not in content:
        content = re.sub(r'</style>', exact_css_from_user + "\n</style>", content, count=1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html media queries successfully.")

if __name__ == "__main__":
    add_deportes_media_queries()
