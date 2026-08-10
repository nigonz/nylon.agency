const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Fix name
html = html.replace(/Matías Molí/g, 'Matías Molinero');
html = html.replace(/Matas Mol/g, 'Matías Molinero');

// 2. Ensure images are hardcoded so they don't depend on JS lazy loading.
// Replace data-bg="fotos/..." with style="background-image: url('fotos/...');"
html = html.replace(/data-bg="([^"]+)"/g, `style="background-image: url('$1');"`);

// 3. To be absolutely safe, let's also remove the lazyLoadImages function since it's no longer needed for staff
html = html.replace(/function lazyLoadImages\(\) {[\s\S]*?lazyLoadImages\(\);/g, '// lazy load removed, images hardcoded for reliability');

// Let's also check for opacity: 0 on .card-image if any.
// In CSS:
// .card-image { filter: grayscale(78%) ... transition: filter ... }
// Nothing hides it.

fs.writeFileSync(file, html, 'utf8');
console.log("Images hardcoded and name fixed.");
