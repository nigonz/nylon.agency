const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// The script crashes because it tries to access canvas and video which we removed.
// Let's replace the canvas lines:
html = html.replace(/const canvas = document.getElementById\('starfield'\);[\s\S]*?rafStar = requestAnimationFrame\(drawStars\);/g, `
            // Starfield removed for somos.html
`);

// Also fix the loadMainVideo part
html = html.replace(/window\.addEventListener\('load', \(\) => {[\s\S]*?}\);/g, `
            // Video load removed for somos.html
`);

// Also fix the whenGSAP block references to missing elements
html = html.replace(/const bgVideo = document.getElementById\('bgVideo'\);/g, `const bgVideo = { play: ()=>Promise.resolve(), pause: ()=>{} }; // mocked`);
html = html.replace(/const logo = document.querySelector\('\.nylon-logo-wrap'\);/g, `const logo = document.createElement('div'); // mocked`);
html = html.replace(/const logoImg = document.querySelector\('\.nylon-logo-img'\);/g, `const logoImg = document.createElement('img'); // mocked`);
html = html.replace(/const scrollHint = document.getElementById\('scrollHint'\);/g, `const scrollHint = document.createElement('div'); // mocked`);

// To be even safer, wordIds elements are missing too:
// const wordIds = ['wInfinita', 'wCreatividad', 'wAdaptabilidad'];
// We can just try-catch the entire whenGSAP body, or just replace the elements with dummy divs
html = html.replace(/const wordIds = \['wInfinita', 'wCreatividad', 'wAdaptabilidad'\];/g, `
                const wordIds = []; // Disabled missing words
`);

// The problem is that the script in somos.html contains a lot of logic tied to the hero section.
// Another approach is to just inject a dummy hero hidden in HTML so the JS doesn't crash:
// But we already deleted it in HTML. Let's just wrap the GSAP sequence in a try-catch to be bulletproof.

html = html.replace(/whenGSAP\(\(\) => {/g, `whenGSAP(() => {
                try {`);
html = html.replace(/}\); \/\/ end whenGSAP/g, `} catch (err) { console.warn("GSAP sequence bypassed due to missing hero elements."); }
            }); // end whenGSAP`);

// Write the file back
fs.writeFileSync(file, html, 'utf8');
console.log("Fixed JS errors in somos.html");
