const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// Remove the DOMContentLoaded wrapper to ensure it runs immediately
html = html.replace(/document\.addEventListener\("DOMContentLoaded", \(\) => \{/g, `(function() {`);
html = html.replace(/\}\);\s*\/\* \s*SECUENCIA HERO/g, `})();
            /* 
               SECUENCIA HERO`);

fs.writeFileSync(file, html, 'utf8');
console.log("Removed DOMContentLoaded wrapper to ensure execution");
