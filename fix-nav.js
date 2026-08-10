const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let indexFixed = false;
let othersFixed = 0;

for (const file of files) {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    if (file === 'index.html') {
        // Remove <a href="...">Inicio</a> from index.html inside the nav-links div
        // A simple string replace or regex
        const navRegex = /(<div class="nav-links">\s*)<a[^>]*>Inicio<\/a>\s*/;
        if (navRegex.test(content)) {
            content = content.replace(navRegex, '$1');
            fs.writeFileSync(filePath, content, 'utf8');
            indexFixed = true;
            console.log(`Updated index.html: Removed "Inicio" link`);
        }
    } else {
        // For other files, replace <a href="...">Inicio</a> with <a href="index.html#main-video">Inicio</a>
        // We only want to target the Inicio link, which might be in the nav. 
        // We look for any <a href="...">Inicio</a>
        const inicioRegex = /<a\s+href="[^"]*"\s*>Inicio<\/a>/g;
        if (inicioRegex.test(content)) {
            content = content.replace(inicioRegex, '<a href="index.html#main-video">Inicio</a>');
            fs.writeFileSync(filePath, content, 'utf8');
            othersFixed++;
            console.log(`Updated ${file}: Changed "Inicio" link to hash`);
        }
    }
}

console.log(`Done. index.html fixed: ${indexFixed}, other files fixed: ${othersFixed}`);
