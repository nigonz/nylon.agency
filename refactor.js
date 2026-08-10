const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const indexHtml = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');

// 1. Extract contentWrap from index.html
const contentWrapStart = indexHtml.indexOf('<div id="contentWrap"');
let contentWrapEnd = -1;
if (contentWrapStart !== -1) {
    // Find the matching closing div for contentWrap
    const sectionHeroStart = indexHtml.indexOf('<!-- ══════════════════════════════════════════\\r\\n         PANTALLA 1 — HERO ESPACIAL', contentWrapStart);
    if (sectionHeroStart === -1) {
        // Fallback
        const h2 = indexHtml.indexOf('<!-- PANTALLA 1');
        contentWrapEnd = indexHtml.lastIndexOf('</div>', h2 !== -1 ? h2 : indexHtml.length);
    } else {
        contentWrapEnd = indexHtml.lastIndexOf('</div>', sectionHeroStart) + 6;
    }
}

if (contentWrapStart === -1 || contentWrapEnd === -1) {
    console.error("Could not find contentWrap");
    process.exit(1);
}

const contentWrap = indexHtml.substring(contentWrapStart, contentWrapEnd);

// 2. Create nosotros.html
// nosotros.html is index.html but with hero removed, and contentWrap kept
let nosotrosHtml = indexHtml;
const heroStart = nosotrosHtml.indexOf('<section class="hero" id="hero"');
const scriptStart = nosotrosHtml.indexOf('<script>', heroStart);
if (heroStart !== -1 && scriptStart !== -1) {
    // We want to remove the hero section and maybe the starfield init script, but the prompt says:
    // "remove the hero section from nosotros.html"
    // Wait, the prompt exactly says: "move the text paragraph... into the <main> or body... of the newly created nosotros.html... Verify that index.html now only contains the full-screen fixed background video section and the global navigation bar."
    // For nosotros.html: "Copy the entire global structure from index.html ... so it retains the exact same <head>, the identical floating navigation header/bar (#staff-nav), the background particles div, and the general body styling. Paste them into the <main> or body content area of the newly created nosotros.html"
    // The hero section *is* the full-screen background video section. So we delete hero from nosotros.html.
    const heroEnd = nosotrosHtml.indexOf('</section>', heroStart) + 10;
    nosotrosHtml = nosotrosHtml.substring(0, heroStart) + nosotrosHtml.substring(heroEnd);
}

// 3. Modify index.html
// index.html should keep hero but remove contentWrap
let newIndexHtml = indexHtml.substring(0, contentWrapStart) + indexHtml.substring(contentWrapEnd);

fs.writeFileSync(path.join(dir, 'nosotros.html'), nosotrosHtml, 'utf8');
fs.writeFileSync(path.join(dir, 'index.html'), newIndexHtml, 'utf8');

// 4. Update navigation links in all HTML files
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(f => {
    let content = fs.readFileSync(path.join(dir, f), 'utf8');
    
    // Update Inicio link
    content = content.replace(/<a[^>]*href="[^"]*"[^>]*>Inicio<\/a>/g, (match) => {
        // preserve class/style if any, but replace href
        return match.replace(/href="[^"]*"/, 'href="index.html"');
    });

    // Update Nosotros link
    content = content.replace(/<a[^>]*href="[^"]*"[^>]*>Nosotros<\/a>/g, (match) => {
        return match.replace(/href="[^"]*"/, 'href="nosotros.html"');
    });

    fs.writeFileSync(path.join(dir, f), content, 'utf8');
});

console.log("Refactoring complete.");
