import sys
import re

def replace_css_blocks():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Block 1 replacement: From VIDEO SECTION (Vimeo) to .vf-sub
    pattern_vsec = r'/\* ══════════════════════════════════════════\s*VIDEO SECTION \(Vimeo\)\s*══════════════════════════════════════════ \*/[\s\S]*?\.vf-sub\s*\{[\s\S]*?\}'
    
    new_vsec = """/* ══════════════════════════════════════════
   VIDEO SECTION (Vimeo) - REDISEÑADO
══════════════════════════════════════════ */
.vsec{
  position:relative;z-index:10;
  padding:34px 44px 0;
  max-width:1260px;
  margin:0 auto;
  width:100%;
}

.vgrid{
  display:grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 22px;
  perspective:1400px;
  perspective-origin:50% 30%;
}

.fw{
  animation:var(--fa,float-a) var(--dur,6s) ease-in-out infinite;
  animation-delay:var(--delay,0s);
}

/* Video card */
.vcard{
  position:relative;
  border-radius:20px;
  overflow:hidden;
  background:var(--bg2);
  border:1px solid rgba(26,143,160,.16);
  box-shadow:var(--cshadow);
  transition:box-shadow .45s,transform .65s cubic-bezier(.22,1,.36,1);
  will-change:transform;
  transform-style:preserve-3d;
  width:100%;
}

.vframe{
  position:relative;
  width:100%;
  aspect-ratio: 16 / 9;
  overflow:hidden;
  border-radius:20px 20px 0 0;
  background:#000;
}

/* Excepciones: 9:16 para videos verticales */
.vcard[data-video-id="1209342794"] .vframe,
.vcard[data-video-id="1203649082"] .vframe,
.vcard[data-video-id="1203649545"] .vframe
{
  aspect-ratio: 9 / 16;
}

/* ═══ VIDEO FACADE ═══ */
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

.video-facade::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(26, 143, 160, 0.1) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.video-facade:hover {
  background: linear-gradient(135deg, #0f0f1a 0%, #1f1f3e 100%);
}

.video-facade:hover::before {
  opacity: 1;
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
  filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3));
}

.video-facade-loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60px;
  height: 60px;
  border: 3px solid rgba(26, 143, 160, 0.2);
  border-top: 3px solid var(--teal);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: translate(-50%, -50%) rotate(0deg); }
  100% { transform: translate(-50%, -50%) rotate(360deg); }
}

.vframe iframe{
  position:absolute;
  inset:0;
  width:100%;
  height:100%;
  border:0;
  border-radius:20px 20px 0 0;
}

/* Card footer */
.vfooter{
  padding:13px 16px 16px;
  background:linear-gradient(to bottom,rgba(0,8,18,.82),rgba(0,10,22,.95));
  border-top:1px solid rgba(26,143,160,.14);
}

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
}"""

    # We first try to replace this block
    if re.search(pattern_vsec, content):
        content = re.sub(pattern_vsec, new_vsec.replace('\\', '\\\\'), content, count=1)
    else:
        print("Could not find VIDEO SECTION pattern.")

    # Block 2 replacement: From .video-overlay-bg to .video-close-btn:hover (or just before </style> or <script)
    # The user says "Luego busca .vcard.video-fullscreen-active y REEMPLAZALO: /* ══ VIDEO FULLSCREEN ══ */ .video-overlay-bg{ ... }"
    # We will replace from .video-overlay-bg to the end of the style block (or just the media queries if we match carefully).
    
    pattern_fullscreen = r'\.video-overlay-bg\s*\{[\s\S]*?(?=\s*</style>)'
    
    new_fullscreen = """/* ══════════════════════════════════════════
   VIDEO FULLSCREEN
══════════════════════════════════════════ */
.video-overlay-bg{
  position:fixed;
  inset:0;
  z-index:999;
  background:rgba(0,0,0,0);
  backdrop-filter:blur(0px);
  opacity:0;
  visibility:hidden;
  pointer-events:none;
  transition:opacity .4s cubic-bezier(.22,1,.36,1),background .4s,backdrop-filter .4s,visibility .4s;
}

.video-overlay-bg.on{
  background:rgba(0,0,0,.92);
  backdrop-filter:blur(8px);
  opacity:1;
  visibility:visible;
  pointer-events:auto;
}

.vcard.video-fullscreen-active{
  position:fixed !important;
  top:50% !important;
  left:50% !important;
  transform:translate(-50%,-50%) !important;
  width:min(95vw, 95vh * 9 / 16) !important;
  height:min(95vh, 95vw * 16 / 9) !important;
  max-width:1200px !important;
  max-height:85vh !important;
  z-index:1000 !important;
  transition:all .45s cubic-bezier(.22,1,.36,1);
  box-shadow:0 40px 100px rgba(0,0,0,.9),0 0 60px rgba(26,143,160,.4);
}

.vcard.video-fullscreen-active[data-video-id="1209342794"],
.vcard.video-fullscreen-active[data-video-id="1203649082"],
.vcard.video-fullscreen-active[data-video-id="1203649545"]
{
  width:min(95vh * 9 / 16, 95vw) !important;
  height:min(95vh, 95vw * 16 / 9) !important;
}

.vcard.video-fullscreen-active .vframe{
  height:100%;
  border-radius:20px;
}

.vcard.video-fullscreen-active .vfooter{
  display:none;
}

.video-close-btn{
  position:absolute;
  top:-50px;
  right:0;
  z-index:1001;
  width:44px;
  height:44px;
  border-radius:50%;
  background:rgba(255,255,255,.12);
  border:1px solid rgba(255,255,255,.25);
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:20px;
  color:#fff;
  cursor:pointer;
  transition:background .2s,border-color .2s;
  opacity:0;
  visibility:hidden;
}

.vcard.video-fullscreen-active .video-close-btn{
  opacity:1;
  visibility:visible;
}

.video-close-btn:hover{
  background:rgba(26,143,160,.4);
  border-color:var(--teal);
}

@media(max-width:900px){
  .vgrid{grid-template-columns:repeat(auto-fit, minmax(280px, 1fr))}
}

@media(max-width:600px){
  .vgrid{grid-template-columns:1fr}
  .vcard.video-fullscreen-active{
    width:95vw !important;
    height:auto !important;
  }
}
"""

    if re.search(pattern_fullscreen, content):
        content = re.sub(pattern_fullscreen, new_fullscreen.replace('\\', '\\\\'), content, count=1)
    else:
        print("Could not find FULLSCREEN pattern.")
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    replace_css_blocks()
