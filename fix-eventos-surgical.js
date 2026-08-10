const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const eventosPath = path.join(dir, 'eventos.html');
let eventosHtml = fs.readFileSync(eventosPath, 'utf8');

// 1. Remove stray text
eventosHtml = eventosHtml.replace(/<div class="hud-logo">.*?<\/div>/g, '');

// 2. Fix the background image scaling and gap
const oldExceptions = /<style>\s*\/\* Eventos Specific Exceptions \*\/[\s\S]*?<\/style>/;
const newExceptions = `<style>
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
            top: 0 !important;
        }
        .hero-bg {
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
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

if (oldExceptions.test(eventosHtml)) {
    eventosHtml = eventosHtml.replace(oldExceptions, newExceptions);
    fs.writeFileSync(eventosPath, eventosHtml, 'utf8');
    console.log("Applied surgical layout fix to eventos.html.");
} else {
    console.log("Could not find Eventos Specific Exceptions block.");
}
