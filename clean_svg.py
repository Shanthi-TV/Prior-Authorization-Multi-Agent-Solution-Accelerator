import re
import os
import base64

def b64_svg(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        svg_content = f.read().encode("utf-8")
    d = base64.b64encode(svg_content).decode('ascii')
    return f'data:image/svg+xml;base64,{d}'

with open('docs/images/readme/solution-architecture.svg', 'r', encoding='utf-8') as f:
    text = f.read()

def repl(m):
    href = m.group(1)
    attrs = m.group(2)
    
    if 'Azure-Container-Apps' in href or 'iVBORw0KGgoAAAANSUhEUgAAB1M' in href[:200]:
        new_href = b64_svg('docs/images/readme/Azure-Container-Apps-Logo.svg')
    elif 'application-insight' in href or 'application-insight' in attrs:
        # If it's the app insights one, let's embed it from PNG as it's fairly small (28KB)
        with open('docs/images/readme/application-insight.png', 'rb') as f_in:
            d = base64.b64encode(f_in.read()).decode('ascii')
        new_href = f'data:image/png;base64,{d}'
    else:
        if 'y="584"' in attrs:
            # app insights fallback
            with open('docs/images/readme/application-insight.png', 'rb') as f_in:
                d = base64.b64encode(f_in.read()).decode('ascii')
            new_href = f'data:image/png;base64,{d}'
        elif len(href) > 1000000:
            new_href = b64_svg('docs/images/readme/Foundry Agent Service - Color.svg')
        elif 'Foundry' in href or 'width="20"' in attrs or 'width="18"' in attrs:
            new_href = b64_svg('docs/images/readme/Foundry Agent Service - Color.svg')
        else:
            new_href = href # fallback

    return f'<image href="{new_href}"{attrs}>'

out = re.sub(r'<image\s+href="([^"]+)"([^>]+)>', repl, text)

# ACA logo 1
out = re.sub(r'<image href="([^"]+)"\s+x="320"\s+y="160"\s+width="36"\s+height="36"\s+preserveAspectRatio="xMidYMid meet"/>',
             r'<image href="\1" x="194" y="159" width="38" height="38" preserveAspectRatio="xMidYMid meet"/>', out)

out = out.replace('<text x="208" y="181"', '<text x="240" y="181"')
out = out.replace('<text x="208" y="198"', '<text x="240" y="198"')

# ACA logo 2 (Next.js)
out = re.sub(r'<image href="([^"]+)"\s+x="240"\s+y="338"\s+width="50"\s+height="50"',
             r'<image href="\1" x="263" y="342" width="40" height="40"', out)

# ACA logo 3 (API Layer)
out = re.sub(r'<image href="([^"]+)"\s+x="396"\s+y="230"\s+width="50"\s+height="50"\s+preserveAspectRatio="xMidYMid meet"/>',
             r'<image href="\1" x="416" y="271" width="40" height="40" preserveAspectRatio="xMidYMid meet"/>', out)

# Cleanup the hidden text "FastAPI Backend Service" and "Logical backend boundary" entirely so it's clean
out = re.sub(r'<text[^>]+>FastAPI Backend Service</text>', '', out)
out = re.sub(r'<text[^>]+>Logical backend boundary</text>', '', out)

with open('docs/images/readme/solution-architecture.svg', 'w', encoding='utf-8') as f:
    f.write(out)

print(f"Cleaned up file. Size: {len(out)} bytes. (was {len(text)} bytes)")
