const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const indexHtml = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');

// The section to move is <section class="staff-section" id="menu" ...> to </section>
const staffStart = indexHtml.indexOf('<section class="staff-section" id="menu"');
const staffEnd = indexHtml.indexOf('</section>', staffStart) + 10;
const staffContent = indexHtml.substring(staffStart, staffEnd);

// 1. Update index.html
let newIndex = indexHtml.substring(0, staffStart) + indexHtml.substring(staffEnd);
// Also remove the hash jump for '#menu' in JS since it's no longer there
newIndex = newIndex.replace("window.location.hash === '#main-video' || window.location.hash === '#menu'", "window.location.hash === '#main-video'");

fs.writeFileSync(path.join(dir, 'index.html'), newIndex, 'utf8');

// 2. Create nosotros.html
// nosotros.html should have the head, the nav, the background particles, and the staffContent.
// The easiest way is to copy index.html, remove main-video, and remove the hero section so it directly shows the staffContent.
// BUT index.html has a complex SPA JS that hides screen2 until landing is triggered.
// If nosotros.html is a separate page, we don't want the landing transition. We want screen2 visible immediately.
let nosotros = indexHtml.replace(/<section id="main-video"[\s\S]*?<\/section>/, ''); // remove main-video
nosotros = nosotros.replace(/<section class="hero" id="hero"[\s\S]*?<\/section>/, ''); // remove hero
// Make screen2 visible by default and allow scrolling
nosotros = nosotros.replace('<style>', `<style>
        #screen2 { opacity: 1 !important; pointer-events: auto !important; position: relative !important; z-index: 10 !important; }
        body { background: var(--bg); overflow-y: scroll !important; }
        #transitionOverlay { display: none !important; }
`);
// Remove the landing JS logic to avoid errors since hero/video don't exist
nosotros = nosotros.replace(/<script>[\s\S]*?<\/script>/g, (match) => {
    if (match.includes('whenGSAP')) {
        // Keep a simple version or remove it entirely if GSAP isn't needed for the staff grid
        // The staff cards might use basic CSS hover. Let's just remove the complex intro JS and keep basic GSAP init if needed.
        return `<script>
        (function () {
            "use strict";
            // Minimal JS for nosotros.html
        })();
        </script>`;
    }
    return match;
});

// Write nosotros.html
fs.writeFileSync(path.join(dir, 'nosotros.html'), nosotros, 'utf8');

// 3. Update links globally
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(f => {
    let content = fs.readFileSync(path.join(dir, f), 'utf8');
    
    // Replace href="index.html#main-video" or href="#main-video" or href="#menu" or href="index.html#menu" 
    // with href="index.html" for Inicio
    content = content.replace(/href="[^"]*#(main-video|hero|menu)"/g, (match, p1) => {
        if (p1 === 'menu') return 'href="nosotros.html"';
        return 'href="index.html"';
    });

    // Replace specific texts:
    content = content.replace(/<a[^>]*href="[^"]*"[^>]*>Inicio<\/a>/g, (match) => {
        return match.replace(/href="[^"]*"/, 'href="index.html"');
    });

    content = content.replace(/<a[^>]*href="[^"]*"[^>]*>Nosotros<\/a>/g, (match) => {
        return match.replace(/href="[^"]*"/, 'href="nosotros.html"');
    });

    fs.writeFileSync(path.join(dir, f), content, 'utf8');
});

console.log("Refactoring complete.");
