const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// I know that the block ends with:
//                     });
//                 });
//             });

// I want to change the last `});` to `})();`
// Let's do this safely by finding the exact string:
const target = `
                    wrapper.addEventListener('mouseleave', () => {
                        // Reset rotation cleanly
                        card.style.transform = \`perspective(1500px) rotateX(0deg) rotateY(0deg)\`;
                    });
                });
            });`;

const replacement = `
                    wrapper.addEventListener('mouseleave', () => {
                        // Reset rotation cleanly
                        card.style.transform = \`perspective(1500px) rotateX(0deg) rotateY(0deg)\`;
                    });
                });
            })();`;

html = html.replace(target, replacement);

fs.writeFileSync(file, html, 'utf8');
console.log("Fixed IIFE manually");
