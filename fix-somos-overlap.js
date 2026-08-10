const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// I'll append the new rules to the end of the existing @media (max-width: 600px) block
// The block ends around line 626 with `}`. Let's find `.agency-description p` inside it and append after it.

const mobileFixes = `
            .agency-description p {
                border-left: none;
                border-right: none;
                padding: 0 4px;
                background: none;
            }

            /* FIX: Push content below fixed navigation and optimize redundant header */
            .agency-description {
                margin-top: 100px !important; 
            }
            .agency-description h2 {
                font-size: 28px !important;
                margin-bottom: 15px !important;
            }
`;

html = html.replace(/\.agency-description p\s*\{\s*border-left:\s*none;\s*border-right:\s*none;\s*padding:\s*0 4px;\s*background:\s*none;\s*\}/, mobileFixes);

fs.writeFileSync(file, html, 'utf8');
console.log('Mobile layout overlap fixed.');
