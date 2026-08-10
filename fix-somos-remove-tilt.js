const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// Use regex to remove the CARD TILT 3D block
html = html.replace(/\/\* ═════════════════════════════════════════[\s\S]*?\(function initCardTilt\(\) \{[\s\S]*?\}\)\(\);/, '');

fs.writeFileSync(file, html, 'utf8');
console.log("Removed initCardTilt");
