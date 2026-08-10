const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// Fix 1: CSS - position: relative !important -> position: fixed !important
html = html.replace(
    '#screen2 { opacity: 1 !important; pointer-events: auto !important; position: relative !important; z-index: 10 !important; }',
    '#screen2 { opacity: 1 !important; pointer-events: auto !important; position: fixed !important; z-index: 10 !important; }'
);

// Fix 2: JS - Starfield silent fail
const oldCtx = `const ctx = canvas.getContext('2d', { alpha: false });`;
const newCtx = `if (!canvas) { /* starfield not present in this page */ }
            const ctx = canvas ? canvas.getContext('2d', { alpha: false }) : null;`;
html = html.replace(oldCtx, newCtx);

html = html.replace('function initStars() {', 'function initStars() {\n                if (!canvas || !ctx) return;');
html = html.replace('function drawStars(ts) {', 'function drawStars(ts) {\n                if (!canvas || !ctx) return;');

fs.writeFileSync(file, html, 'utf8');
console.log('Fixed CSS scroll and JS starfield crash.');
