import sys
import re

def replace_old_script():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the block to replace. The user said:
    # Busca en el HTML esta línea exacta:
    # /* ═══════════════════════════════════════════
    #    LIGHTBOX
    # ═══════════════════════════════════════════ */
    # // ── VIDEO FACADE LAZY LOADING (DEFERRED FOR PERFORMANCE) ──
    # BORRA TODO desde esa línea hasta el final del documento (incluyendo los dos scripts LIGHTBOX al final).
    
    # Let's write a regex that catches this. There might be some encoding artifacts, so we use .*?
    pattern = r'/\*[\s═]*LIGHTBOX[\s═]*\*/\s*//[\s─]*VIDEO FACADE LAZY LOADING.*?</body>'
    
    new_script = """/* ═══════════════════════════════════════════
   VIDEO PLAYER — FUNCIONAL
═══════════════════════════════════════════ */
(function(){
  let overlay = null;
  let currentCard = null;
  let currentPlayer = null;

  // Crear overlay
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
    
    // Limpiar
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
    currentPlayer = null;
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
    
    // Esperar 300ms para que se vea el loader
    setTimeout(() => {
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
  setTimeout(() => {
    if(document.readyState === 'loading'){
      document.addEventListener('DOMContentLoaded', attachListeners);
    } else {
      attachListeners();
    }
  }, 800);
})();

/* ═══════════════════════════════════════════
   PHOTO LIGHTBOX
═══════════════════════════════════════════ */
document.querySelectorAll('.pcard[data-src]').forEach(c=>{
  c.addEventListener('click',()=>{
    document.getElementById('lbimg').src=c.dataset.src;
    document.getElementById('lb').classList.add('on');
  });
});

const lb=document.getElementById('lb');
if(document.getElementById('lbx')){
  document.getElementById('lbx').addEventListener('click',()=>lb.classList.remove('on'));
}
lb.addEventListener('click',e=>{if(e.target===lb)lb.classList.remove('on')});
document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('on')});
</script>
</body>
</html>"""
    
    # We replace everything from the first occurrence of the old LIGHTBOX + VIDEO FACADE comment to </body>
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, new_script + '\n', content, flags=re.DOTALL)
    else:
        # Fallback if pattern fails
        print("Pattern not found. Trying simpler approach.")
        idx = content.find('VIDEO FACADE LAZY LOADING (DEFERRED FOR PERFORMANCE)')
        if idx != -1:
            # Backtrack to the /* before it
            idx_start = content.rfind('/*', 0, idx)
            content = content[:idx_start] + new_script
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    replace_old_script()
