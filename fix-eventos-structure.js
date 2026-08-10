const fs = require('fs');
const path = require('path');

const dir = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web';

// 1. Fix eventos.html
const eventosPath = path.join(dir, 'eventos.html');
let eventosHtml = fs.readFileSync(eventosPath, 'utf8');

// Replace the <body ...> to include transparent-nav-page
if (!eventosHtml.includes('transparent-nav-page')) {
    eventosHtml = eventosHtml.replace(/<body([^>]*)>/, '<body$1 class="transparent-nav-page">');
}

// Remove old Eventos exceptions and add new ones
const oldEventosExceptions = /<style>\s*\/\* Eventos Specific Exceptions \*\/[\s\S]*?<\/style>/;
const newEventosExceptions = `<style>
        /* Eventos Specific Exceptions */
        .transparent-nav-page #staff-nav {
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            box-shadow: none !important;
            border-bottom: none !important;
        }
        main, .hero {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        .hero-bg {
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            width: 100% !important;
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        .hero-img {
            object-fit: cover !important;
            object-position: center 15% !important;
            width: 100% !important;
            height: 100% !important;
            transform: scale(1) !important;
        }
        .hero-split-layout {
            padding-top: 130px !important;
            position: relative;
            z-index: 10;
        }
    </style>`;

if (oldEventosExceptions.test(eventosHtml)) {
    eventosHtml = eventosHtml.replace(oldEventosExceptions, newEventosExceptions);
} else {
    eventosHtml = eventosHtml.replace('</head>', newEventosExceptions + '\n</head>');
}
fs.writeFileSync(eventosPath, eventosHtml, 'utf8');
console.log("Updated eventos.html structural fixes.");

// 2. Fix holo.html
const holoPath = path.join(dir, 'holo.html');
let holoHtml = fs.readFileSync(holoPath, 'utf8');

if (!holoHtml.includes('transparent-nav-page')) {
    holoHtml = holoHtml.replace(/<body([^>]*)>/, '<body$1 class="transparent-nav-page">');
}

// Ensure the #staff-nav uses the generic class rule
const oldHoloExceptions = /<style>\s*\/\* Holo Specific Exceptions \*\/[\s\S]*?<\/style>/;
const newHoloExceptions = `<style>
        /* Holo Specific Exceptions */
        @media (min-width: 769px) {
            #staff-nav {
                left: auto !important;
                right: 15px !important;
                transform: scale(0.9) !important;
                transform-origin: right top !important;
                width: auto !important;
            }
            .nav-logo {
                position: fixed !important;
                top: 30px !important;
                left: 40px !important;
            }
            header {
                margin-top: 3vh !important;
            }
            main.gallery-track {
                padding-top: 4vh !important;
                margin-top: 0 !important;
                gap: 50px !important;
            }
        }
        
        /* Mobile overrides to prevent main global padding */
        main, .hero, .holo-hero {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        
        .transparent-nav-page #staff-nav {
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            box-shadow: none !important;
            border-bottom: none !important;
        }
    </style>`;

if (oldHoloExceptions.test(holoHtml)) {
    holoHtml = holoHtml.replace(oldHoloExceptions, newHoloExceptions);
} else {
    holoHtml = holoHtml.replace('</head>', newHoloExceptions + '\n</head>');
}
fs.writeFileSync(holoPath, holoHtml, 'utf8');
console.log("Updated holo.html structural fixes.");
