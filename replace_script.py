import sys

def replace_all():
    file_path = "comercial.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace Celsur, Jefatura, Deneb in <section class="vsec">
    # The first 3 .vcard blocks are for Celsur, Jefatura, Deneb.
    # We can use regex to replace them, but they are clearly marked.
    # Let's replace the whole vgrid in vsec.
    # We know the content from <section class="vsec"> to </section> contains exactly 3 cards currently.
    
    import re
    vsec_match = re.search(r'<section class="vsec">\s*<div class="vgrid">([\s\S]*?)</div>\s*</section>', content)
    if vsec_match:
        new_vsec = """
<!-- CELSUR -->
<div class="fw reveal" style="--delay:0s;--dur:6.8s;--fa:float-a">
  <div class="vcard tilt" data-video-id="1209342794">
    <div class="vframe">
      <div class="video-facade" data-video-id="1209342794">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">Celsur</div>
      <div class="vf-sub">Institucional · Vilma V1.3</div>
    </div>
  </div>
</div>

<!-- JEFATURA MI MPC -->
<div class="fw reveal" style="--delay:0.65s;--dur:8.1s;--fa:float-b">
  <div class="vcard tilt" data-video-id="935095167">
    <div class="vframe">
      <div class="video-facade" data-video-id="935095167">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">Jefatura MI MPC</div>
      <div class="vf-sub">Institucional</div>
    </div>
  </div>
</div>

<!-- DENEB S.A -->
<div class="fw reveal" style="--delay:1.30s;--dur:7.4s;--fa:float-c">
  <div class="vcard tilt" data-video-id="1209345218">
    <div class="vframe">
      <div class="video-facade" data-video-id="1209345218">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">Deneb S.A</div>
      <div class="vf-sub">Institucional · V2.3</div>
    </div>
  </div>
</div>
"""
        content = content[:vsec_match.start(1)] + new_vsec + content[vsec_match.end(1):]

    # 2. Replace MARKETING sections in psec grid
    # Reel 2, Blacksale, Desmontable Trekking, Ferrari, DFSK
    # This corresponds to the entire pgrid (or at least the first 5 cards).
    # Since the user says "reemplazar estos bloques" and the current pgrid has exactly 5 cards and one empty/placeholder.
    
    psec_match = re.search(r'<section class="psec">.*?<div class="pgrid" id="pgrid">([\s\S]*?)</div>\s*</section>', content, re.DOTALL)
    if psec_match:
        new_psec = """
<!-- REEL 2 -->
<div class="fw reveal" style="--delay:0s;--dur:7.2s;--fa:float-b">
  <div class="vcard tilt" data-video-id="1209354393">
    <div class="vframe">
      <div class="video-facade" data-video-id="1209354393">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">Reel 2</div>
      <div class="vf-sub">Contenido Promocional</div>
    </div>
  </div>
</div>

<!-- BLACKSALE -->
<div class="fw reveal" style="--delay:0.35s;--dur:8.6s;--fa:float-a">
  <div class="vcard tilt" data-video-id="1203649082">
    <div class="vframe">
      <div class="video-facade" data-video-id="1203649082">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">Blacksale</div>
      <div class="vf-sub">9x16 · 15"</div>
    </div>
  </div>
</div>

<!-- DESMONTABLE TREKKING -->
<div class="fw reveal" style="--delay:0.70s;--dur:6.9s;--fa:float-c">
  <div class="vcard tilt" data-video-id="1203649545">
    <div class="vframe">
      <div class="video-facade" data-video-id="1203649545">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">Desmontable Trekking</div>
      <div class="vf-sub">Ripstop</div>
    </div>
  </div>
</div>

<!-- FERRARI -->
<div class="fw reveal" style="--delay:1.05s;--dur:9.3s;--fa:float-a">
  <div class="vcard tilt" data-video-id="1209355971">
    <div class="vframe">
      <div class="video-facade" data-video-id="1209355971">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">Ferrari</div>
      <div class="vf-sub">Nylon · Marketing</div>
    </div>
  </div>
</div>

<!-- DFSK (mantener como está) -->
<div class="fw reveal" style="--delay:1.40s;--dur:7.7s;--fa:float-b">
  <div class="vcard tilt" data-video-id="1209347728">
    <div class="vframe">
      <div class="video-facade" data-video-id="1209347728">
        <div class="video-facade-play-btn">
          <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        </div>
      </div>
    </div>
    <div class="vfooter">
      <div class="vf-title">DFSK</div>
      <div class="vf-sub">Cariló V2.1</div>
    </div>
  </div>
</div>
"""
        content = content[:psec_match.start(1)] + new_psec + content[psec_match.end(1):]

    # 3. CSS for .vcard
    css_vcard_pattern = r'\.vcard\s*\{[\s\S]*?transform-style:preserve-3d;\s*\}'
    new_vcard_css = """\n.vcard{
  position:relative;border-radius:20px;overflow:hidden;
  background:var(--bg2);
  border:1px solid rgba(26,143,160,.16);
  box-shadow:var(--cshadow);
  transition:box-shadow .45s,transform .65s cubic-bezier(.22,1,.36,1);
  will-change:transform;
  transform-style:preserve-3d;
  max-width:360px;
  aspect-ratio:auto;
  height:auto;
}

/* Aspect ratios dinámicos por video ID */
.vcard[data-video-id="1209342794"],  /* CELSUR 9:16 */
.vcard[data-video-id="1203649082"],  /* BLACKSALE 9:16 */
.vcard[data-video-id="1203649545"]   /* DESMONTABLE 9:16 */
{
  aspect-ratio: 9 / 16;
  max-height: 520px;
}

.vcard[data-video-id="935095167"],   /* JEFATURA 16:9 */
.vcard[data-video-id="1209345218"],  /* DENEB 4:3 */
.vcard[data-video-id="1209355971"],  /* FERRARI 4:3 */
.vcard[data-video-id="1209347728"],  /* DFSK 4:3 */
.vcard[data-video-id="1209354393"]   /* REEL 2 16:9 */
{
  aspect-ratio: 16 / 9;
  max-height: 380px;
}\n"""
    content = re.sub(css_vcard_pattern, new_vcard_css, content, count=1)
    # Remove the old max-width:360px just in case
    content = re.sub(r'\.vcard\{max-width:360px;margin:0 auto;\}', '', content)

    # 4. CSS for vf-title and vf-sub
    content = re.sub(r'\.vf-title\{.*?\}', '.vf-title {\n  font-family: \'Playfair Display\', serif;\n  font-size: 15px;\n  font-weight: 600;\n  letter-spacing: -0.5px;\n  color: #fff;\n  margin-bottom: 3px;\n}', content)
    content = re.sub(r'\.vf-sub\{.*?\}', '.vf-sub {\n  font-family: \'Cormorant Garamond\', serif;\n  font-size: 11px;\n  font-weight: 400;\n  color: var(--teal-l);\n  opacity: .75;\n  letter-spacing: .5px;\n}', content)

    # 5. JS Block
    js_pattern = r'\(function\(\)\{\s*// ── VIDEO FACADE LAZY LOADING.*?\}\)\(\);'
    new_js = """(function(){
  let overlay = null;
  let currentPlayer = null;
  let loadTimeout = null;

  function initVideoFacades() {
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'video-overlay-bg';
      document.body.appendChild(overlay);
    }

    function closeFullscreen(card) {
      if (currentPlayer) {
        currentPlayer.pause?.().catch(() => {});
        currentPlayer = null;
      }
      
      card.classList.remove('video-fullscreen-active');
      overlay.classList.remove('on');

      const vframe = card.querySelector('.vframe');
      if (vframe) {
        // Recrear la fachada
        const videoId = card.dataset.videoId;
        vframe.innerHTML = `
          <div class="video-facade" data-video-id="${videoId}">
            <div class="video-facade-play-btn">
              <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
            </div>
          </div>
        `;
        vframe.querySelector('.video-facade').addEventListener('click', handleVideoClick);
      }

      const closeBtn = card.querySelector('.video-close-btn');
      if (closeBtn) closeBtn.remove();
    }

    function handleVideoClick(e) {
      e.preventDefault();
      e.stopPropagation();

      const facade = e.currentTarget;
      const videoId = facade.dataset.videoId;
      const card = facade.closest('.vcard');

      if (!card) return;

      // Mostrar loader
      facade.innerHTML = '<div class="video-facade-loading"></div>';

      clearTimeout(loadTimeout);
      loadTimeout = setTimeout(() => {
        const vframe = card.querySelector('.vframe');
        
        // Crear iframe Vimeo
        const iframeContainer = document.createElement('div');
        iframeContainer.style.cssText = 'position:absolute;inset:0;border-radius:20px 20px 0 0;';
        
        const iframe = document.createElement('iframe');
        iframe.src = `https://player.vimeo.com/video/${videoId}?color=1a8fa0&title=0&byline=0&portrait=0&autoplay=1&muted=0`;
        iframe.frameBorder = '0';
        iframe.allow = 'autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share';
        iframe.referrerPolicy = 'strict-origin-when-cross-origin';
        iframe.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:20px 20px 0 0;';
        
        iframeContainer.appendChild(iframe);
        vframe.innerHTML = '';
        vframe.appendChild(iframeContainer);

        // Fullscreen
        card.classList.add('video-fullscreen-active');
        overlay.classList.add('on');

        // Close button
        if (!card.querySelector('.video-close-btn')) {
          const closeBtn = document.createElement('div');
          closeBtn.className = 'video-close-btn';
          closeBtn.innerHTML = '✕';
          closeBtn.addEventListener('click', (ev) => {
            ev.stopPropagation();
            closeFullscreen(card);
          });
          card.appendChild(closeBtn);
        }

        // Inicializar Vimeo API si está disponible
        if (window.Vimeo?.Player) {
          try {
            currentPlayer = new Vimeo.Player(iframe);
            currentPlayer.play?.().catch(() => {});
          } catch (err) {
            console.warn('Vimeo API no disponible, iframe suficiente');
          }
        }
      }, 400);
    }

    // Overlay close
    overlay.addEventListener('click', () => {
      const active = document.querySelector('.vcard.video-fullscreen-active');
      if (active) closeFullscreen(active);
    });

    // ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const active = document.querySelector('.vcard.video-fullscreen-active');
        if (active) closeFullscreen(active);
      }
    });

    // Attach listeners to all facades
    document.querySelectorAll('.video-facade').forEach(facade => {
      facade.addEventListener('click', handleVideoClick);
    });
  }

  // Init después de 1.5s para no bloquear animaciones
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      setTimeout(initVideoFacades, 1500);
    });
  } else {
    setTimeout(initVideoFacades, 1500);
  }
})();"""
    content = re.sub(js_pattern, new_js.replace('\\', '\\\\'), content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    replace_all()
