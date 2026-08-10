const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Move staff-section from the top to inside screen2
const doctypeIndex = html.indexOf('<!DOCTYPE html>');
if (doctypeIndex > 0) {
    const staffSectionBlock = html.substring(0, doctypeIndex);
    html = html.substring(doctypeIndex);
    
    // Inject it into screen2, right after </nav>
    html = html.replace(/<\/nav>/, '</nav>\n\n    ' + staffSectionBlock.trim());
}

// 2. Remove the old initCardTilt
const tiltStart = html.indexOf('(function initCardTilt() {');
if (tiltStart !== -1) {
    // Need to find the end of the IIFE. It ends right before `whenGSAP(() => {`
    // So let's delete everything from tiltStart to `/* SECUENCIA HERO` (excluding it)
    const tiltEndStr = '/* ═════════════════════════════════════════\n               SECUENCIA HERO';
    let tiltEnd = html.indexOf('/* ═════════════════════════════════════════\r\n               SECUENCIA HERO', tiltStart);
    if (tiltEnd === -1) {
        tiltEnd = html.indexOf('/* ═════════════════════════════════════════\n               SECUENCIA HERO', tiltStart);
    }
    if (tiltEnd !== -1) {
        html = html.substring(0, tiltStart) + html.substring(tiltEnd);
    } else {
        console.warn("Could not find the end of initCardTilt IIFE");
    }
}

// 3. Inject new tilt logic inside whenGSAP(() => { try {
const newLogic = `
                /* ── TILT 3D TARJETAS (desktop only) ── */
                if (!reducedMotion && !IS_TOUCH && window.innerWidth > 600) {
                    const MAX_TILT = 13;
                    const LIFT_Z   = 16;
                    const SHADOW_ON  = '0 32px 64px rgba(0,0,0,0.95), 0 0 36px rgba(245,166,35,0.18), inset 0 0 0 1px rgba(245,166,35,0.22)';
                    const SHADOW_OFF = '0 20px 50px rgba(0,0,0,0.9), inset 0 0 0 1px rgba(245,166,35,0.1)';

                    document.querySelectorAll('.celestial-card').forEach(card => {
                        const inner = card.querySelector('.card-inner');
                        const glare = card.querySelector('.card-glare');

                        card.addEventListener('mousemove', e => {
                            const r  = card.getBoundingClientRect();
                            const nx = ((e.clientX - r.left) / r.width  - 0.5) * 2;
                            const ny = ((e.clientY - r.top)  / r.height - 0.5) * 2;
                            inner.style.transform  = \`rotateX(\${-ny * MAX_TILT}deg) rotateY(\${nx * MAX_TILT}deg) translateZ(\${LIFT_Z}px)\`;
                            inner.style.boxShadow  = SHADOW_ON;
                            if (glare) {
                                glare.style.background = \`radial-gradient(circle at \${((nx+1)/2*100).toFixed(1)}% \${((ny+1)/2*100).toFixed(1)}%, rgba(245,166,35,0.26), transparent 58%)\`;
                                glare.style.opacity    = Math.min(0.85, 0.35 + (Math.abs(nx) + Math.abs(ny)) * 0.22) + '';
                            }
                        });

                        card.addEventListener('mouseleave', () => {
                            inner.style.transform = 'rotateX(0deg) rotateY(0deg) translateZ(0px)';
                            inner.style.boxShadow = SHADOW_OFF;
                            if (glare) { glare.style.opacity = '0'; }
                        });
                    });
                }

                /* ── TOUCH PRESS DEPTH (mobile only) ── */
                if (IS_TOUCH) {
                    document.querySelectorAll('.celestial-card').forEach(card => {
                        const inner = card.querySelector('.card-inner');
                        card.addEventListener('touchstart', () => {
                            inner.style.transition = 'transform 0.12s ease, box-shadow 0.12s ease';
                            inner.style.transform  = 'scale(0.97) translateZ(-6px)';
                            inner.style.boxShadow  = '0 8px 24px rgba(0,0,0,0.95)';
                        }, { passive: true });
                        card.addEventListener('touchend', () => {
                            inner.style.transform = 'scale(1) translateZ(0px)';
                            inner.style.boxShadow = '0 20px 50px rgba(0,0,0,0.9), inset 0 0 0 1px rgba(245,166,35,0.1)';
                        }, { passive: true });
                    });
                }
`;

// Insert just before `} catch (err)` inside whenGSAP
html = html.replace(/} catch \(err\) \{/g, newLogic + '\n                } catch (err) {');

fs.writeFileSync(file, html, 'utf8');
console.log("Fixed HTML stray block and JS timing");
