const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\eventos.html';
let html = fs.readFileSync(file, 'utf8');

const regex = /<style>\s*\/\* Eventos Specific Exceptions \*\/[\s\S]*?<\/style>/;
const newCSS = `<style>
        /* Eventos Specific Exceptions */
        @media (min-width: 769px) {
            #staff-nav {
                left: auto !important;
                right: 15px !important;
                transform: none !important; /* DO NOT USE SCALE, IT BREAKS FIXED POSITIONING OF CHILDREN */
                width: auto !important;
            }
            .nav-logo {
                position: fixed !important;
                top: 25px !important;
                left: 30px !important; /* Esquina izquierda absoluta */
                z-index: 9999 !important;
            }
        }

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
            position: fixed !important; 
            top: 0 !important; 
            left: 0 !important;
            width: 100vw !important;
            height: 120vh !important; /* Más altura */
            margin: 0 !important;
            padding: 0 !important;
            z-index: -1 !important; 
        }
        
        .hero-img {
            object-fit: cover !important;
            object-position: center top !important; /* Asegurar que no se corte la cabeza */
            width: 100vw !important;
            height: 120vh !important; /* Más altura */
            transform: none !important; 
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
    console.log("Fixed NYLON logo position and increased image height.");
} else {
    console.log("Could not find Eventos Specific Exceptions block.");
}
