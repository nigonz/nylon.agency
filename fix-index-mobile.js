const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\index.html';
let html = fs.readFileSync(file, 'utf8');

// Fix 1: Remove stray \r\n at the beginning of the file
html = html.replace(/^\\r\\n/, '');

// Fix 2: Speed up mobile intro sequence
const oldSequence = `
                    /* Aparición de cada palabra */
                    let cursor = 0.9;
                    wordIds.forEach(id => {
                        const el = document.getElementById(id);
                        master.set(el, { scale: 0.005, opacity: 0, webkitTextStroke: '2px rgba(5, 215, 218, 0)' }, cursor);
                        master.to(el, { scale: 1, opacity: 1, webkitTextStroke: '2.5px rgba(5, 215, 218, 1)', duration: 0.8, ease: 'power2.out' }, cursor);
                        cursor += 1.8;
                        master.to(el, { scale: 16, opacity: 0, webkitTextStroke: '2.5px rgba(5, 215, 218, 0)', duration: 0.62, ease: 'power2.in' }, cursor);
                        cursor += 0.85;
                    });`;

const newSequence = `
                    /* Aparición de cada palabra (optimizada para mobile) */
                    const mMult = (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) || (typeof IS_TOUCH !== 'undefined' && IS_TOUCH) || window.innerWidth <= 768 ? 0.6 : 1;
                    let cursor = 0.9 * mMult;
                    wordIds.forEach(id => {
                        const el = document.getElementById(id);
                        master.set(el, { scale: 0.005, opacity: 0, webkitTextStroke: '2px rgba(5, 215, 218, 0)' }, cursor);
                        master.to(el, { scale: 1, opacity: 1, webkitTextStroke: '2.5px rgba(5, 215, 218, 1)', duration: 0.8 * mMult, ease: 'power2.out' }, cursor);
                        cursor += 1.8 * mMult;
                        master.to(el, { scale: 16, opacity: 0, webkitTextStroke: '2.5px rgba(5, 215, 218, 0)', duration: 0.62 * mMult, ease: 'power2.in' }, cursor);
                        cursor += 0.85 * mMult;
                    });`;

// Because of possible character encoding mismatches, let's replace with regex targeting the logical lines
html = html.replace(/let cursor = 0\.9;\s*wordIds\.forEach[\s\S]*?cursor \+= 0\.85;\s*\}\);/, newSequence.trim());

fs.writeFileSync(file, html, 'utf8');
console.log('Fixed index.html: Removed stray characters and sped up mobile GSAP intro.');
