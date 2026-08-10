const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';

// 1. Fix holo.html
const holoPath = path.join(dir, 'holo.html');
let holoHtml = fs.readFileSync(holoPath, 'utf8');

const holoStyle = `
    <style>
        /* Holo Specific Exceptions */
        #staff-nav {
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            border: none !important;
            box-shadow: none !important;
        }
        main, .hero, .holo-hero {
            padding-top: 140px !important;
        }
    </style>
</head>`;

if (holoHtml.includes('</head>') && !holoHtml.includes('Holo Specific Exceptions')) {
    holoHtml = holoHtml.replace('</head>', holoStyle);
    fs.writeFileSync(holoPath, holoHtml, 'utf8');
    console.log("Applied Holo specific fixes.");
}

// 2. Fix eventos.html
const eventosPath = path.join(dir, 'eventos.html');
let eventosHtml = fs.readFileSync(eventosPath, 'utf8');

const eventosStyle = `
    <style>
        /* Eventos Specific Exceptions */
        #staff-nav {
            background: linear-gradient(to bottom, rgba(0,0,0,0.8), transparent) !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            border: none !important;
            box-shadow: none !important;
        }
        .hero-img {
            object-fit: cover !important;
            object-position: center 15% !important;
            transform: scale(1) !important;
            min-height: 100vh !important;
        }
        main, .hero {
            padding-top: 140px !important;
        }
    </style>
</head>`;

if (eventosHtml.includes('</head>') && !eventosHtml.includes('Eventos Specific Exceptions')) {
    eventosHtml = eventosHtml.replace('</head>', eventosStyle);
    fs.writeFileSync(eventosPath, eventosHtml, 'utf8');
    console.log("Applied Eventos specific fixes.");
}
