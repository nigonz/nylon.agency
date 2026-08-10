const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';

// 1. File Renames
const renameMap = {
    'nosotros.html': 'servicios.html',
    'slicer.html': 'portfolio.html',
    'slicer_mobile.html': 'portfolio_mobile.html'
};

for (const [oldName, newName] of Object.entries(renameMap)) {
    const oldPath = path.join(dir, oldName);
    const newPath = path.join(dir, newName);
    if (fs.existsSync(oldPath)) {
        fs.renameSync(oldPath, newPath);
    }
}

// 2. Update redirect in portfolio.html
const portfolioPath = path.join(dir, 'portfolio.html');
if (fs.existsSync(portfolioPath)) {
    let pf = fs.readFileSync(portfolioPath, 'utf8');
    pf = pf.replace(/slicer_mobile\.html/g, 'portfolio_mobile.html');
    fs.writeFileSync(portfolioPath, pf, 'utf8');
}

// 3. Build somos.html and clean index.html
const indexHtmlPath = path.join(dir, 'index.html');
const indexHtml = fs.readFileSync(indexHtmlPath, 'utf8');

// Build somos.html (start with index.html)
let somosHtml = indexHtml;
// Remove hero section
somosHtml = somosHtml.replace(/<section class="hero" id="hero"[\s\S]*?<\/section>/, '');
// Remove main-video section
somosHtml = somosHtml.replace(/<section id="main-video"[\s\S]*?<\/section>/, '');
// Add styles to make screen2 visible unconditionally and disable transition overlay
somosHtml = somosHtml.replace('</head>', `
    <style>
        #screen2 { opacity: 1 !important; pointer-events: auto !important; position: relative !important; z-index: 10 !important; }
        body { background: var(--bg); overflow-y: scroll !important; }
        #transitionOverlay { display: none !important; }
    </style>
</head>`);
// Clean JS that might fail without hero/video
somosHtml = somosHtml.replace(/btn\.addEventListener\('click', launchLanding\);/g, '// btn listener removed');
somosHtml = somosHtml.replace(/btn\.addEventListener\('touchend',[\s\S]*?}\);/g, '// btn touch listener removed');

fs.writeFileSync(path.join(dir, 'somos.html'), somosHtml, 'utf8');

// Clean index.html
let cleanIndexHtml = indexHtml;
// Remove staff-section
cleanIndexHtml = cleanIndexHtml.replace(/<section class="staff-section" id="menu"[\s\S]*?<\/section>/, '');
fs.writeFileSync(indexHtmlPath, cleanIndexHtml, 'utf8');

// 4. Global Navigation Update
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
const newNavHTML = `            <div class="nav-links">
                <a href="index.html">Inicio</a>
                <a href="somos.html">Somos</a>
                <a href="servicios.html">Servicios</a>
                <a href="portfolio.html">Portfolio</a>
            </div>`;

files.forEach(f => {
    let content = fs.readFileSync(path.join(dir, f), 'utf8');
    
    // Replace the entire <div class="nav-links"> block safely
    content = content.replace(/<div class="nav-links">[\s\S]*?<\/div>/, newNavHTML);
    
    fs.writeFileSync(path.join(dir, f), content, 'utf8');
});

console.log("Architecture updated successfully.");
