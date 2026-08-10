const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');
    let changed = false;

    // 1. Update the global layout block
    const oldFixRegex = /<style>\s*\/\* Global Mobile Nav Accessibility Fix \*\/[\s\S]*?<\/style>\s*<\/head>/g;
    
    const newFix = `<style>
        /* Global Mobile Nav Accessibility Fix */
        @media (max-width: 768px) {
            #staff-nav {
                min-height: 60px !important;
                padding: 10px 12px !important;
            }
            .nav-links {
                display: flex !important;
                flex-wrap: nowrap !important;
                gap: 8px !important;
                justify-content: center !important;
                width: 100%;
            }
            #staff-nav a {
                font-size: 0.85rem !important;
                padding: 8px 4px !important;
                white-space: nowrap !important;
                text-align: center;
            }
        }

        /* Global Top Clearance for Fixed Nav (Desktop & Mobile) */
        .staff-section,
        .agency-description,
        .portfolio-grid,
        .portfolio-mobile-grid,
        .ugc-section,
        .brand-section,
        .comercial-section,
        .eventos-section,
        .contacto-section,
        main {
            padding-top: 100px !important;
            margin-top: 0 !important;
        }
    </style>
</head>`;

    if (oldFixRegex.test(content)) {
        content = content.replace(oldFixRegex, newFix);
        changed = true;
    }

    // 2. Specific fix for portfolio.html 3D viewport
    if (file === 'portfolio.html') {
        const viewportRegex = /\.viewport\s*\{[\s\S]*?pointer-events:\s*none;\s*\}/;
        if (viewportRegex.test(content)) {
            const newViewport = `.viewport {
            position: fixed; top: 90px; left: 0;
            width: 100vw; height: calc(100vh - 90px);
            perspective: 800px; overflow: hidden; 
            z-index: 10;
            pointer-events: none;
        }`;
            content = content.replace(viewportRegex, newViewport);
            changed = true;
        }
    }

    if (changed) {
        fs.writeFileSync(path.join(dir, file), content, 'utf8');
        console.log("Applied project layout fixes to " + file);
    }
});
