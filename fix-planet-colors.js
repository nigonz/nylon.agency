const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\servicios.html';
let html = fs.readFileSync(file, 'utf8');

// The original line for SOCIAL MEDIA colors is:
// hex:'#B8A038', hexDark:'#3A300A', hexLight:'#F0DE8A', size:0.92, offset:Math.PI/3,

const oldColors = "hex:'#B8A038', hexDark:'#3A300A', hexLight:'#F0DE8A'";
const newColors = "hex:'#8B1C47', hexDark:'#380B1C', hexLight:'#D95A8D'";

if (html.includes(oldColors)) {
    html = html.replace(oldColors, newColors);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Updated colors to morado borgoña");
} else {
    console.log("Could not find the exact color string.");
}
