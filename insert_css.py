import sys
import re

def insert_css():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The user wants to paste the new CSS after .vfooter
    # But wait, we already have .video-facade and .video-overlay-bg in the file.
    # We should probably remove the old ones to avoid duplicates.
    # Let's remove the old VIDEO FACADE and VIDEO FULLSCREEN blocks if they exist.
    
    # Remove old VIDEO FACADE block
    content = re.sub(r'/\*\s*═══\s*VIDEO FACADE\s*═══\s*\*/[\s\S]*?(?=\.vframe iframe)', '', content)
    
    # Remove old VIDEO FULLSCREEN block
    content = re.sub(r'/\*\s*══════════════════════════════════════════\s*VIDEO FULLSCREEN[\s\S]*?(?=@media\(max-width:1024px\))', '', content)
    
    # Now find .vfooter{...} or .vf-sub{...} to insert after
    # Because .vf-title and .vf-sub are currently right after .vfooter
    # Let's insert after .vf-sub { ... }
    
    new_css = """
/* ══════════════════════════════════════════
   VIDEO FACADE - ESTILOS VISUALES
══════════════════════════════════════════ */

.video-facade {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 100%);
  border-radius: 20px 20px 0 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;
}

.video-facade-play-btn {
  position: relative;
  width: 80px;
  height: 80px;
  background: rgba(26, 143, 160, 0.9);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  box-shadow: 0 8px 32px rgba(26, 143, 160, 0.3);
}

.video-facade:hover .video-facade-play-btn {
  transform: scale(1.1);
  background: rgba(26, 143, 160, 1);
  box-shadow: 0 12px 48px rgba(26, 143, 160, 0.5);
}

.video-facade-play-btn svg {
  width: 32px;
  height: 32px;
  fill: #ffffff;
  margin-left: 4px;
}

.video-facade-loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60px;
  height: 60px;
  border: 3px solid rgba(26, 143, 160, 0.2);
  border-top: 3px solid var(--teal, #1a8fa0);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: translate(-50%, -50%) rotate(0deg); }
  100% { transform: translate(-50%, -50%) rotate(360deg); }
}

/* ══════════════════════════════════════════
   FULLSCREEN VIDEO
══════════════════════════════════════════ */

.video-overlay-bg {
  position: fixed;
  inset: 0;
  z-index: 999;
  background: rgba(0, 0, 0, 0);
  backdrop-filter: blur(0px);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.4s cubic-bezier(0.22, 1, 0.36, 1),
              background 0.4s,
              backdrop-filter 0.4s,
              visibility 0.4s;
}

.video-overlay-bg.on {
  background: rgba(0, 0, 0, 0.92);
  backdrop-filter: blur(8px);
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.vcard.video-fullscreen-active {
  position: fixed !important;
  top: 50% !important;
  left: 50% !important;
  transform: translate(-50%, -50%) !important;
  width: min(95vw, 1200px) !important;
  height: auto !important;
  max-height: 90vh !important;
  z-index: 1000 !important;
  transition: all 0.45s cubic-bezier(0.22, 1, 0.36, 1);
  box-shadow: 0 40px 100px rgba(0, 0, 0, 0.9), 0 0 60px rgba(26, 143, 160, 0.4);
}

.vcard.video-fullscreen-active .vframe {
  height: auto;
  max-height: 80vh;
  border-radius: 20px;
}

.vcard.video-fullscreen-active .vfooter {
  display: none;
}

.video-close-btn {
  position: absolute;
  top: -50px;
  right: 0;
  z-index: 1001;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: #fff;
  cursor: pointer;
  transition: background 0.2s, border-color 0.2s;
  opacity: 0;
  visibility: hidden;
}

.vcard.video-fullscreen-active .video-close-btn {
  opacity: 1;
  visibility: visible;
}

.video-close-btn:hover {
  background: rgba(26, 143, 160, 0.4);
  border-color: var(--teal, #1a8fa0);
}
"""
    # Insert right before @media(max-width:1024px)
    insert_pattern = r'(@media\(max-width:1024px\))'
    if re.search(insert_pattern, content):
        content = re.sub(insert_pattern, new_css.replace('\\', '\\\\') + r'\1', content, count=1)
    else:
        # fallback, just search for .vfooter { ... } or similar
        print("Fallback insertion")
        pass

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    insert_css()
