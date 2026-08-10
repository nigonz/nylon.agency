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
                transform: none !important;
                width: auto !important;
            }
            .nav-logo {
                position: fixed !important;
                top: 25px !important;
                left: 30px !important;
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
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            z-index: -1 !important; 
        }
        
        .hero-img {
            object-fit: cover !important;
            object-position: center center !important; 
            width: 100vw !important;
            height: 100vh !important;
            transform: none !important; 
            margin: 0 !important;
            padding: 0 !important;
            display: block !important;
        }
        
        /* THE REAL FIX FOR THE SPLIT LAYOUT GAP */
        .hero-split-layout {
            padding-top: 0 !important; /* DO NOT push the whole layout down */
            margin-top: 0 !important;
            height: 100vh !important;
        }
        
        .split-text {
            padding-top: 150px !important; /* ONLY push the text container down */
        }
        
        .split-image {
            margin-top: 0 !important; /* Force to absolute top */
            padding-top: 0 !important;
            height: 100vh !important; /* Full browser height */
        }
        
        .split-image img {
            height: 100% !important;
            object-fit: cover !important;
            object-position: center top !important; /* Ensure head is not cut off */
        }
    </style>`;

if (regex.test(html)) {
    html = html.replace(regex, newCSS);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Successfully targeted the right-side split image and text container independently.");
} else {
    console.log("Could not find Eventos Specific Exceptions block.");
}
