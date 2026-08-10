const fs = require('fs');
const path = require('path');

const ugcPath = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\ugc.html';
const photosDir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\fotos\\\\diseño';

let html = fs.readFileSync(ugcPath, 'utf8');

// 1. Remove the Videos section completely
const videoStart = html.indexOf('<!-- ═══ VIDEOS (Vimeo) ═══ -->');
const photoStart = html.indexOf('<!-- ═══ PHOTOS ═══ -->');
if (videoStart !== -1 && photoStart !== -1) {
    html = html.substring(0, videoStart) + html.substring(photoStart);
}

// 2. Change the title
html = html.replace('<h2>Fragmentos del Universo</h2>', '<h2>Galería de Diseño</h2>');

// 3. Generate the 21 cards
const files = fs.readdirSync(photosDir);
let newGrid = '<div class="pgrid" id="pgrid">\n\n';
let delay = 0;
let faList = ['float-a', 'float-b', 'float-c'];

files.forEach((f, i) => {
    let dur = (Math.random() * 3 + 6).toFixed(1);
    let fa = faList[i % 3];
    newGrid += `      <div class="fw reveal" style="--delay:${delay.toFixed(2)}s;--dur:${dur}s;--fa:${fa}">
        <div class="pcard tilt" data-src="fotos/diseño/${f}">
          <img src="fotos/diseño/${f}" alt="Diseño" loading="lazy">
          <div class="pcard-ov"></div><div class="pcard-shine"></div>
          <div class="pcard-exp"><svg viewBox="0 0 24 24"><polyline points="15,3 21,3 21,9"/><polyline points="9,21 3,21 3,15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg></div>
        </div>
      </div>\n`;
    delay += 0.15;
});
newGrid += '\n    </div>';

// 4. Replace the old grid
const gridStart = html.indexOf('<div class="pgrid" id="pgrid">');
const gridEnd = html.indexOf('</section>', gridStart);
if (gridStart !== -1 && gridEnd !== -1) {
    html = html.substring(0, gridStart) + newGrid + '\n  ' + html.substring(gridEnd);
}

fs.writeFileSync(ugcPath, html, 'utf8');
console.log('Successfully updated ugc.html');
