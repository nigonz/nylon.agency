const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\eventos.html';
let html = fs.readFileSync(file, 'utf8');

const regex = /<style>\s*\/\* Eventos Specific Exceptions \*\/[\s\S]*?<\/style>/;
const newCSS = `<style>
        /* Eventos Specific Exceptions */
        .transparent-nav-page #staff-nav {
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            box-shadow: none !important;
            border-bottom: none !important;
        }
        .transparent-nav-page .nav-logo {
            position: fixed !important;
            top: 30px !important;
            left: 20px !important;
            z-index: 1000 !important;
        }
        main, .hero {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        .hero-bg {
            position: fixed !important; 
            top: -5vh !important; 
            left: -5vw !important;
            width: 110vw !important;
            height: 110vh !important;
            margin: 0 !important;
            padding: 0 !important;
            z-index: -1 !important; 
        }
        .hero-img {
            object-fit: cover !important;
            object-position: center 5% !important; /* Shift focus slightly down from absolute top */
            width: 110vw !important;
            height: 110vh !important;
            transform: scale(1.15) !important; 
            transform-origin: top center !important;
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

if (regex.test(html)) {
    html = html.replace(regex, newCSS);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Applied overcompensated background fix and moved nav-logo.");
} else {
    console.log("Could not find Eventos Specific Exceptions block.");
}
