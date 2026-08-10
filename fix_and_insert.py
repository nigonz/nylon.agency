import sys
import re

def fix_and_insert():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # First, let's make sure .vf-title and .vf-sub exist right after .vfooter.
    # Currently .vfooter{ ... } is followed by /* VIDEO FACADE
    
    missing_classes = """
.vf-title {
  font-family: 'Playfair Display', serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: -0.5px;
  color: #fff;
  margin-bottom: 4px;
}

.vf-sub {
  font-family: 'Cormorant Garamond', serif;
  font-size: 11px;
  font-weight: 400;
  color: var(--teal-l);
  opacity: .75;
  letter-spacing: .5px;
}
"""

    fullscreen_css = """
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
  transition: opacity 0.4s cubic-bezier(0.22, 1, 0.36, 1), background 0.4s, backdrop-filter 0.4s, visibility 0.4s;
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

    # If .vf-sub is missing, we insert it after .vfooter
    if ".vf-sub" not in content:
        pattern = r'(\.vfooter\s*\{[\s\S]*?\})'
        content = re.sub(pattern, r'\1' + missing_classes.replace('\\', '\\\\'), content, count=1)
    
    # Strip existing FULLSCREEN VIDEO just in case it's lingering elsewhere
    content = re.sub(r'/\*\s*══════════════════════════════════════════\s*FULLSCREEN VIDEO[\s\S]*?(?=\s*@media|\s*/\*|\s*</style>)', '', content)

    # Now append fullscreen_css exactly after the newly inserted or existing .vf-sub block
    pattern_sub = r'(\.vf-sub\s*\{[\s\S]*?\})'
    content = re.sub(pattern_sub, r'\1' + fullscreen_css.replace('\\', '\\\\'), content, count=1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    fix_and_insert()
