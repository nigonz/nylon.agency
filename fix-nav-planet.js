const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');
    let changed = false;

    // We only inject if the file contains `<nav id="staff-nav"` or `#staff-nav` in CSS.
    if (content.includes('#staff-nav')) {
        const mobileNavCSS = `
    <style>
        /* Global Mobile Nav Accessibility Fix */
        @media (max-width: 768px) {
            #staff-nav {
                min-height: 70px !important;
            }
            #staff-nav a {
                font-size: 1.1rem !important;
                padding: 12px 15px !important;
            }
        }
    </style>
</head>`;
        
        if (!content.includes('Global Mobile Nav Accessibility Fix')) {
            content = content.replace('</head>', mobileNavCSS);
            changed = true;
        }
    }

    // Step 2: Fix planet label in servicios.html
    if (file === 'servicios.html') {
        if (content.includes("shortName:'PAID MEDIA'")) {
            content = content.replace(/shortName:'PAID MEDIA'/g, "shortName:'DISEÑO GRÁFICO'");
            content = content.replace(/title:'PAID MEDIA'/g, "title:'DISEÑO GRÁFICO'");
            changed = true;
        }
        if (content.includes("shortName: 'PAID MEDIA'")) {
            content = content.replace(/shortName:\s*'PAID MEDIA'/g, "shortName:'DISEÑO GRÁFICO'");
            content = content.replace(/title:\s*'PAID MEDIA'/g, "title:'DISEÑO GRÁFICO'");
            changed = true;
        }
    }

    if (changed) {
        fs.writeFileSync(path.join(dir, file), content, 'utf8');
        console.log("Updated " + file);
    }
});
