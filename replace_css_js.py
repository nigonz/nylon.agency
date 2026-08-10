import sys
import re

def replace_css_and_js():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Block 1 replacement: .vgrid down to before VIDEO FACADE
    pattern_vgrid = r'\.vgrid\s*\{[\s\S]*?(?=\s*/\*\s*═══\s*VIDEO FACADE)'
    
    new_vgrid = """.vgrid{
  display:grid;
  grid-template-columns: repeat(3, 1fr);
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

/* Verticales: 9:16 */
.vcard[data-video-id="1209342794"] .vframe,
.vcard[data-video-id="1203649082"] .vframe,
.vcard[data-video-id="1203649545"] .vframe
{
  aspect-ratio: 9 / 16;
}

@media(max-width:1024px){
  .vgrid{grid-template-columns: repeat(2, 1fr)}
}

@media(max-width:600px){
  .vgrid{grid-template-columns: 1fr}
}
"""

    if re.search(pattern_vgrid, content):
        content = re.sub(pattern_vgrid, new_vgrid.replace('\\', '\\\\'), content, count=1)
    else:
        print("Could not find .vgrid pattern.")

    # Remove duplicate media queries if any exist from previous CSS at the bottom of the file (from .video-close-btn:hover down)
    content = re.sub(r'@media\(max-width:900px\)\{\s*\.vgrid\{grid-template-columns:repeat\(auto-fit, minmax\(280px, 1fr\)\)\}\s*\}\s*@media\(max-width:600px\)\{\s*\.vgrid\{grid-template-columns:1fr\}\s*\.vcard\.video-fullscreen-active\{\s*width:95vw !important;\s*height:auto !important;\s*\}\s*\}', '', content)


    # Block 2: VIDEO PLAYER
    pattern_js = r'/\*\s*═══════════════════════════════════════════\s*VIDEO PLAYER — FUNCIONAL\s*═══════════════════════════════════════════\s*\*/[\s\S]*?(?=</script>)'
    
    new_js = """/* ═══════════════════════════════════════════
   VIDEO PLAYER — FUNCIONAL v2
═══════════════════════════════════════════ */
(function(){
  let currentCard = null;
  let overlay = null;

  // Crear overlay
  function createOverlay(){
    if(overlay) return overlay;
    
    overlay = document.createElement('div');
    overlay.className = 'video-overlay-bg';
    overlay.addEventListener('click', closeVideo);
    document.body.appendChild(overlay);
    
    return overlay;
  }

  // Abrir video
  function openVideo(e){
    e.preventDefault();
    e.stopPropagation();
    
    const facade = this;
    const videoId = facade.dataset.videoId;
    const card = facade.closest('.vcard');
    
    if(!card || currentCard) return;
    currentCard = card;
    
    // Mostrar loader
    facade.innerHTML = '<div class="video-facade-loading"></div>';
    
    // Esperar para que se vea el loader
    setTimeout(() => {
      const vframe = card.querySelector('.vframe');
      if(!vframe) return;
      
      // Crear iframe
      vframe.innerHTML = '';
      const iframe = document.createElement('iframe');
      iframe.src = `https://player.vimeo.com/video/${videoId}?autoplay=1&color=1a8fa0&title=0&byline=0&portrait=0&muted=1`;
      iframe.allow = 'autoplay; fullscreen; picture-in-picture';
      iframe.frameBorder = '0';
      iframe.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;border-radius:20px 20px 0 0;';
      vframe.appendChild(iframe);
      
      // Fullscreen
      card.classList.add('video-fullscreen-active');
      createOverlay().classList.add('on');
      
      // Close button
      if(!card.querySelector('.video-close-btn')){
        const btn = document.createElement('div');
        btn.className = 'video-close-btn';
        btn.innerHTML = '✕';
        btn.onclick = (ev) => {
          ev.stopPropagation();
          closeVideo();
        };
        card.appendChild(btn);
      }
    }, 300);
  }

  // Cerrar video
  function closeVideo(){
    if(!currentCard) return;
    
    const vframe = currentCard.querySelector('.vframe');
    const videoId = currentCard.dataset.videoId;
    
    // Limpiar iframe
    vframe.innerHTML = '';
    
    // Recrear fachada
    const facade = document.createElement('div');
    facade.className = 'video-facade';
    facade.dataset.videoId = videoId;
    facade.innerHTML = `<div class="video-facade-play-btn">
      <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
    </div>`;
    facade.onclick = openVideo;
    vframe.appendChild(facade);
    
    // Cerrar overlay
    currentCard.classList.remove('video-fullscreen-active');
    if(overlay) overlay.classList.remove('on');
    
    const btn = currentCard.querySelector('.video-close-btn');
    if(btn) btn.remove();
    
    currentCard = null;
  }

  // Inicializar
  function init(){
    document.querySelectorAll('.video-facade').forEach(facade => {
      facade.onclick = openVideo;
    });
  }

  // ESC key
  document.addEventListener('keydown', (e) => {
    if(e.key === 'Escape' && currentCard){
      closeVideo();
    }
  });

  // Init después de que cargue el DOM
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

/* ═══════════════════════════════════════════
   PHOTO LIGHTBOX
═══════════════════════════════════════════ */
const lb = document.getElementById('lb');
const lbx = document.getElementById('lbx');
if(lbx) lbx.onclick = () => lb.classList.remove('on');
lb.onclick = (e) => { if(e.target === lb) lb.classList.remove('on'); };
document.addEventListener('keydown', (e) => {
  if(e.key === 'Escape') lb.classList.remove('on');
});
"""

    if re.search(pattern_js, content):
        content = re.sub(pattern_js, new_js.replace('\\', '\\\\'), content, count=1)
    else:
        print("Could not find VIDEO PLAYER pattern.")
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    replace_css_and_js()
