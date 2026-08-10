const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// Step 1: CSS modifications
// 1. Add perspective: 1500px to .celestial-card
html = html.replace(/\.celestial-card \{([^}]*?)\}/, (match, inner) => {
    if (!inner.includes('perspective:')) {
        return `.celestial-card {${inner}\n            perspective: 1500px;\n        }`;
    }
    return match.replace(/perspective:\s*[^;]+;/, 'perspective: 1500px;');
});

// 2. Add transform-style: preserve-3d; and transition: transform 0.3s ease-out; to .card-inner
html = html.replace(/\.card-inner \{([^}]*?)\}/, (match, inner) => {
    let newInner = inner;
    if (!newInner.includes('transform-style: preserve-3d;')) {
        newInner += '\n            transform-style: preserve-3d;';
    }
    if (!newInner.includes('transition:')) {
        newInner += '\n            transition: transform 0.3s ease-out;';
    } else {
        // If there's an existing transition, maybe append to it or replace it.
        // Actually .card-inner didn't have transition before. Let's just append if it doesn't have transform transition.
        if (!newInner.includes('transform 0.3s ease-out')) {
            newInner = newInner.replace(/transition:\s*([^;]+);/, 'transition: $1, transform 0.3s ease-out;');
        }
    }
    return `.card-inner {${newInner}}`;
});

// Step 3: Mobile safeguard
// In the mobile query, target .card-inner
html = html.replace(/@media \(max-width: 600px\) \{/, `@media (max-width: 600px) {
            .card-inner {
                transform: rotateX(0deg) rotateY(0deg) !important;
            }`);

// Step 2: Inject JS logic
const jsLogic = `
            document.addEventListener("DOMContentLoaded", () => {
                // Only run 3D effects on desktop to prevent mobile freezing
                if (window.innerWidth <= 768) return;

                const wrappers = document.querySelectorAll('.celestial-card'); 
                
                wrappers.forEach(wrapper => {
                    const card = wrapper.querySelector('.card-inner') || wrapper; 
                    
                    wrapper.addEventListener('mousemove', (e) => {
                        const rect = wrapper.getBoundingClientRect();
                        const centerX = rect.left + rect.width / 2;
                        const centerY = rect.top + rect.height / 2;
                        
                        const mouseX = e.clientX - centerX;
                        const mouseY = e.clientY - centerY;
                        
                        // Rotation intensity modifiers
                        const rotateX = (mouseY / (rect.height / 2)) * -12; 
                        const rotateY = (mouseX / (rect.width / 2)) * 12;

                        card.style.transform = \`rotateX(\${rotateX}deg) rotateY(\${rotateY}deg)\`;
                    });

                    wrapper.addEventListener('mouseleave', () => {
                        // Reset rotation cleanly
                        card.style.transform = \`rotateX(0deg) rotateY(0deg)\`;
                    });
                });
            });
`;

// Remove old initTilt
html = html.replace(/function initTilt\(\) \{[\s\S]*?initTilt\(\);/, jsLogic);

fs.writeFileSync(file, html, 'utf8');
console.log("Applied 3D tilt fixes to somos.html");
