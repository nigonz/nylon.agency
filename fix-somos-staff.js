const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// The card to replace:
const camilaRegex = /<div class="celestial-card" aria-label="Camila Bazn">[\s\S]*?<\/div>\s*<\/div>/;

const newCards = `
                <div class="celestial-card" aria-label="Matías Molinero">
                    <div class="card-inner">
                        <div class="card-image" style="background-image: url('fotos/Moli.jpg.jpeg');" role="img" aria-label="Foto de Matías Molinero">
                            <div class="card-glare" aria-hidden="true"></div>
                        </div>
                        <div class="card-info">
                            <div class="slide-title">Matías Molinero</div>
                            <div class="slide-name">Drone Pilot · Editor</div>
                        </div>
                    </div>
                </div>

                <div class="celestial-card" aria-label="María Lahoz">
                    <div class="card-inner">
                        <div class="card-image" style="background-image: url('fotos/Maru.jpg.jpeg');" role="img" aria-label="Foto de María Lahoz">
                            <div class="card-glare" aria-hidden="true"></div>
                        </div>
                        <div class="card-info">
                            <div class="slide-title">María Lahoz</div>
                            <div class="slide-name">Fotógrafa</div>
                        </div>
                    </div>
                </div>`;

// Wait, the regex might have encoding issues with "Camila Bazán" vs "Camila Bazn".
// Let's replace by looking for "Camila" to be safe.
const safeCamilaRegex = /<div class="celestial-card" aria-label="Camila[^>]+>[\s\S]*?<div class="slide-title">Camila[^<]+<\/div>[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/;

// Actually let's just use a more explicit string replacement if possible.
// Or just match `<div class="celestial-card" aria-label="Camila` to the end of that specific card.
const camilaTarget = html.match(/<div class="celestial-card" aria-label="Camila[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/);
if (camilaTarget) {
    html = html.replace(camilaTarget[0], newCards);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Successfully replaced Camila with Matías and María.");
} else {
    console.log("Could not find Camila's card to replace.");
}
