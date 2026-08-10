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
            header {
                margin-top: 15vh !important;
            }
            main.gallery-track {
                padding-top: 60px !important;
                margin-top: 0 !important;
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
    console.log("Updated Holo exceptions.");
} else {
    console.log("Could not find Holo Specific Exceptions block.");
}
