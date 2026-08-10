const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\holo.html';
let html = fs.readFileSync(file, 'utf8');

const oldExceptions = /<style>\s*\/\* Holo Specific Exceptions \*\/[\s\S]*?<\/style>/;
const newExceptions = `<style>
        /* Holo Specific Exceptions */
        @media (min-width: 769px) {
            #staff-nav {
                left: auto !important;
                right: 40px !important;
                transform: none !important;
                width: auto !important;
            }
            .nav-logo {
                position: fixed !important;
                top: 30px !important;
                left: 40px !important;
            }
            header {
                margin-top: 12vh !important;
            }
            main.gallery-track {
                padding-top: 0 !important;
                margin-top: -2vh !important;
                gap: 50px !important;
            }
        }
        
        #staff-nav {
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            border: none !important;
            box-shadow: none !important;
        }
    </style>`;

if (oldExceptions.test(html)) {
    html = html.replace(oldExceptions, newExceptions);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Updated Holo exceptions with fine-tuned PC positioning.");
} else {
    console.log("Could not find Holo Specific Exceptions block.");
}
