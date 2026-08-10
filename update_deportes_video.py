import sys
import re

def update_deportes_video_playback():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/deportes.html"
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()

    # 1. Insert CSS before </style>
    css_to_insert = """
/* Modal Video Styles */
.video-overlay { position:fixed; inset:0; z-index:10000; background:rgba(0,0,0,0); backdrop-filter:blur(0px); opacity:0; visibility:hidden; pointer-events:none; transition:all 0.4s ease; }
.video-overlay.active { background:rgba(0,2,6,0.92); backdrop-filter:blur(8px); opacity:1; visibility:visible; pointer-events:auto; }
.modal-video-card { position:fixed; top:50%; left:50%; transform:translate(-50%,-50%) scale(0.9); width:min(95vw, 450px); aspect-ratio:9/16; z-index:10001; background:var(--bg2); border-radius:20px; box-shadow:0 40px 100px rgba(0,0,0,0.9),0 0 60px rgba(26,143,160,0.4); opacity:0; transition:all 0.4s ease; }
.video-overlay.active .modal-video-card { opacity:1; transform:translate(-50%,-50%) scale(1); }
.modal-close-btn { position:absolute; top:-50px; right:0; width:44px; height:44px; border-radius:50%; background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.25); display:flex; align-items:center; justify-content:center; font-size:20px; color:#fff; cursor:pointer; transition:all 0.2s; z-index:10002; }
.modal-close-btn:hover { background:rgba(26,143,160,0.4); border-color:var(--teal); }
@media(max-width:600px){ .modal-video-card { width:85vw; } .modal-close-btn { top:-45px; right:-10px; } }
"""
    # Let's see if we already have .video-overlay to avoid duplication
    if '.video-overlay.active' not in content:
        content = re.sub(r'</style>', css_to_insert + "\n</style>", content)

    # 2. Replace initVideoFacades() function
    old_init = r'function initVideoFacades\(\)\s*\{[\s\S]*?(?=\n\s*\}\n\s*//\s*──|function|document\.add)'
    # Wait, regex for function body might be tricky. Let's just find `function initVideoFacades()` and extract until we close it, or we can just replace everything from `function initVideoFacades() {` to the next function or end of script block.
    # A safer way is to find the bounds of initVideoFacades
    start_idx = content.find("function initVideoFacades()")
    if start_idx != -1:
        # Find the matching closing brace
        brace_count = 0
        end_idx = -1
        started = False
        for i in range(start_idx, len(content)):
            if content[i] == '{':
                brace_count += 1
                started = True
            elif content[i] == '}':
                brace_count -= 1
                if started and brace_count == 0:
                    end_idx = i
                    break
        
        if end_idx != -1:
            new_init = """function initVideoFacades() {
  const overlay = document.createElement('div');
  overlay.className = 'video-overlay';
  overlay.id = 'videoOverlay';
  document.body.appendChild(overlay);
  let currentModal = null;

  function closeVideo() {
    if (!currentModal) return;
    overlay.classList.remove('active');
    setTimeout(() => {
      if(currentModal) { currentModal.remove(); currentModal = null; }
    }, 400);
  }

  document.querySelectorAll('.video-facade').forEach(facade => {
    const videoId = facade.dataset.videoId;
    if (!videoId) return;

    facade.addEventListener('click', function(e) {
      e.preventDefault(); e.stopPropagation();
      if (currentModal) return;

      currentModal = document.createElement('div');
      currentModal.className = 'modal-video-card';
      currentModal.innerHTML = `
        <div class="modal-close-btn">✕</div>
        <iframe src="https://player.vimeo.com/video/${videoId}?color=02968d&title=0&byline=0&portrait=0&autoplay=1" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;inset:0;width:100%;height:100%;border-radius:20px;"></iframe>
      `;
      overlay.appendChild(currentModal);
      
      requestAnimationFrame(() => { overlay.classList.add('active'); });
      currentModal.querySelector('.modal-close-btn').addEventListener('click', closeVideo);
    });
  });

  overlay.addEventListener('click', (e) => { if (e.target === overlay) closeVideo(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeVideo(); });
}"""
            content = content[:start_idx] + new_init + content[end_idx+1:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated deportes.html video playback successfully.")

if __name__ == "__main__":
    update_deportes_video_playback()
