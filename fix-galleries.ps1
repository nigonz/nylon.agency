$files = @("galeria2.rely.html", "galeria2.cf.html", "galeria2.zan.html")

$headBlock = @"
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nylon | Sintonía Perfecta</title>
    <!-- Importación estricta de tipografías híbridas -->
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Playfair+Display:wght@400;600;700;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
"@

$headerBlock = @"
    <header style="text-align: center; margin-top: 120px;">
        <h1 class="brand-title" style="font-family: 'Playfair Display', serif !important;">SINTONÍA PERFECTA</h1>
        <h2 style="font-family: 'Space Grotesk', sans-serif !important; font-size: 1rem; letter-spacing: 6px; color: var(--cyan); margin-top: 10px; text-transform: uppercase;">
            // FRECUENCIA COMPARTIDA
        </h2>
    </header>
"@

$cssBlock = @"
        /* =========================================
           SISTEMA DE GALERÍA ESTRICTO
        ========================================= */
        .vgrid {
            display: grid !important;
            grid-template-columns: repeat(3, 1fr) !important;
            max-width: 1000px;
            margin: 0 auto;
            gap: 30px;
            align-items: start;
        }

        .vcard {
            width: 100%;
            max-width: 280px;
            margin: 0 auto;
            border-radius: 16px;
            overflow: hidden;
            background: #000;
        }

        /* Fuerza la simetría vertical sin importar el tipo de video */
        .vframe {
            position: relative;
            width: 100%;
            aspect-ratio: 9/16 !important; 
            overflow: hidden;
        }

        .vframe iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* Responsivo */
        @media (max-width: 900px) {
            .vgrid { grid-template-columns: repeat(2, 1fr) !important; }
        }
        @media (max-width: 600px) {
            .vgrid { grid-template-columns: 1fr !important; }
            .vcard { max-width: 85vw; }
        }
"@

foreach ($f in $files) {
    if (Test-Path $f) {
        $content = Get-Content $f -Raw
        
        # Replace <head> to <style>
        $content = $content -replace '(?s)<head>.*?(?=<style>)', "$headBlock`r`n    "
        
        # Replace <header>
        $content = $content -replace '(?s)<header(?:>| [^>]*>).*?</header>', $headerBlock
        
        # Remove old CSS for .vgrid, .vcard, .vframe simply by replacing
        $content = $content -replace '(?s)\.vgrid\s*\{[^}]*\}', ''
        $content = $content -replace '(?s)\.vcard\s*\{[^}]*\}', ''
        $content = $content -replace '(?s)\.vframe\s*\{[^}]*\}', ''
        $content = $content -replace '(?s)\.vframe\s+iframe\s*\{[^}]*\}', ''
        # We also need to strip it out of media queries, which is harder. 
        # But we can just inject the new css with !important at the very end of style block.
        
        $content = $content -replace '(?s)\s*</style>', "`r`n$cssBlock`r`n    </style>"
        
        Set-Content $f $content -NoNewline
    }
}
