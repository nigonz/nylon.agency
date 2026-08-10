const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// Replace the `});` at the end of the IIFE with `})();`
// It's followed by /* SECUENCIA HERO
html = html.replace(/\}\);\s*\/\* \s*SECUENCIA HERO/g, `})();\n            /* \n               SECUENCIA HERO`);

fs.writeFileSync(file, html, 'utf8');
console.log("Fixed IIFE syntax error");
