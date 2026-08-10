const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// 1. Replace the CSS block for .celestial-card
html = html.replace(/\.celestial-card \{[\s\S]*?\}/, `.celestial-card {
            /* Ancho responsivo: nunca más ancho que la pantalla */
            width: clamp(220px, 28vw, 300px);
            height: clamp(340px, 42vw, 460px);
            position: relative;
            transform-style: preserve-3d;
            cursor: crosshair;
            flex-shrink: 0;
            transition: transform 0.08s linear;
            will-change: transform;
        }`);

// 2. Replace the CSS block for .card-inner
html = html.replace(/\.card-inner \{[\s\S]*?\}/, `.card-inner {
            width: 100%;
            height: 100%;
            position: relative;
            background: rgba(10, 5, 0, 0.82);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9), inset 0 0 0 1px rgba(245, 166, 35, 0.1);
            transform-style: preserve-3d;
            transition: transform 0.08s linear, box-shadow 0.3s ease;
        }`);

// 3. Remove my old JS block
const oldJsRegex = /\(function\(\) \{\s*\/\/ Only run 3D effects[\s\S]*?\}\)\(\);/;
html = html.replace(oldJsRegex, '');

// 4. Inject the new JS block exactly before /* SECUENCIA HERO + TRANSICIÓN
const newJs = `
            /* ═════════════════════════════════════════
               CARD TILT 3D
            ═════════════════════════════════════════ */
            (function initCardTilt() {
                // Skip on mobile/touch — already handled by the existing @media (max-width: 600px) CSS
                const IS_TOUCH_LOCAL = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
                if (IS_TOUCH_LOCAL || window.innerWidth <= 600) return;

                const MAX_TILT = 14;        // degrees, max rotation on each axis
                const GLARE_STRENGTH = 0.38; // opacity multiplier for .card-glare
                const LIFT_Z = 18;           // translateZ on hover (px)
                const SHADOW_HOVER = '0 32px 64px rgba(0,0,0,0.95), 0 0 40px rgba(245,166,35,0.18), inset 0 0 0 1px rgba(245,166,35,0.22)';
                const SHADOW_REST  = '0 20px 50px rgba(0,0,0,0.9), inset 0 0 0 1px rgba(245,166,35,0.1)';

                document.querySelectorAll('.celestial-card').forEach(card => {
                    const inner = card.querySelector('.card-inner');
                    const glare = card.querySelector('.card-glare');

                    card.addEventListener('mousemove', e => {
                        const rect = card.getBoundingClientRect();
                        // Normalized position: -1 to +1 relative to card center
                        const nx = ((e.clientX - rect.left) / rect.width  - 0.5) * 2;
                        const ny = ((e.clientY - rect.top)  / rect.height - 0.5) * 2;

                        const rotY =  nx * MAX_TILT;   // lean left/right
                        const rotX = -ny * MAX_TILT;   // lean up/down

                        inner.style.transform = \`rotateX(\${rotX}deg) rotateY(\${rotY}deg) translateZ(\${LIFT_Z}px)\`;
                        inner.style.boxShadow = SHADOW_HOVER;

                        // Move glare highlight following the cursor
                        if (glare) {
                            const gx = ((nx + 1) / 2 * 100).toFixed(1);
                            const gy = ((ny + 1) / 2 * 100).toFixed(1);
                            glare.style.background = \`radial-gradient(circle at \${gx}% \${gy}%, rgba(245,166,35,0.28), transparent 58%)\`;
                            glare.style.opacity = (0.4 + Math.abs(nx) * 0.3 + Math.abs(ny) * 0.3) * GLARE_STRENGTH * 2.5 + '';
                        }
                    });

                    card.addEventListener('mouseleave', () => {
                        inner.style.transform = 'rotateX(0deg) rotateY(0deg) translateZ(0px)';
                        inner.style.boxShadow = SHADOW_REST;
                        if (glare) {
                            glare.style.opacity = '0';
                            glare.style.background = 'radial-gradient(circle at 50% 50%, rgba(245,166,35,0.2), transparent 60%)';
                        }
                    });
                });
            })();
            
            /* `;

html = html.replace(/\/\* \s*SECUENCIA HERO \+ TRANSICIÓN/, newJs + `SECUENCIA HERO + TRANSICIÓN`);

// In case the word "TRANSICIÓN" is messed up with encoding, let's just match "SECUENCIA HERO"
html = html.replace(/\/\* \s*SECUENCIA HERO/g, newJs + `SECUENCIA HERO`);

fs.writeFileSync(file, html, 'utf8');
console.log("Applied new tilt logic and CSS");
