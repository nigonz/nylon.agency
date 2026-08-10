const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\servicios.html';
let html = fs.readFileSync(file, 'utf8');

const oldCopyMatch = html.match(/copy:\`No se trata de gastar[\s\S]*?para crecer.\`/);
if (oldCopyMatch) {
    const newCopy = "copy:`La identidad visual es el primer contacto con tu audiencia.\\n\\nDiseñamos piezas gráficas con propósito, buscando no solo estética, sino impacto y coherencia.\\n\\nDesde branding integral hasta assets digitales, creamos una identidad que comunica la esencia de tu marca y perdura en el tiempo.`";
    html = html.replace(oldCopyMatch[0], newCopy);
    fs.writeFileSync(file, html, 'utf8');
    console.log("Updated copy for Diseño Gráfico");
} else {
    console.log("Could not find the Paid Media copy string.");
}
