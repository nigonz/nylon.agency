<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NYLON | Host & Conducción</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<style>
/* ══════════════════════════════════════════
   ROOT & RESET
══════════════════════════════════════════ */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --teal: #00756c;
  --teal-l: #02968d;
  --teal-g:rgba(26,143,160,.28);
  --cyan: #00756d;
  --cyan2:rgba(0,200,220,1);
  --bg:#020205; 
  --bg2:#03040a;
  --glass:rgba(255,255,255,.045);
  --glass-b:rgba(255,255,255,.09);
  --text:rgba(255,255,255,.88);
  --text-d:rgba(255,255,255,.35);
  --cshadow:0 20px 60px rgba(0,0,0,.82),0 0 35px rgba(26,143,160,.22),0 0 80px rgba(0,110,140,.10),inset 0 1px 0 rgba(255,255,255,.07);
  --cshadow-h:0 40px 100px rgba(0,0,0,.95),0 0 55px rgba(26,143,160,.44),0 0 120px rgba(0,180,200,.20),inset 0 1px 0 rgba(255,255,255,.12);
}
main, .hero { padding-top: 0 !important; margin-top: 0 !important; }

html{scroll-behavior:smooth}
body{font-family:'Sora',sans-serif;background:var(--bg);min-height:100vh;overflow-x:hidden;color:var(--text);cursor:crosshair}
button,a,.vcard,.pcard,.lbx{cursor:pointer}
::-webkit-scrollbar{width:3px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:rgba(26,143,160,.40);border-radius:2px}

  #staff-nav {
            position: fixed; 
            top: 20px; 
            left: 50%; 
            transform: translateX(-50%);
            width: 92%;
            max-width: 1200px;
            z-index: 2000;
            display: flex; 
            align-items: center; 
            justify-content: space-between;
            padding: 15px 30px !important;
            min-height: 60px;
            background: rgba(5, 5, 12, 0.55);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 40px;
            pointer-events: auto;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }
        .nav-logo {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 13px; font-weight: 700;
            letter-spacing: 5px; color: #fff;
            text-transform: uppercase;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        .nav-logo:hover {
            color: #00756c;
        }
        .nav-links {
            display: flex; gap: 30px;
        }
        .nav-links a {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 11px; font-weight: 600;
            letter-spacing: 2px; color: rgba(255, 255, 255, 0.6);
            text-transform: uppercase;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .nav-links a:hover, .nav-links a.active {
            color: #00756c;
        }
        .mobile-menu-btn {
            display: none; background: none; border: none;
            color: #fff; font-size: 20px; cursor: pointer;
        }
        @media(max-width: 768px) {
            .nav-links { display: none; }
            .mobile-menu-btn { display: block; }
        }

/* ══════════════════════════════════════════
   LOADER
══════════════════════════════════════════ */
#loader{
  position:fixed;inset:0;background:#010103;z-index:9999;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  transition:opacity .6s,visibility .6s;
}
#loader.out{opacity:0;visibility:hidden}
.l-ring{
  width:160px;height:160px;border-radius:50%;
  border:1px solid rgba(26,143,160,.1);
  border-top-color:var(--teal-l);
  animation:spin 1.8s cubic-bezier(.4,0,.2,1) infinite;
  display:flex;align-items:center;justify-content:center;
}
.l-ring::before{
  content:'';width:120px;height:120px;border-radius:50%;
  border:1px dashed rgba(26,143,160,.3);
  animation:spin 3s linear infinite reverse;
}
.l-core{
  position:absolute;font-family:'Orbitron',sans-serif;font-size:10px;
  letter-spacing:4px;color:var(--teal-l);
  text-shadow:0 0 10px var(--teal);
  animation:pulse 2s ease-in-out infinite;
}
.l-bar{width:200px;height:2px;background:rgba(255,255,255,.05);margin-top:40px;border-radius:2px;overflow:hidden}
.l-fill{height:100%;background:var(--teal-l);width:0%;box-shadow:0 0 10px var(--teal)}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse{0%,100%{opacity:.5}50%{opacity:1}}

/* ══════════════════════════════════════════
   NEBULA BG (Canvas + CSS)
══════════════════════════════════════════ */
#bgCanvas{position:fixed;inset:0;z-index:0;pointer-events:none;background:#010103}
.neb{position:fixed;border-radius:50%;pointer-events:none;z-index:1}
.na{width:1100px;height:1100px;background:radial-gradient(ellipse,rgba(0,180,200,.08) 0%,transparent 68%);top:-35%;left:-20%;filter:blur(95px);animation:nd 36s ease-in-out infinite alternate}
.nb{width:800px;height:800px;background:radial-gradient(ellipse,rgba(8,25,120,.15) 0%,transparent 68%);bottom:-28%;right:-24%;filter:blur(105px);animation:nd 42s ease-in-out infinite alternate-reverse}
.nc{width:520px;height:520px;background:radial-gradient(ellipse,rgba(0,110,130,.10) 0%,transparent 68%);top:36%;left:10%;filter:blur(78px);animation:nd 29s ease-in-out infinite alternate}
.nd-n{width:380px;height:380px;background:radial-gradient(ellipse,rgba(90,10,75,.08) 0%,transparent 68%);top:55%;right:6%;filter:blur(68px);animation:nd 23s ease-in-out infinite alternate-reverse}
.ne-n{width:300px;height:300px;background:radial-gradient(ellipse,rgba(0,80,160,.09) 0%,transparent 68%);top:16%;right:20%;filter:blur(62px);animation:nd 19s ease-in-out infinite alternate}
@keyframes nd{0%{transform:translate(0,0) scale(1)}100%{transform:translate(32px,22px) scale(1.10)}}
#dust{position:fixed;inset:0;z-index:2;pointer-events:none;overflow:hidden}
.dp{position:absolute;border-radius:50%;background:rgba(255,255,255,.55);animation:dp-rise linear infinite}
@keyframes dp-rise{0%{transform:translateY(0) translateX(0);opacity:0}8%{opacity:1}92%{opacity:.3}100%{transform:translateY(-110vh) translateX(var(--dx,0px));opacity:0}}

/* ══════════════════════════════════════════
   HUD
══════════════════════════════════════════ */
.hud{
  position:fixed;top:0;left:0;right:0;z-index:100;
  padding:14px 28px;display:flex;align-items:center;justify-content:space-between;
  background:linear-gradient(to bottom,rgba(2,2,5,.85),transparent);
  pointer-events:none;
}
.hud-logo{font-family:'Orbitron',sans-serif;font-size:10px;letter-spacing:4px;color:rgba(26,143,160,.72);display:flex;align-items:center;gap:8px}
.hud-dot{width:6px;height:6px;border-radius:50%;background:var(--teal-l);box-shadow:0 0 8px var(--teal);animation:blink 2.5s ease-in-out infinite}
.hud-center{font-family:'Orbitron',sans-serif;font-size:8px;letter-spacing:3px;color:rgba(26,143,160,.40);text-align:center}
.hud-coord{font-family:'Orbitron',sans-serif;font-size:8px;letter-spacing:2px;color:rgba(26,143,160,.48)}

/* ══════════════════════════════════════════
   MAIN / HERO
══════════════════════════════════════════ */
main{position:relative;z-index:10}

.hero{
  position:relative;width:100%;height:100vh;min-height:640px;
  overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center;
}
.hero-bg{position:absolute;inset:0;z-index:0; background-color: #010103;}
.hero-img{
  width:100%;height:100%;object-fit:cover;transform:scale(1.10);
  will-change:transform;
  filter:brightness(.18) saturate(1.2) contrast(1.2) hue-rotate(15deg); 
  opacity: 0.8;
}
.hero-vignette{
  position:absolute;inset:0;
  background:
    radial-gradient(circle at center, transparent 20%, rgba(2,2,5,0.8) 70%, rgba(2,2,5,1) 100%),
    linear-gradient(to bottom, rgba(2,2,5,0.5) 0%, transparent 30%, transparent 60%, rgba(2,2,5,1) 100%);
}

/* ── HERO SPLIT LAYOUT ── */
.hero-split-layout {
  position:relative; z-index:5;
  display:flex; width:100vw; 
  height:100vh;
  margin-top:-80px;
  padding-top:80px;
  animation:hero-rise 1.8s cubic-bezier(.16,1,.3,1) .4s both;
}
.split-text {
  flex:1; display:flex; flex-direction:column;
  justify-content:center; align-items:flex-start;
  padding: 40px 40px 40px calc(max(4vw, (100vw - 1200px)/2) + 30px); z-index:10;
}
.split-image {
  flex:1; position:relative; overflow:hidden;
  border-left:1px solid rgba(0,200,220,0.2);
  margin-top:-80px; /* Sube la imagen anulando el padding del contenedor padre */
  height:calc(100vh + 80px);
}
.split-image img {
  width:100%; height:100%; object-fit:cover; object-position:center 10%;
}
.split-overlay {
  position:absolute; inset:0;
  background:linear-gradient(to left, transparent 60%, var(--bg) 100%);
}
@media(max-width:900px) {
  .hero-split-layout { flex-direction:column-reverse; }
  .split-text, .split-image { flex:auto; height:50vh; }
  .split-text { padding:24px; align-items:center; }
}

.holo-wrap{
  position:relative;z-index:5;
  display:flex;flex-direction:column;align-items:center;
  opacity:0;animation:hero-rise 1.8s cubic-bezier(.16,1,.3,1) .4s both;
}
@keyframes hero-rise{from{opacity:0;transform:translateY(36px)}to{opacity:1;transform:translateY(0)}}

#holoCanvas{
  display:block;
  width:min(520px,90vw);
  height:min(360px,62vw);
  filter:drop-shadow(0 0 25px rgba(0,180,200,.45)) drop-shadow(0 0 60px rgba(0,140,160,.25));
}

.holo-readouts{position:absolute;inset:0;pointer-events:none;}
.hdr-item{
  position:absolute;font-family:'Orbitron',sans-serif;font-size:8px;letter-spacing:2.5px;
  text-transform:uppercase;color:rgba(0,200,220,.85);padding:6px 10px;
  border-left:1px solid rgba(0,200,220,.50);background:rgba(0,10,20,.6);
  backdrop-filter:blur(8px);animation:hdr-flicker 4s ease-in-out infinite;white-space:nowrap;
}
.hdr-item span{display:block;color:rgba(0,180,200,.58);font-size:7px;letter-spacing:1.5px;margin-bottom:2px}
.hdr-item.left{left:0;top:42%;transform:translateY(-50%);border-left:none;border-right:1px solid rgba(0,200,220,.50);text-align:right}
.hdr-item.right{right:0;top:42%}
.hdr-item.top-l{left:8%;top:12%;font-size:7px}
.hdr-item.top-r{right:8%;top:12%;font-size:7px;border-left:none;border-right:1px solid rgba(0,200,220,.50);text-align:right}
@keyframes hdr-flicker{0%,100%{opacity:.7}45%{opacity:.9}50%{opacity:.3}55%{opacity:.9}60%{opacity:.7}}

.namecard{
  position:relative; margin-top:10px; padding:0; text-align:left;
  background:transparent;
  border:none;
  backdrop-filter:none;
  box-shadow:none;
}
.namecard::before,.namecard::after,.nc-br,.nc-bl{display:none;}


.nc-label{
  font-family:'Orbitron',sans-serif;font-size:9px;letter-spacing:6px;text-transform:uppercase;
  color:rgba(0,200,220,.7);margin-bottom:4px;
}
.nc-name{
  font-family:'Sora',sans-serif; font-size:clamp(40px,6vw,68px); font-weight:800;
  letter-spacing:-1px;line-height:1.1; text-transform: uppercase; margin-top: 0px; text-align:left;
}
.nc-name em{
  font-style:normal;
  background:linear-gradient(128deg, #ffffff, #178d8f, #0f5b5c);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  text-shadow: 0 0 20px rgba(23,141,143,0.3);
}
.nc-sub{
  font-family:'Space Grotesk',sans-serif;font-size:13px; font-weight: 500;
  color:rgba(255,255,255,.6);letter-spacing:3px;margin-top:2px; text-transform: uppercase; text-align:left;
}
.nc-tags{display:flex;gap:8px;justify-content:flex-start;flex-wrap:wrap;margin-top:12px}
.nc-tag{
  padding:4px 16px;border-radius:20px;
  font-family:'Space Grotesk',sans-serif;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;
  background:rgba(23,141,143,0.1);border:1px solid #178d8f;color:#178d8f;
  transition:all 0.3s; cursor:pointer;
}
.nc-tag:hover{
  background:rgba(23,141,143,0.2);
  box-shadow:0 0 15px rgba(23,141,143,0.4);
}

.scroll-cue{
  margin-top:35px;display:flex;flex-direction:column;align-items:center;gap:7px;
  color:rgba(255,255,255,.4);font-family:'Space Grotesk',sans-serif;font-size:10px;letter-spacing:4px;text-transform:uppercase;
}
.s-tube{width:24px;height:40px;border-radius:12px;border:1px solid rgba(255,255,255,.2);display:flex;justify-content:center;padding-top:7px}
.s-ball{width:4px;height:4px;border-radius:50%;background:var(--teal-l);box-shadow:0 0 8px var(--teal);animation:sb 2.2s ease-in-out infinite}
@keyframes sb{0%,100%{transform:translateY(0);opacity:1}55%{transform:translateY(18px);opacity:.2}}

/* ══════════════════════════════════════════
   SECTION HEADERS
══════════════════════════════════════════ */
.sec-hd{
  position:relative;z-index:10;display:flex;align-items:center;gap:16px;
  padding:88px 44px 0;max-width:1260px;margin:0 auto;width:100%;
}
.sec-orb{
  width:32px;height:32px;flex-shrink:0;border-radius:50%;
  display:flex;align-items:center;justify-content:center;font-size:12px;
  background:var(--glass-b);border:1px solid rgba(0,200,220,.25);color:var(--teal-l);
  box-shadow:0 0 15px rgba(0,180,200,.15);
}
.sec-hd h2{
  font-family:'Sora',sans-serif;font-size:clamp(20px,2vw,28px);font-weight:400;
  text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,.9);
}
.sec-line{flex:1;height:1px;background:linear-gradient(90deg,rgba(0,200,220,.2),transparent)}

/* ══════════════════════════════════════════
   VIDEO GRID (ESTILO EVENTOS.HTML)
══════════════════════════════════════════ */
.vsec {
  position: relative; z-index: 10;
  padding: 40px 0 120px;
}

.vgrid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 30px;
  max-width: 1260px;
  margin: 0 auto;
  padding: 0 44px;
}

.vcard {
  position: relative;
  background: rgba(1, 4, 10, 0.4);
  border: 1px solid rgba(0, 200, 220, 0.15);
  border-radius: 20px;
  padding: 16px;
  transform-style: preserve-3d;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.vcard:hover {
  background: rgba(1, 4, 10, 0.6);
  border-color: rgba(0, 200, 220, 0.4);
  box-shadow: 0 25px 50px rgba(0,0,0,0.6), 0 0 30px rgba(0, 200, 220, 0.15);
}

.vframe{
  position:relative;
  /* ✨ EL CAMBIO A FORMATO CELULAR VERTICAL ✨ */
  aspect-ratio: 9/16; 
  overflow:hidden;
  border-radius:20px 20px 0 0;
  background:#000;
}

/* ═══ VIDEO FACADE (Patrón Lazy Loading) ═══ */
.video-facade {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 100%);
  border-radius: 20px 20px 0 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;
}

.video-facade::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(5, 215, 218, 0.1) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.video-facade:hover {
  background: linear-gradient(135deg, #0f0f1a 0%, #1f1f3e 100%);
}

.video-facade:hover::before {
  opacity: 1;
}

.video-facade-play-btn {
  position: relative;
  width: 80px;
  height: 80px;
  background: rgba(5, 215, 218, 0.9);
  border-radius: 50%;
  display: none;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 30px rgba(5, 215, 218, 0.4);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.video-facade-play-btn svg {
  width: 30px;
  height: 30px;
  fill: #fff;
  margin-left: 5px;
}

.video-facade:hover .video-facade-play-btn {
  transform: scale(1.1);
}

/* Área central oculta que se usa de trigger (si es necesario) */
.vcard-click-zone {
  position: absolute;
  inset: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none; /* Dejamos que los clics pasen al facade */
}
.vcard:hover .vcard-click-zone {
  opacity: 1;
}

.vcard-play-btn {
  width: 60px;
  height: 60px;
  background: rgba(0, 200, 220, 0.85);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 25px rgba(0, 200, 220, 0.5);
  transform: translateZ(30px);
}
.vcard-play-btn svg {
  width: 24px;
  height: 24px;
  fill: #fff;
  margin-left: 4px;
}


.vfooter {
  padding: 16px 8px 8px;
}

.vf-title {
  font-family: 'Sora', sans-serif;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 4px;
  letter-spacing: 0.5px;
}

.vf-sub {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 1px;
}

/* ══════════════════════════════════════════
   PHOTO GRID (Manteniendo estilo Sci-Fi original)
══════════════════════════════════════════ */
.psec{position:relative;z-index:10;padding:40px 0 120px;perspective:1200px}
.constel{position:absolute;inset:0;z-index:0;pointer-events:none}
.constel line{stroke:rgba(0,180,200,.15);stroke-width:1;stroke-dasharray:4 4;animation:dash 20s linear infinite}
@keyframes dash{to{stroke-dashoffset:-100}}

.pgrid{
  position:relative;z-index:1;max-width:1260px;margin:0 auto;padding:0 44px;
  display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:32px;
}
.pcard{
  position:relative;border-radius:12px;overflow:hidden;background:#010103;
  transform-style:preserve-3d;transition:transform .4s cubic-bezier(.16,1,.3,1);
  box-shadow:var(--cshadow);
}
.pcard::after{content:'';position:absolute;inset:0;border:1px solid rgba(255,255,255,.05);border-radius:12px;pointer-events:none}
.pcard img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block;filter:grayscale(60%) contrast(1.1);transition:filter .4s}
.pcard-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(1,1,3,.9) 0%,transparent 60%);pointer-events:none}
.pcard-shine{position:absolute;inset:0;pointer-events:none;mix-blend-mode:overlay;opacity:.6}
.pcard-exp{
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) translateZ(30px) scale(0);
  width:48px;height:48px;background:rgba(26,143,160,.8);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 20px var(--teal);transition:transform .4s cubic-bezier(.175,.885,.32,1.275);
}
.pcard-exp svg{width:20px;height:20px;stroke:#fff;stroke-width:2;fill:none}
.pcard:hover{box-shadow:var(--cshadow-h)}
.pcard:hover img{filter:grayscale(0) contrast(1.05)}
.pcard:hover .pcard-exp{transform:translate(-50%,-50%) translateZ(30px) scale(1)}

/* ══════════════════════════════════════════
   REVEAL & ANIMATIONS
══════════════════════════════════════════ */
.fw{perspective:1000px}
.reveal{opacity:0;transform:translateY(40px) rotateX(10deg);transition:all 1s cubic-bezier(.16,1,.3,1)}
.reveal.vis{
  opacity:1;transform:translateY(0) rotateX(0);
  animation:var(--fa,none) var(--dur,6s) ease-in-out infinite alternate;
}
@keyframes float-a{0%{transform:translateY(0)}100%{transform:translateY(-12px)}}
@keyframes float-b{0%{transform:translateY(0)}100%{transform:translateY(-18px)}}
@keyframes float-c{0%{transform:translateY(0)}100%{transform:translateY(-8px)}}

/* ══════════════════════════════════════════
   LIGHTBOX (FOTOS)
══════════════════════════════════════════ */
#lb{
  position:fixed;inset:0;background:rgba(1,1,3,.95);backdrop-filter:blur(10px);
  z-index:99999;display:flex;align-items:center;justify-content:center;
  opacity:0;visibility:hidden;transition:all .4s;
}
#lb.on{opacity:1;visibility:visible}
#lbimg{max-width:90vw;max-height:90vh;border-radius:4px;box-shadow:0 0 60px rgba(0,0,0,.8);transform:scale(.95);transition:transform .4s}
#lb.on #lbimg{transform:scale(1)}
.lbx{
  position:absolute;top:30px;right:40px;color:rgba(255,255,255,.6);
  font-family:'Space Grotesk',sans-serif;font-size:24px;transition:color .3s;
}
.lbx:hover{color:#fff}

/* ══════════════════════════════════════════
   VIDEO LIGHTBOX (Para los videos verticales)
══════════════════════════════════════════ */
#vlb {
  position: fixed; inset: 0; background: rgba(1, 2, 5, 0.98);
  backdrop-filter: blur(15px); z-index: 99999;
  display: flex; align-items: center; justify-content: center;
  opacity: 0; visibility: hidden; transition: all 0.4s;
}
#vlb.on { opacity: 1; visibility: visible; }
.vlb-x {
  position: absolute; top: 30px; right: 40px; color: rgba(255, 255, 255, 0.5);
  font-family: 'Space Grotesk', sans-serif; font-size: 28px; cursor: pointer;
  transition: color 0.3s; z-index: 10;
}
.vlb-x:hover { color: #fff; }

/* Contenedor del Iframe (Proporción Celular 9:16) */
#vlb-inner {
  position: relative;
  width: 90vw;
  max-width: 450px; /* Ancho máximo para mantenerlo como celular en desktop */
  aspect-ratio: 9/16; 
  background: #000;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 0 60px rgba(0,0,0,0.8), 0 0 30px rgba(0,200,220,0.1);
  transform: scale(0.95); transition: transform 0.4s;
}
#vlb.on #vlb-inner { transform: scale(1); }
#vlb-iframe {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;
}
</style>
</head>
<body>

<nav id="staff-nav">
  <a href="index.html" class="nav-logo">NYLON</a>
  <div class="nav-links">
      <a href="directores.html">Directores</a>
      <a href="produccion.html">Producción</a>
      <a href="host.html" class="active">Host</a>
      <a href="eventos.html">Eventos</a>
      <a href="contacto.html">Contacto</a>
  </div>
  <button class="mobile-menu-btn">☰</button>
</nav>

<div id="loader">
  <div class="l-ring"><div class="l-core">SISTEMA</div></div>
  <div class="l-bar"><div class="l-fill" id="lFill"></div></div>
</div>

<canvas id="bgCanvas"></canvas>
<div class="neb na"></div><div class="neb nb"></div>
<div class="neb nc"></div><div class="neb nd-n"></div><div class="neb ne-n"></div>
<div id="dust"></div>



<div id="lb"><div class="lbx" id="lbx">✕</div><img id="lbimg" src="" alt=""></div>

<!-- VIDEO LIGHTBOX -->
<div id="vlb">
  <div class="vlb-x" id="vlbx">✕</div>
  <div id="vlb-inner">
    <iframe id="vlb-iframe" src="" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

<main>

  <section class="hero">
    <div class="hero-bg" style="background: linear-gradient(to bottom, #010103 0%, rgba(0, 70, 80, 0.4) 100%); z-index: 0;">
    </div>

    <div class="hero-split-layout">
      <div class="split-text">
        <div class="namecard">
          <div class="nc-br"></div><div class="nc-bl"></div>
          <div class="nc-label">◈ Archivo Audiovisual ◈</div>
          <div class="nc-name">NATALIA <em>GARAYGORTA</em></div>
          <div class="nc-sub">Periodista</div>
          <div class="nc-tags">
            <span class="nc-tag">HOST ON CAMERA TALENT</span>
            <span class="nc-tag">PROYECT MANAGER</span>
            <span class="nc-tag">PERIODISMO</span>
          </div>
        </div>

        <div class="scroll-cue" style="align-self: flex-start; margin-top: 40px;">
          <div class="s-tube"><div class="s-ball"></div></div>
          <span>Explorar Archivos</span>
        </div>
      </div>
      <div class="split-image">
        <img src="fotos/naty0.jpeg" alt="Natalia Garaygorta">
        <div class="split-overlay"></div>
      </div>
    </div>
  </section>

  <div class="sec-hd reveal">
    <div class="sec-orb">▶</div>
    <h2>Proyectos Destacados</h2>
    <div class="sec-line"></div>
  </div>

  <section class="vsec">
    <div class="vgrid">
      
      <!-- VIDEOS VERTICALES -->
      <div class="fw reveal" style="--delay:0s;--dur:7s;--fa:float-a">
        <div class="vcard tilt" data-vimeo="1210821329">
          <div class="vframe">
            <!-- La imagen de fondo la carga JS via API de Vimeo -->
            <div class="video-facade" data-video-id="1210821329">
              <div class="video-facade-play-btn">
                <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
              </div>
            </div>
          </div>
          <div class="vcard-click-zone">
            <div class="vcard-play-btn">
              <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
            </div>
          </div>
          <div class="vfooter">
            <div class="vf-title">EN CAMPO</div>
            <div class="vf-sub">Cobertura Especial · 2025</div>
          </div>
        </div>
      </div>

      <div class="fw reveal" style="--delay:0.65s;--dur:8.1s;--fa:float-b">
        <div class="vcard tilt" data-vimeo="1178232720">
          <div class="vframe">
            <div class="video-facade" data-video-id="1178232720">
              <div class="video-facade-play-btn">
                <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
              </div>
            </div>
          </div>
          <div class="vcard-click-zone">
            <div class="vcard-play-btn">
              <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
            </div>
          </div>
          <div class="vfooter">
            <div class="vf-title">MODO PILOTO</div>
            <div class="vf-sub">Spot Comercial · 2024</div>
          </div>
        </div>
      </div>

      <div class="fw reveal" style="--delay:1.30s;--dur:7.4s;--fa:float-c">
        <div class="vcard tilt" data-vimeo="1210821329">
          <div class="vframe">
            <div class="video-facade" data-video-id="1210821329">
              <div class="video-facade-play-btn">
                <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
              </div>
            </div>
          </div>
          <div class="vcard-click-zone">
            <div class="vcard-play-btn">
              <svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
            </div>
          </div>
          <div class="vfooter">
            <div class="vf-title">IMG_7587</div>
            <div class="vf-sub">Cobertura 2025</div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <div class="sec-hd reveal" style="margin-top:12px">
    <div class="sec-orb">◈</div>
    <h2>Detrás de Escena</h2>
    <div class="sec-line"></div>
  </div>

  <section class="psec">
    <svg class="constel" id="constelSvg" aria-hidden="true"></svg>
    <div class="pgrid" id="pgrid">
      <div class="fw reveal" style="--delay:0s;--dur:7.2s;--fa:float-b"><div class="pcard tilt" data-src="fotos/naty.jpeg"><img style="object-fit:cover; object-position:center;" src="fotos/naty.jpeg" alt="Fotografía 1" loading="lazy"><div class="pcard-ov"></div><div class="pcard-shine"></div><div class="pcard-exp"><svg viewBox="0 0 24 24"><polyline points="15,3 21,3 21,9"/><polyline points="9,21 3,21 3,15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg></div></div></div>
      <div class="fw reveal" style="--delay:0.35s;--dur:8.6s;--fa:float-a"><div class="pcard tilt" data-src="fotos/naty1.png"><img style="object-fit:cover; object-position:center;" src="fotos/naty1.png" alt="Fotografía 2" loading="lazy"><div class="pcard-ov"></div><div class="pcard-shine"></div><div class="pcard-exp"><svg viewBox="0 0 24 24"><polyline points="15,3 21,3 21,9"/><polyline points="9,21 3,21 3,15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg></div></div></div>
      
      
      
      
    
<div class="fw reveal" style="--delay:1.2s;--dur:7.2s;--fa:float-b"><div class="pcard tilt" data-src="fotos/naty2.png"><img style="object-fit:cover; object-position:center;" src="fotos/naty2.png" alt="Fotografía 3" loading="lazy"><div class="pcard-ov"></div><div class="pcard-shine"></div><div class="pcard-exp"><svg viewBox="0 0 24 24"><polyline points="15,3 21,3 21,9"/><polyline points="9,21 3,21 3,15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg></div></div></div></div>
  </section>
</main>

<script>
(function(){const fill=document.getElementById('lFill'),loader=document.getElementById('loader');let p=0;const t=setInterval(()=>{p+=Math.random()*20+3;if(p>=100){p=100;clearInterval(t);setTimeout(()=>loader.classList.add('out'),280)}fill.style.width=Math.min(p,100)+'%';},90);})();
(function(){const cv=document.getElementById('bgCanvas'),ctx=cv.getContext('2d');let W,H,stars=[],shoots=[],nebDust=[];let offscreen=null;function rsz(){W=cv.width=innerWidth;H=cv.height=innerHeight;buildGalaxyBg();}window.addEventListener('resize',()=>{clearTimeout(window._rszT);window._rszT=setTimeout(rsz,200)});rsz();function buildGalaxyBg(){offscreen=document.createElement('canvas');offscreen.width=W;offscreen.height=H;const oc=offscreen.getContext('2d');const bandAngle=-12*Math.PI/180;const bCos=Math.cos(bandAngle),bSin=Math.sin(bandAngle);const bandW=H*0.38;for(let i=0;i<3200;i++){const along=(Math.random()-.5)*Math.sqrt(W*W+H*H)*1.1;const perp=(Math.random()-.5)*bandW;const gauss=Math.exp(-Math.pow(perp/(bandW*0.28),2));const px=W/2+along*bCos-perp*bSin;const py=H/2+along*bSin+perp*bCos;if(px<0||px>W||py<0||py>H)continue;const a=gauss*(Math.random()*0.45+0.04);oc.beginPath();oc.arc(px,py,Math.random()*0.55+0.08,0,Math.PI*2);oc.fillStyle=`rgba(190,210,255,${a.toFixed(3)})`;oc.fill();}const clusters=[{cx:W*0.22,cy:H*0.18,r:H*0.10,n:400,col:'rgba(220,235,255,'},{cx:W*0.78,cy:H*0.25,r:H*0.08,n:300,col:'rgba(200,225,255,'},{cx:W*0.55,cy:H*0.72,r:H*0.09,n:350,col:'rgba(210,230,255,'},{cx:W*0.12,cy:H*0.60,r:H*0.07,n:250,col:'rgba(230,220,255,'},];clusters.forEach(cl=>{for(let i=0;i<cl.n;i++){const r=Math.random()*cl.r;const ang=Math.random()*Math.PI*2;const px=cl.cx+r*Math.cos(ang);const py=cl.cy+r*Math.sin(ang);const a=Math.exp(-r/cl.r*2.5)*(Math.random()*0.55+0.12);oc.beginPath();oc.arc(px,py,Math.random()*0.7+0.1,0,Math.PI*2);oc.fillStyle=cl.col+a.toFixed(3)+')';oc.fill();}const g=oc.createRadialGradient(cl.cx,cl.cy,0,cl.cx,cl.cy,cl.r*1.4);g.addColorStop(0,`rgba(180,200,255,0.07)`);g.addColorStop(1,'rgba(180,200,255,0)');oc.beginPath();oc.arc(cl.cx,cl.cy,cl.r*1.4,0,Math.PI*2);oc.fillStyle=g;oc.fill();});const galaxies=[{x:W*0.08,y:H*0.40,rx:28,ry:10,ang:0.4,a:0.28},{x:W*0.92,y:H*0.55,rx:20,ry:7,ang:-0.3,a:0.22},{x:W*0.35,y:H*0.88,rx:22,ry:6,ang:0.8,a:0.20},{x:W*0.68,y:H*0.08,rx:18,ry:5,ang:0.1,a:0.24},{x:W*0.82,y:H*0.82,rx:25,ry:8,ang:-0.6,a:0.19},{x:W*0.15,y:H*0.78,rx:16,ry:5,ang:0.5,a:0.18},];galaxies.forEach(g=>{oc.save();oc.translate(g.x,g.y);oc.rotate(g.ang);const gr=oc.createRadialGradient(0,0,0,0,0,g.rx);gr.addColorStop(0,`rgba(220,235,255,${g.a})`);gr.addColorStop(0.35,`rgba(200,220,255,${g.a*0.5})`);gr.addColorStop(1,'rgba(200,215,255,0)');oc.scale(1,g.ry/g.rx);oc.beginPath();oc.ellipse(0,0,g.rx,g.rx,0,0,Math.PI*2);oc.fillStyle=gr;oc.fill();for(let i=0;i<60;i++){const sr=Math.random()*g.rx*0.8,sa=Math.random()*Math.PI*2;oc.beginPath();oc.arc(sr*Math.cos(sa),sr*Math.sin(sa),0.4,0,Math.PI*2);oc.fillStyle=`rgba(230,240,255,${(Math.random()*0.6+0.2).toFixed(2)})`;oc.fill();}oc.restore();});}const SCOLS=['rgba(255,255,255,','rgba(160,225,248,','rgba(188,206,255,','rgba(215,248,255,','rgba(255,235,200,'];function mkStar(){return{x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.6+.14,a:Math.random()*.72+.05,da:(Math.random()*.009+.002)*(Math.random()<.5?1:-1),sp:Math.random()*.04+.004,ang:Math.random()*Math.PI*2,dr:(Math.random()-.5)*.009,col:SCOLS[Math.floor(Math.random()*SCOLS.length)]};}function mkShoot(){const y=Math.random()*H*.55;return{x:-24,y,vx:Math.random()*11+5,vy:Math.random()*3.8+.5,len:Math.random()*185+80,a:1};}function mkNebDust(){return{x:Math.random()*W,y:Math.random()*H,r:Math.random()*.65+.1,a:Math.random()*.09+.02,hue:158+Math.random()*62,sp:Math.random()*.015+.002,ang:Math.random()*Math.PI*2,dr:(Math.random()-.5)*.004};}for(let i=0;i<340;i++)stars.push(mkStar());for(let i=0;i<100;i++)nebDust.push(mkNebDust());let fr=0;function draw(){ctx.clearRect(0,0,W,H);if(offscreen)ctx.drawImage(offscreen,0,0);for(const s of nebDust){s.ang+=s.dr;s.x+=Math.cos(s.ang)*s.sp;s.y+=Math.sin(s.ang)*s.sp;if(s.x<-2)s.x=W+2;if(s.x>W+2)s.x=-2;if(s.y<-2)s.y=H+2;if(s.y>H+2)s.y=-2;ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);ctx.fillStyle=`hsla(${s.hue},78%,68%,${s.a.toFixed(2)})`;ctx.fill();}for(const s of stars){s.a+=s.da;if(s.a>.80)s.da=-Math.abs(s.da);if(s.a<.04)s.da=Math.abs(s.da);s.ang+=s.dr;s.x+=Math.cos(s.ang)*s.sp;s.y+=Math.sin(s.ang)*s.sp;if(s.x<-2)s.x=W+2;if(s.x>W+2)s.x=-2;if(s.y<-2)s.y=H+2;if(s.y>H+2)s.y=-2;ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);ctx.fillStyle=`${s.col}${s.a.toFixed(2)})`;ctx.fill();}if(fr%260===0)shoots.push(mkShoot());for(let i=shoots.length-1;i>=0;i--){const s=shoots[i];s.x+=s.vx;s.y+=s.vy;s.a-=.011;if(s.a<=0){shoots.splice(i,1);continue}const g=ctx.createLinearGradient(s.x-s.len,s.y-(s.vy/s.vx)*s.len,s.x,s.y);g.addColorStop(0,'rgba(255,255,255,0)');g.addColorStop(.6,`rgba(155,238,255,${(s.a*.58).toFixed(2)})`);g.addColorStop(1,`rgba(255,255,255,${s.a.toFixed(2)})`);ctx.beginPath();ctx.moveTo(s.x-s.len,s.y-(s.vy/s.vx)*s.len);ctx.lineTo(s.x,s.y);ctx.strokeStyle=g;ctx.lineWidth=1.3;ctx.stroke();}fr++;requestAnimationFrame(draw);}draw();})();
(function(){const d=document.getElementById('dust');for(let i=0;i<30;i++){const p=document.createElement('div');p.className='dp';const sz=Math.random()*2.2+.4;p.style.cssText=`width:${sz}px;height:${sz}px;left:${Math.random()*100}%;bottom:-10px;--dx:${(Math.random()-.5)*220}px;animation-duration:${Math.random()*38+22}s;animation-delay:-${Math.random()*38}s;opacity:${Math.random()*.45+.12}`;d.appendChild(p);}})();

document.querySelectorAll('.tilt').forEach(card=>{const isV=card.classList.contains('vcard');const maxR=isV?10:9;card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect();const dx=(e.clientX-r.left-r.width/2)/(r.width/2);const dy=(e.clientY-r.top-r.height/2)/(r.height/2);card.style.transform=`perspective(900px) rotateY(${dx*maxR}deg) rotateX(${-dy*maxR*.8}deg) translateZ(12px) scale(1.022)`;const sh=card.querySelector('.pcard-shine');if(sh){const px=((dx+1)/2*100).toFixed(1),py=((dy+1)/2*100).toFixed(1);sh.style.background=`radial-gradient(ellipse at ${px}% ${py}%,rgba(255,255,255,.09) 0%,transparent 55%)`}});card.addEventListener('mouseleave',()=>{card.style.transform='';const sh=card.querySelector('.pcard-shine');if(sh)sh.style.background='';});});
const io=new IntersectionObserver(en=>{en.forEach(e=>{if(!e.isIntersecting)return;const d=parseFloat(e.target.style.getPropertyValue('--delay')||'0')*350;setTimeout(()=>e.target.classList.add('vis'),d);io.unobserve(e.target);});},{threshold:.12});document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
function drawConst(){const svg=document.getElementById('constelSvg');const cards=document.querySelectorAll('#pgrid .pcard');if(cards.length<2)return;svg.innerHTML='';const sr=svg.getBoundingClientRect();svg.setAttribute('viewBox',`0 0 ${sr.width} ${sr.height}`);svg.style.cssText='position:absolute;inset:0;width:100%;height:100%';const cs=Array.from(cards).map(c=>{const r=c.getBoundingClientRect();return{x:r.left-sr.left+r.width/2,y:r.top-sr.top+r.height/2}});[[0,1],[1,2],[3,4],[4,5],[1,4],[0,3],[2,5],[0,4]].forEach(([a,b])=>{if(!cs[a]||!cs[b])return;const ln=document.createElementNS('http://www.w3.org/2000/svg','line');ln.setAttribute('x1',cs[a].x);ln.setAttribute('y1',cs[a].y);ln.setAttribute('x2',cs[b].x);ln.setAttribute('y2',cs[b].y);svg.appendChild(ln);});}window.addEventListener('load',()=>setTimeout(drawConst,500));window.addEventListener('resize',()=>setTimeout(drawConst,300));
document.querySelectorAll('.pcard[data-src]').forEach(c=>{c.addEventListener('click',()=>{document.getElementById('lbimg').src=c.dataset.src;document.getElementById('lb').classList.add('on')});});const lb=document.getElementById('lb');document.getElementById('lbx').addEventListener('click',()=>lb.classList.remove('on'));lb.addEventListener('click',e=>{if(e.target===lb)lb.classList.remove('on')});document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('on')});

(function(){
  // 1. Fetch Thumbnails for facades
  document.querySelectorAll('.vcard[data-vimeo]').forEach(card => {
    const videoId = card.dataset.vimeo;
    const facade = card.querySelector('.video-facade');
    if (facade && videoId) {
      fetch('https://vimeo.com/api/v2/video/' + videoId + '.json')
        .then(response => response.json())
        .then(data => {
          if(data[0] && data[0].thumbnail_large) {
            facade.style.backgroundImage = 'url(' + data[0].thumbnail_large + ')';
            facade.style.backgroundSize = 'cover';
            facade.style.backgroundPosition = 'center';
          }
        }).catch(err => console.log('Thumbnail error', err));
    }
  });

  // 2. Lightbox Logic with Auto-close
  const vlb = document.getElementById('vlb');
  const vlbFrame = document.getElementById('vlb-iframe');
  const vlbX = document.getElementById('vlbx');
  let vimeoPlayer = null;

  function closeVideo() {
    vlb.classList.remove('on');
    vlbFrame.src = '';
    document.body.style.overflow = '';
    if (vimeoPlayer) {
      vimeoPlayer.off('ended');
      vimeoPlayer = null;
    }
  }

  function openVideo(id) {
    // Load iframe with API enabled
    vlbFrame.src = 'https://player.vimeo.com/video/' + id + '?autoplay=1&color=00756c&title=0&byline=0&portrait=0&api=1';
    vlb.classList.add('on');
    document.body.style.overflow = 'hidden';
    
    // Initialize Vimeo Player and listen for 'ended' event
    setTimeout(() => {
      vimeoPlayer = new Vimeo.Player(vlbFrame);
      vimeoPlayer.on('ended', () => {
        closeVideo();
      });
    }, 300); // Slight delay to ensure iframe is loaded
  }

  // 3. Attach click events to all cards
  document.querySelectorAll('.vcard[data-vimeo]').forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', (e) => {
      e.preventDefault();
      openVideo(card.dataset.vimeo);
    });
  });

  vlbX.addEventListener('click', closeVideo);
  vlb.addEventListener('click', e => { if (e.target === vlb) closeVideo(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeVideo(); });
})();
</script>
<script src="https://player.vimeo.com/api/player.js"></script>
</body>
</html>
