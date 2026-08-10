const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

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
`;

// Insert the JS before `whenGSAP(() => {`
html = html.replace('            whenGSAP(() => {', newJs + '\n            whenGSAP(() => {');

fs.writeFileSync(file, html, 'utf8');
console.log("Injected JS perfectly.");
