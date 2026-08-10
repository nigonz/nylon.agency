const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\holo.html';
let html = fs.readFileSync(file, 'utf8');

const regex = /header\s*\{\s*margin-top:\s*6vh\s*!important;\s*\}\s*main\.gallery-track\s*\{\s*padding-top:\s*0\s*!important;\s*margin-top:\s*-2vh\s*!important;/;

const replacement = `header {
                margin-top: 3vh !important;
            }
            main.gallery-track {
                padding-top: 4vh !important;
                margin-top: 0 !important;`;

if (regex.test(html)) {
    html = html.replace(regex, replacement);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Updated Holo precise layout tweaks.");
} else {
    console.log("Could not find the target CSS block.");
}
