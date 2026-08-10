$files = Get-ChildItem -Filter galeria2.*.html
$vlbCss = @"
/* ── VIDEO LIGHTBOX ── */
#vlb {
  position:fixed;inset:0;z-index:3000;
  background:rgba(1,1,8,.96);
  display:none;align-items:center;justify-content:center;
  backdrop-filter:blur(28px);
  -webkit-backdrop-filter:blur(28px);
}
#vlb.on { display:flex; }
#vlb-inner {
  position:relative;
  width:min(900px,92vw);
  aspect-ratio:16/9;
  border-radius:18px;overflow:hidden;
  box-shadow:0 40px 100px rgba(0,0,0,.95),0 0 60px rgba(26,143,160,.35),0 0 120px rgba(0,180,200,.14);
  animation:vlb-in .45s cubic-bezier(.22,1,.36,1);
}
#vlb-inner.vertical { aspect-ratio:4/5; width:min(700px,82vw); }
@media(orientation:landscape){
  #vlb-inner { aspect-ratio:16/9; width:min(1100px,92vw); }
}
@keyframes vlb-in{from{opacity:0;transform:scale(.88) translateY(22px)}to{opacity:1;transform:none}}
#vlb-iframe {
  position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:18px;
}
.vlb-x {
  position:fixed;top:22px;right:26px;
  width:48px;height:48px;border-radius:50%;
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);
  display:flex;align-items:center;justify-content:center;
  font-size:22px;color:#fff;cursor:pointer;z-index:3010;
  transition:background .2s,border-color .2s,transform .2s;
}
.vlb-x:hover{background:rgba(26,143,160,.35);border-color:var(--teal);transform:rotate(90deg)}

/* Overlay play sobre tarjeta */
.vcard-overlay {
  position:absolute;inset:0;z-index:20;cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  background:transparent;
  transition:background .3s;
}
.vcard-overlay:hover { background:rgba(0,0,0,.25); }
.vcard-play {
  width:68px;height:68px;border-radius:50%;
  background:rgba(26,143,160,.85);
  border:2px solid rgba(255,255,255,.4);
  backdrop-filter:blur(10px);
  display:flex;align-items:center;justify-content:center;
  opacity:0;transform:scale(.7);
  transition:opacity .3s,transform .3s,box-shadow .3s;
  box-shadow:0 0 0 0 rgba(26,143,160,.5);
  pointer-events:none;
}
.vcard-play svg { fill:#fff; width:24px; height:24px; margin-left:4px; }
.vcard-overlay:hover .vcard-play {
  opacity:1;transform:scale(1);
  box-shadow:0 0 30px rgba(26,143,160,.7),0 0 65px rgba(0,200,220,.3);
}
"@

$vlbHtml = @"
<!-- VIDEO LIGHTBOX -->
<div id="vlb">
  <div class="vlb-x" id="vlbx">✕</div>
  <div id="vlb-inner">
    <iframe id="vlb-iframe" src="" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>
"@

$vlbJs = @"

/* ═══════════════════════════════════════════
   VIDEO LIGHTBOX
═══════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
  const vlb = document.getElementById('vlb');
  const vlbIframe = document.getElementById('vlb-iframe');
  const vlbx = document.getElementById('vlbx');
  const inner = document.getElementById('vlb-inner');
  if(!vlb) return;

  function closeVlb() {
    vlb.classList.remove('on');
    vlbIframe.src = '';
  }
  vlbx.addEventListener('click', closeVlb);
  vlb.addEventListener('click', (e) => {
    if(e.target === vlb) closeVlb();
  });

  document.querySelectorAll('.vcard[data-vimeo]').forEach(card => {
    card.addEventListener('click', () => {
      const vid = card.getAttribute('data-vimeo');
      const hash = card.getAttribute('data-hash');
      const ratio = card.getAttribute('data-ratio');
      if(ratio && ratio.includes('16') && ratio.startsWith('9')) {
        inner.classList.add('vertical');
      } else {
        inner.classList.remove('vertical');
      }
      let url = 'https://player.vimeo.com/video/' + vid + '?autoplay=1&badge=0&autopause=0';
      if(hash) url += '&h=' + hash;
      vlbIframe.src = url;
      vlb.classList.add('on');
    });
  });

  // OEmbed para miniaturas de videos con hash
  document.querySelectorAll('.vcard[data-vimeo][data-hash]').forEach(async card => {
    const vid = card.getAttribute('data-vimeo');
    const hash = card.getAttribute('data-hash');
    const img = card.querySelector('img');
    if(!img) return;
    try {
      const res = await fetch(`https://vimeo.com/api/oembed.json?url=https://vimeo.com/${vid}/${hash}`);
      const data = await res.json();
      if(data.thumbnail_url) {
        img.src = data.thumbnail_url;
      }
    } catch(e) { console.error('Error cargando miniatura:', e); }
  });
});
"@

foreach ($file in $files) {
    Write-Host "Procesando $($file.Name)..."
    $content = Get-Content $file.FullName -Raw -Encoding UTF8

    # 1. Insert CSS before </style>
    if ($content -notmatch 'VIDEO LIGHTBOX') {
        $content = $content -replace '(?s)</style>', "`n$vlbCss`n</style>"
    }

    # 2. Insert HTML before <main> (or if no main, before <script)
    if ($content -notmatch 'id="vlb"') {
        if ($content -match '<main') {
            $content = $content -replace '(?s)(<main)', "`n$vlbHtml`n`$1"
        } else {
            $content = $content -replace '(?s)(<script)', "`n$vlbHtml`n`$1"
        }
    }

    # 3. Insert JS before </body>
    if ($content -notmatch 'closeVlb') {
        $content = $content -replace '(?s)</body>', "`n$vlbJs`n</body>"
    }

    # 4. Replace iframe inside .vcard with new vcard structure
    # Matches: <div class="vcard"> <div class="vframe"> <iframe src="...video/123456?..." ...></iframe> </div> </div>
    $pattern = '(?s)<div class="vcard">\s*<div class="vframe">\s*<iframe src="[^"]*?video/(\d+)\?[^"]*?"[^>]*?title="([^"]*)"[^>]*></iframe>\s*</div>\s*</div>'
    $content = [regex]::Replace($content, $pattern, {
        param($match)
        $vid = $match.Groups[1].Value
        $title = $match.Groups[2].Value
        # Determine format/ratio - by default we'll make all gallery vertical 4/5 as requested recently, or just 16/9
        $ratio = "16/9" # If needed they can be vertical. But since we don't know, we use a standard. Actually they are car videos mostly horizontal.
        return @"
<div class="vcard" data-vimeo="$vid" data-ratio="$ratio">
    <div class="vframe">
        <img src="https://vumbnail.com/$vid.jpg" alt="$title" style="width:100%;height:100%;object-fit:cover;display:block;">
    </div>
    <div class="vcard-overlay">
        <div class="vcard-play"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
    </div>
</div>
"@
    })

    [IO.File]::WriteAllText($file.FullName, $content, [Text.Encoding]::UTF8)
}
Write-Host "Done!"
