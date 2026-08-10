const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\holo.html';
let html = fs.readFileSync(file, 'utf8');

const regex = /right:\s*40px\s*!important;/;
const replacement = 'right: 15px !important;\n                transform: scale(0.9) !important; /* Achicar sutilmente */\n                transform-origin: right top !important;';

if (regex.test(html)) {
    html = html.replace(regex, replacement);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Updated Holo nav position to the right and slightly smaller.");
} else {
    console.log("Could not find the target CSS block for right: 40px.");
}
