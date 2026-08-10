const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';
const backupPath = 'C:\\\\Users\\\\Nigonz\\\\AppData\\\\Roaming\\\\Code\\\\User\\\\History\\\\-35832ae9\\\\7IFA.html';
const indexHtmlPath = path.join(dir, 'index.html');
const somosHtmlPath = path.join(dir, 'somos.html');

let indexHtml = fs.readFileSync(indexHtmlPath, 'utf8');
let backupHtml = fs.readFileSync(backupPath, 'utf8');

// 1. Extract staff-section from backup
const staffStart = backupHtml.indexOf('<section class="staff-section" id="menu"');
const staffEnd = backupHtml.indexOf('</section>', staffStart) + 10;
let staffContent = backupHtml.substring(staffStart, staffEnd);

// Fix images and names in staffContent
staffContent = staffContent.replace(/class="card-image"\s+data-bg="([^"]+)"/g, 'class="card-image" style="background-image: url(\'$1\');"');
staffContent = staffContent.replace(/Matías Molí/g, 'Matías Molinero');
staffContent = staffContent.replace(/class="card-image lazy-bg"\s+data-bg="([^"]+)"/g, 'class="card-image" style="background-image: url(\'$1\');"'); // Just in case it has lazy-bg class

// 2. Build somosHtml from indexHtml
let somosHtml = indexHtml;

// Remove hero section
somosHtml = somosHtml.replace(/<section class="hero" id="hero"[\s\S]*?<\/section>/, '');
// Remove main-video section
somosHtml = somosHtml.replace(/<section id="main-video"[\s\S]*?<\/section>/, '');

// Clean JS btn listeners
somosHtml = somosHtml.replace(/btn\.addEventListener\('click', launchLanding\);/g, '// btn listener removed');
somosHtml = somosHtml.replace(/btn\.addEventListener\('touchend',[\s\S]*?\}\);/g, '// btn touch listener removed');

// Remove old initTilt completely!
somosHtml = somosHtml.replace(/function initTilt\(\) \{[\s\S]*?initTilt\(\);/, '');

// 3. Inject staffContent into screen2
somosHtml = somosHtml.replace(/<\/nav>/, '</nav>\n\n    ' + staffContent);

// 4. Inject styles for screen2 and tilt transitions
const styles = `
    <style>
        #screen2 { opacity: 1 !important; pointer-events: auto !important; position: relative !important; z-index: 10 !important; }
        body { background: var(--bg); overflow-y: scroll !important; }
        #transitionOverlay { display: none !important; }

        .celestial-card {
            transition: transform 0.08s linear;
            will-change: transform;
        }

        .celestial-card .card-inner {
            transition: transform 0.08s linear, box-shadow 0.3s ease;
        }
    </style>
</head>`;
somosHtml = somosHtml.replace('</head>', styles);

// 5. Inject new desktop and mobile tilt logic inside whenGSAP try block
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

// Insert the tilt logic right before `} catch (err)`
somosHtml = somosHtml.replace(/\} catch \(err\) \{/, newTiltLogic + '\n                } catch (err) {');

fs.writeFileSync(somosHtmlPath, somosHtml, 'utf8');
console.log("Successfully rebuilt somos.html from backup index with new tilt logic!");
