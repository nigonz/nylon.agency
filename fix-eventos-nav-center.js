const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\eventos.html';
let html = fs.readFileSync(file, 'utf8');

const regex = /#staff-nav\s*\{\s*left:\s*auto\s*!important;\s*right:\s*15px\s*!important;\s*transform:\s*none\s*!important;\s*width:\s*auto\s*!important;\s*\}/;

const newCSS = `#staff-nav {
                left: 0 !important;
                right: 0 !important;
                margin-left: auto !important;
                margin-right: auto !important;
                width: fit-content !important;
                transform: none !important;
            }`;

if (regex.test(html)) {
    html = html.replace(regex, newCSS);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Centered nav safely in eventos.html");
} else {
    console.log("Could not find the target CSS block for #staff-nav to center it.");
}
