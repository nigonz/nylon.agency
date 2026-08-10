const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const indexHtml = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
const nosotrosHtml = fs.readFileSync(path.join(dir, 'nosotros.html'), 'utf8');

// 1. Extract staff section from current nosotros.html
const staffStart = nosotrosHtml.indexOf('<section class="staff-section" id="menu"');
const staffEnd = nosotrosHtml.indexOf('</section>', staffStart) + 10;
const staffContent = nosotrosHtml.substring(staffStart, staffEnd);

// 2. Inject staff section back into index.html
const injectionPoint = indexHtml.indexOf('</div>\\r\\n\\r\\n    <!-- ══════════════════════════════════════════\\r\\n         PANTALLA 1 — HERO ESPACIAL');
let restoredIndex = indexHtml;
if (injectionPoint !== -1) {
    restoredIndex = indexHtml.substring(0, injectionPoint) + staffContent + '\\r\\n' + indexHtml.substring(injectionPoint);
} else {
    // Fallback if line endings differ
    const fallbackInjection = indexHtml.indexOf('<!-- PANTALLA 1 — HERO ESPACIAL');
    const actualPoint = indexHtml.lastIndexOf('</div>', fallbackInjection);
    restoredIndex = indexHtml.substring(0, actualPoint) + staffContent + '\\r\\n' + indexHtml.substring(actualPoint);
}

// Restore the JS hash check
restoredIndex = restoredIndex.replace("window.location.hash === '#main-video'", "window.location.hash === '#main-video' || window.location.hash === '#menu'");

// 3. Restore nosotros.html from VSCode history
const backupPath = 'C:\\\\Users\\\\Nigonz\\\\AppData\\\\Roaming\\\\Code\\\\User\\\\History\\\\5d44462a\\\\JIEJ.html';
if (fs.existsSync(backupPath)) {
    const backupNosotros = fs.readFileSync(backupPath, 'utf8');
    fs.writeFileSync(path.join(dir, 'nosotros.html'), backupNosotros, 'utf8');
    console.log("Restored nosotros.html from backup.");
}

// Restore index.html
fs.writeFileSync(path.join(dir, 'index.html'), restoredIndex, 'utf8');
console.log("Restored index.html.");
