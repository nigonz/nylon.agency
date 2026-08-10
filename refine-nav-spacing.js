const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), 'utf8');
    let changed = false;

    // 1. Update the global layout block I injected in the previous step
    // We want to replace `margin-top: 130px !important;` with `padding-top: 100px !important; margin-top: 0 !important;`
    if (content.includes('margin-top: 130px !important;')) {
        content = content.replace(/margin-top:\s*130px\s*!important;/g, 'padding-top: 100px !important;\n                margin-top: 0 !important;');
        changed = true;
    }

    // 2. Slim down the desktop #staff-nav
    // Find `#staff-nav { ... padding: 14px 28px; ... }` and change to `padding: 10px 30px !important; min-height: 60px;`
    // Wait, the user example says `padding: 15px 30px !important;`.
    const navPaddingRegex = /padding:\s*14px 28px;/;
    if (navPaddingRegex.test(content)) {
        content = content.replace(navPaddingRegex, 'padding: 15px 30px !important;\n            min-height: 60px;');
        changed = true;
    }

    // 3. Fix the massive gap on somos.html specific mobile media query
    if (file === 'somos.html' || content.includes('margin-top: 100px !important;')) {
        const agencyDescRegex = /\.agency-description\s*\{\s*margin-top:\s*100px\s*!important;\s*\}/g;
        if (agencyDescRegex.test(content)) {
            content = content.replace(agencyDescRegex, '');
            changed = true;
        }
    }

    if (changed) {
        fs.writeFileSync(path.join(dir, file), content, 'utf8');
        console.log("Applied refinement to " + file);
    }
});
