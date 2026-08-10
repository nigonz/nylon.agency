$template = Get-Content ".\galeria2.html" -Raw -Encoding UTF8

# Define the galleries and their videos
$galleries = @{
    "peugeot" = @( @{ vid="1209347459"; ratio="16/9"; title="DR VF" } )
    "rely" = @( 
        @{ vid="1209347295"; ratio="16/9"; title="Video 1" },
        @{ vid="1209347295"; ratio="16/9"; title="Video 2" },
        @{ vid="1209347295"; ratio="16/9"; title="Video 3" }
    )
    "zan" = @( @{ vid="1209349371"; ratio="16/9"; title="DR VF" } )
    "cf" = @( @{ vid="1209349077"; ratio="16/9"; title="DR VF" } )
}

foreach ($gal in $galleries.GetEnumerator()) {
    $name = $gal.Key
    $vids = $gal.Value
    
    $content = $template
    
    # We find the .vgrid block and replace its contents.
    # The template has a section with class="vsec". We'll replace everything inside <div class="vgrid">...</div>
    
    $vgridStartIndex = $content.IndexOf('<div class="vgrid">')
    $vgridEndIndex = $content.IndexOf('</div>', $content.IndexOf('<!-- FIN DE LA GALERIA -->', $vgridStartIndex))
    if ($vgridEndIndex -eq -1) {
        $vgridEndIndex = $content.IndexOf('</div>', $content.IndexOf('</section>', $vgridStartIndex) - 20)
    }
    
    # Just to be safer with regex, let's replace the whole section
    $pattern = '(?s)<section class="vsec".*?</section>'
    
    $replacement = "<section class=`"vsec`" style=`"padding-top: 30px; padding-bottom: 100px;`">`n"
    
    if ($name -eq "peugeot") {
        $replacement += "    <div style=`"max-width: 900px; margin: 0 auto;`">`n"
        $aspect = "16/9"
    } else {
        $replacement += "    <div class=`"vgrid`">`n"
        $aspect = "4/5"
    }
    
    $delay = 0
    $fa = "a"
    foreach ($v in $vids) {
        $vid = $v.vid
        $ratio = $v.ratio
        $title = $v.title
        
        $replacement += @"
        <div class="fw" style="--delay:${delay}s;--dur:6.8s;--fa:float-${fa}">
            <div class="vcard" data-vimeo="$vid" data-ratio="$ratio">
                <div class="vframe" style="aspect-ratio: ${aspect} !important; border-radius: 20px;">
                    <img src="https://vumbnail.com/${vid}.jpg" alt="$title" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;display:block;">
                </div>
                <div class="vcard-overlay">
                    <div class="vcard-play"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
                </div>
            </div>
        </div>
"@ + "`n"
        $delay += 0.65
        if ($fa -eq "a") { $fa = "b" } else { $fa = "a" }
    }
    
    $replacement += "    </div>`n</section>"
    
    $content = [regex]::Replace($content, $pattern, $replacement)
    
    if ($name -eq "peugeot") {
        # Also remove max-width constraints in Peugeot
        $content = $content -replace '\.vcard\s*\{\s*max-width:\s*310px;[^}]*\}', '.vcard { margin: 0 auto; width: 100%; }'
        $content = $content -replace '\.vcard \{ max-width: 75vw; \}', '.vcard { max-width: 92vw; }'
    }
    
    $outFile = ".\galeria2.${name}.html"
    [IO.File]::WriteAllText($outFile, $content, [Text.Encoding]::UTF8)
    Write-Host "Rebuilt $outFile"
}
