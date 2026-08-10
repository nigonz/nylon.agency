const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';

// Fix eventos.html
const eventosPath = path.join(dir, 'eventos.html');
let eventosHtml = fs.readFileSync(eventosPath, 'utf8');

// 1. Completely delete the HUD nav block that contains the stray text
eventosHtml = eventosHtml.replace(/<nav class="hud">[\s\S]*?<\/nav>/g, '');
// Also catch the specific stray string if it was left behind
eventosHtml = eventosHtml.replace(/NYLON · WORKS<\/div>/g, '');

// 2. Fix the background image CSS
const oldEventosExceptions = /<style>\s*\/\* Eventos Specific Exceptions \*\/[\s\S]*?<\/style>/;
const newEventosExceptions = `<style>
        /* Eventos Specific Exceptions */
        .transparent-nav-page #staff-nav {
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            box-shadow: none !important;
            border-bottom: none !important;
        }
        main, .hero {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        .hero-bg {
            position: fixed !important; /* Force viewport anchoring */
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            z-index: -1 !important; /* Ensure it stays behind text */
        }
        .hero-img {
            object-fit: cover !important;
            object-position: center top !important;
            width: 100vw !important;
            height: 100vh !important;
            transform: scale(1) !important;
            margin: 0 !important;
            padding: 0 !important;
            display: block !important;
        }
        .hero-split-layout {
            padding-top: 140px !important;
            position: relative;
            z-index: 10;
            margin-top: 0 !important;
        }
    </style>`;

if (oldEventosExceptions.test(eventosHtml)) {
    eventosHtml = eventosHtml.replace(oldEventosExceptions, newEventosExceptions);
}
fs.writeFileSync(eventosPath, eventosHtml, 'utf8');
console.log("Fixed eventos.html background and deleted stray text.");

// Fix holo.html (Ensure no HUD block there either)
const holoPath = path.join(dir, 'holo.html');
let holoHtml = fs.readFileSync(holoPath, 'utf8');
holoHtml = holoHtml.replace(/<nav class="hud">[\s\S]*?<\/nav>/g, '');
fs.writeFileSync(holoPath, holoHtml, 'utf8');
console.log("Fixed holo.html stray text.");
