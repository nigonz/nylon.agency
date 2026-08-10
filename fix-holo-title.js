const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\holo.html';
let html = fs.readFileSync(file, 'utf8');

const regex = /margin-top:\s*12vh\s*!important;/;
const replacement = 'margin-top: 6vh !important;';

if (regex.test(html)) {
    html = html.replace(regex, replacement);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Updated Holo header margin.");
} else {
    console.log("Could not find the 12vh margin-top in header.");
}
