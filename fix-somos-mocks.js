const fs = require('fs');
const path = require('path');

const file = 'c:\\\\Users\\\\Nigonz\\\\OneDrive\\\\Documentos\\\\nylon\\\\nylon-web\\\\somos.html';
let html = fs.readFileSync(file, 'utf8');

const mockElements = `
                // Mocks for missing index.html elements in somos.html
                const overlay = document.getElementById('transitionOverlay') || document.createElement('div');
                const screen2 = document.getElementById('screen2') || document.createElement('div');
                const btn = document.getElementById('spaceBtn') || document.createElement('div');
                const backBtn = document.getElementById('backBtn') || document.createElement('div');
                const bgVideo = document.getElementById('bgVideo') || { play: ()=>Promise.resolve(), pause: ()=>{}, currentTime: 0 };
                const logo = document.createElement('div');
                const logoImg = document.createElement('img');
                const scrollHint = document.createElement('div');
                const wordIds = [];
`;

// Match from `const overlay =` to `const wordIds =`
html = html.replace(/const overlay = document\.getElementById\('transitionOverlay'\);[\s\S]*?const wordIds = \[[^\]]*\];/, mockElements);

fs.writeFileSync(file, html, 'utf8');
console.log("Mocked missing elements successfully");
