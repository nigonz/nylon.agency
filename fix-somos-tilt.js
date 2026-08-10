const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

const newTiltLogic = `
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

// Also, the previous `try-catch` wrapper for whenGSAP is missing because I rebuilt from index.html without it!
// But `index.html` actually runs fine without `try-catch` if `main-video` doesn't exist?
// No, `bgVideo.currentTime = 0;` will crash if `bgVideo` is missing!
// But wait, my `rebuild-somos.js` DOES add `const bgVideo = { play: ()=>Promise.resolve(), pause: ()=>{} }; // mocked` ?
// No, `execute-architecture.js` did that manually but wait! `execute-architecture.js` DID NOT add `const bgVideo = ...`, it was added in `fix-somos-js.js`!
// So let's re-apply the `fix-somos-js.js` fixes as well right now:
// 1. Mock the missing elements
const mockElements = `
                // Mocks for missing index.html elements in somos.html
                const overlay = document.getElementById('transitionOverlay') || document.createElement('div');
                const screen2 = document.getElementById('screen2') || document.createElement('div');
                const btn = document.getElementById('spaceBtn') || document.createElement('div');
                const backBtn = document.getElementById('backBtn') || document.createElement('div');
                const bgVideo = document.getElementById('bgVideo') || { play: ()=>Promise.resolve(), pause: ()=>{}, currentTime: 0 };
                const logo = document.createElement('div');
                const logoImg = document.createElement('img');
                const scrollHint = document.createElement('div');
                const wordIds = [];
`;
html = html.replace(/const overlay = document\.getElementById\('transitionOverlay'\);[\s\S]*?const wordIds = \['w_experiencia', 'w_tactica', 'w_visual'\];/, mockElements);

// 2. Inject the new tilt logic right before `}); // end whenGSAP`
html = html.replace(/\}\);\s*\/\/\s*end whenGSAP/, newTiltLogic + '\n            }); // end whenGSAP');

fs.writeFileSync(file, html, 'utf8');
console.log("Injected tilt logic and JS fixes to somos.html");
