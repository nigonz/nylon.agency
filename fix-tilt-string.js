const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

// Fix the transform string in the mousemove event
html = html.replace(/card\.style\.transform = `rotateX\(\$\{rotateX\}deg\) rotateY\(\$\{rotateY\}deg\)`/g, "card.style.transform = `perspective(1500px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`");

// Fix the transform string in the mouseleave event
html = html.replace(/card\.style\.transform = `rotateX\(0deg\) rotateY\(0deg\)`/g, "card.style.transform = `perspective(1500px) rotateX(0deg) rotateY(0deg)`");

fs.writeFileSync(file, html, 'utf8');
console.log("Fixed missing perspective() in transform string");
