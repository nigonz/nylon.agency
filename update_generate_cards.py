import sys
import re

def update_generate_cards():
    file_path = "c:/Users/Nigonz/OneDrive/Documentos/nylon/nylon-web 14-07 - copia/comercial_nuevo.v1.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_gen_func = """function generateCards(data, gridId) {
      const grid = document.getElementById(gridId);
      if (!grid) return;
      
      data.forEach(video => {
        const card = document.createElement('div');
        card.className = 'video-card';
        card.dataset.videoId = video.id;
        card.innerHTML = `
          <div class="video-frame">
            <div class="video-facade">
              <div class="play-btn">
                <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
              </div>
            </div>
          </div>
          <div class="video-footer">
            <div class="video-title">${video.title}</div>
            <div class="video-subtitle">${video.subtitle}</div>
          </div>
        `;
        card.addEventListener('click', () => openVideo(video.id, video.title, video.customIframe));
        grid.appendChild(card);

        // Fetch thumbnail from Vimeo API
        fetch(`https://vimeo.com/api/v2/video/${video.id}.json`)
          .then(response => response.json())
          .then(vimeoData => {
            if (vimeoData && vimeoData[0] && vimeoData[0].thumbnail_large) {
              const facade = card.querySelector('.video-facade');
              if (facade) {
                facade.style.backgroundImage = `url(${vimeoData[0].thumbnail_large})`;
                facade.style.backgroundSize = 'cover';
                facade.style.backgroundPosition = 'center';
              }
            }
          })
          .catch(err => console.error('Error fetching Vimeo thumbnail:', err));
      });
    }"""
      
    pattern = r'function generateCards\(data,\s*gridId\)\s*\{[\s\S]*?(?=generateCards\(videoData\.institucionales)'
    
    new_content = re.sub(pattern, new_gen_func.replace('\\', '\\\\') + "\n\n    ", content, count=1)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated generateCards successfully.")
    else:
        print("Could not find the target function to replace.")

if __name__ == "__main__":
    update_generate_cards()
