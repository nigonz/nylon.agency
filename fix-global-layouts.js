const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');
    let changed = false;

    // 1. Remove the old Global Mobile Nav Accessibility Fix so we can replace it cleanly
    const oldFixRegex = /<style>\s*\/\* Global Mobile Nav Accessibility Fix \*\/[\s\S]*?<\/style>/g;
    if (oldFixRegex.test(content)) {
        content = content.replace(oldFixRegex, '');
    }

    // 2. Inject the comprehensive fix right before </head>
    const comprehensiveFix = `
    <style>
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

        /* Global Desktop Top Clearance for Fixed Nav */
        @media (min-width: 769px) {
            .staff-section,
            .agency-description,
            .portfolio-grid,
            .portfolio-mobile-grid,
            .ugc-section,
            .brand-section,
            .comercial-section,
            .eventos-section,
            .contacto-section {
                margin-top: 130px !important;
            }
        }
    </style>
</head>`;

    if (content.includes('</head>')) {
        content = content.replace('</head>', comprehensiveFix);
        changed = true;
    }

    if (changed) {
        fs.writeFileSync(path.join(dir, file), content, 'utf8');
        console.log("Applied layout fixes to " + file);
    }
});
