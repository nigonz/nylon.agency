const fs = require('fs');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\eventos.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Correct the name typo
html = html.replace(/Matías Molí/g, 'Matías Molinero');
html = html.replace(/Matas Mol/g, 'Matías Molinero');

// 2. Override the grid in @media(max-width:600px)
const oldGridCSS = `  .vgrid{grid-template-columns:1fr}
  .pgrid{grid-template-columns:1fr}`;

const newGridCSS = `  .vgrid, .pgrid {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 15px !important;
      padding: 2vh 4vw 10vh 4vw !important;
      overflow-x: hidden !important;
      width: 100% !important;
  }

  .vcard, .pcard {
      width: 100% !important;
      min-width: 0 !important;
      height: auto !important;
      min-height: 200px !important;
      margin: 0 !important;
  }

  .vcard .vf-title, .vcard h2, .vcard h3, .pcard h2, .pcard h3 {
      font-size: 1rem !important;
  }
  .vcard .vf-sub, .vcard p, .pcard p {
      font-size: 0.7rem !important;
  }`;

html = html.replace(oldGridCSS, newGridCSS);

// 3. Update the media tags
// Update all iframes to video tags with the requested attributes
// The prompt said: "For all 6 <video ...> tags, update their attributes to be strictly: playsinline muted loop preload="none"."
html = html.replace(/<iframe[\s\S]*?src="([^"]+)"[\s\S]*?<\/iframe>/g, (match, src) => {
    // clean up the src if needed, or just leave it
    return `<video src="${src}" playsinline muted loop preload="none"></video>`;
});

// For all 4 <img ...> tags in this section, add the attribute loading="lazy"
// Actually, they already have loading="lazy" as seen in the view_file:
// <img src="fotos/d1.jpg" alt="Drone Shot 1" loading="lazy">
// We will just enforce it just in case
html = html.replace(/<img( [^>]*)?>/g, (match, group1) => {
    if (!match.includes('loading="lazy"')) {
        return `<img${group1 || ''} loading="lazy">`;
    }
    return match;
});

// Crucial Mobile JS: Ensure that autoplay is NOT hardcoded on all 6 videos.
// We removed autoplay when replacing the iframe/video tag, we used playsinline muted loop preload="none".
// Let's also add a small JS snippet at the end of the body to handle intersection observer for playing videos on mobile

const jsSnippet = `
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const videos = document.querySelectorAll("video");
    const isMobile = window.matchMedia("(max-width: 600px)").matches;
    
    if (isMobile && videos.length > 0) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.play().catch(e => console.log("Autoplay prevented:", e));
          } else {
            entry.target.pause();
          }
        });
      }, { threshold: 0.5 });
      
      videos.forEach(vid => {
        // Prevent hardcoded autoplay on mobile
        vid.autoplay = false; 
        observer.observe(vid);
        
        // Ensure play on tap
        vid.addEventListener("click", () => {
          if (vid.paused) vid.play();
          else vid.pause();
        });
      });
    }
  });
</script>
</body>`;

html = html.replace(/<\/body>/i, jsSnippet);

fs.writeFileSync(file, html, 'utf8');
console.log("Updates applied successfully.");
