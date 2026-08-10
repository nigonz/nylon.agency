import sys
import re

def insert_css():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's clean up existing VIDEO FACADE and FULLSCREEN VIDEO chunks just to avoid massive duplication
    content = re.sub(r'/\*\s*══════════════════════════════════════════\s*VIDEO FACADE - ESTILOS VISUALES[\s\S]*?(?=\s*\.vcard\s*\{|\s*@media|\s*/\*|\s*</style>)', '', content)
    content = re.sub(r'/\*\s*══════════════════════════════════════════\s*FULLSCREEN VIDEO[\s\S]*?(?=\s*\.vcard\s*\{|\s*@media|\s*/\*|\s*</style>)', '', content)
    content = re.sub(r'/\*\s*═══\s*VIDEO FACADE\s*═══[\s\S]*?(?=\s*\.vframe iframe|\s*/\*|\s*</style>)', '', content)
    content = re.sub(r'/\*\s*══════════════════════════════════════════\s*VIDEO FULLSCREEN[\s\S]*?(?=\s*@media|\s*/\*|\s*</style>)', '', content)
    
    new_css = """\n/* ══════════════════════════════════════════
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
}\n"""

    # We find the .vf-sub { ... } block (which comes after .vfooter usually) or .vfooter directly
    pattern = r'(\.vfooter\s*\{[\s\S]*?\})'
    # Actually, the user says "después de que cierre .vfooter{...}". So let's insert right there.
    
    # Wait, earlier I added .vf-title and .vf-sub after .vfooter.
    # I'll just find .vfooter block and append the new CSS there. 
    # But let's avoid placing it between .vfooter and .vf-title if we can.
    # The prompt explicitly says "AGREGAR DESPUÉS de esos bloques CSS, este código COMPLETO... PEGA EL CSS ANTERIOR JUSTO DESPUÉS de que cierre .vfooter{...}."
    
    # I will replace .vfooter block with .vfooter block + the new CSS.
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1' + new_css.replace('\\', '\\\\'), content, count=1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    insert_css()
