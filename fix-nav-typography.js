const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const filesToFix = ['index.html', 'somos.html'];

const oldFontImport = 'href="https://fonts.googleapis.com/css2?family=Righteous&family=Unbounded:wght@300;400;700&display=swap"';
const newFontImport = 'href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Righteous&family=Unbounded:wght@200..900&display=swap"';

const oldNavCSS = /#staff-nav a\s*\{[\s\S]*?text-transform: lowercase;\s*transition: color 0\.3s ease;\s*\}/;
const newNavCSS = `#staff-nav a {
            color: rgba(255,255,255,0.55);
            text-decoration: none;
            font-family: 'Fraunces', serif;
            font-size: 16px; font-weight: 400;
            letter-spacing: 0.5px; text-transform: capitalize;
            transition: color 0.3s ease;
        }`;

filesToFix.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');
    
    // Update font imports
    if (content.includes(oldFontImport)) {
        content = content.replace(oldFontImport, newFontImport);
    } else {
        // If it doesn't have the exact old import, we just replace the Righteous import
        content = content.replace(/href="https:\/\/fonts.googleapis.com\/css2\?family=Righteous[^"]*"/, newFontImport);
    }

    // Update CSS block
    if (oldNavCSS.test(content)) {
        content = content.replace(oldNavCSS, newNavCSS);
    }
    
    fs.writeFileSync(path.join(dir, file), content, 'utf8');
    console.log("Fixed " + file);
});
