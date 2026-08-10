import sys
import re

def replace_all():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace CSS for .vcard and aspect ratios
    # In my previous edit I wrote:
    # .vcard{ ... }
    # /* Aspect ratios dinámicos por video ID */ ...
    # .vframe ...
    
    # Let's find .vcard{ up to /* ═══ VIDEO FACADE
    css_vcard_pattern = r'\.vcard\s*\{[\s\S]*?/\*\s*═══\s*VIDEO FACADE'
    new_vcard_css = """\n.vcard{
  position:relative;border-radius:20px;overflow:hidden;
  background:var(--bg2);
  border:1px solid rgba(26,143,160,.16);
  box-shadow:var(--cshadow);
  transition:box-shadow .45s,transform .65s cubic-bezier(.22,1,.36,1);
  will-change:transform;
  transform-style:preserve-3d;
  max-width:360px;
  margin:0 auto;
}

.vframe{
  position:relative;
  width:100%;
  aspect-ratio: 16 / 9;
  overflow:hidden;
  border-radius:20px 20px 0 0;
  background:#000;
}

/* Excepciones: 9:16 para algunos videos */
.vcard[data-video-id="1209342794"] .vframe,  /* CELSUR */
.vcard[data-video-id="1203649082"] .vframe,  /* BLACKSALE */
.vcard[data-video-id="1203649545"] .vframe   /* DESMONTABLE */
{
  aspect-ratio: 9 / 16;
}

/* ═══ VIDEO FACADE"""
    content = re.sub(css_vcard_pattern, new_vcard_css, content)

    # 2. Replace vf-title and vf-sub
    content = re.sub(r'\.vf-title\s*\{[\s\S]*?\}', '.vf-title {\n  font-family: \'Playfair Display\', serif;\n  font-size: 14px;\n  font-weight: 600;\n  letter-spacing: -0.5px;\n  color: #fff;\n  margin-bottom: 4px;\n}', content)
    content = re.sub(r'\.vf-sub\s*\{[\s\S]*?\}', '.vf-sub {\n  font-family: \'Cormorant Garamond\', serif;\n  font-size: 11px;\n  font-weight: 400;\n  color: var(--teal-l);\n  opacity: .75;\n  letter-spacing: .5px;\n}', content)

    # 3. Replace JS block
    # Note: the previous JS started with (function(){
    # let overlay = null;
    # let currentPlayer = null;
    js_pattern = r'\(function\(\)\{\s*let overlay = null;[\s\S]*?\}\)\(\);'
    new_js = """/* ═══════════════════════════════════════════
   VIDEO PLAYER — LIMPIO Y FUNCIONAL
═══════════════════════════════════════════ */
(function(){
  let overlay = null;
  let currentCard = null;

  // Crear overlay una sola vez
  function getOverlay(){
    if(!overlay){
      overlay = document.createElement('div');
      overlay.className = 'video-overlay-bg';
      document.body.appendChild(overlay);
      overlay.addEventListener('click', closeVideo);
    }
    return overlay;
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
    facade.innerHTML = `
      <div class="video-facade-play-btn">
        <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
      </div>
    `;
    facade.addEventListener('click', openVideo);
    vframe.appendChild(facade);
    
    // Cerrar modal
    currentCard.classList.remove('video-fullscreen-active');
    getOverlay().classList.remove('on');
    currentCard = null;
  }

  // Abrir video
  function openVideo(e){
    e.preventDefault();
    e.stopPropagation();
    
    const facade = e.currentTarget;
    const videoId = facade.dataset.videoId;
    const card = facade.closest('.vcard');
    
    if(!card) return;
    
    currentCard = card;
    const vframe = card.querySelector('.vframe');
    
    // Mostrar loader
    facade.innerHTML = '<div class="video-facade-loading"></div>';
    
    // Dar tiempo para que se vea el loader
    setTimeout(() => {
      // Limpiar y crear iframe
      vframe.innerHTML = '';
      
      const iframe = document.createElement('iframe');
      iframe.title = 'Vimeo Player';
      iframe.src = `https://player.vimeo.com/video/${videoId}?autoplay=1&color=1a8fa0&title=0&byline=0&portrait=0`;
      iframe.frameBorder = '0';
      iframe.allow = 'autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share';
      iframe.referrerPolicy = 'strict-origin-when-cross-origin';
      iframe.style.cssText = `
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        border-radius: 20px 20px 0 0;
      `;
      
      vframe.appendChild(iframe);
      
      // Fullscreen
      card.classList.add('video-fullscreen-active');
      getOverlay().classList.add('on');
      
      // Close button
      let closeBtn = card.querySelector('.video-close-btn');
      if(!closeBtn){
        closeBtn = document.createElement('div');
        closeBtn.className = 'video-close-btn';
        closeBtn.innerHTML = '✕';
        closeBtn.addEventListener('click', (ev) => {
          ev.stopPropagation();
          closeVideo();
        });
        card.appendChild(closeBtn);
      }
    }, 300);
  }

  // Attach listeners
  function attachListeners(){
    document.querySelectorAll('.video-facade').forEach(facade => {
      facade.removeEventListener('click', openVideo);
      facade.addEventListener('click', openVideo);
    });
  }

  // ESC key
  document.addEventListener('keydown', (e) => {
    if(e.key === 'Escape' && currentCard){
      closeVideo();
    }
  });

  // Init
  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', attachListeners);
  } else {
    attachListeners();
  }
})();"""
    content = re.sub(js_pattern, new_js.replace('\\', '\\\\'), content, count=1)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    replace_all()
