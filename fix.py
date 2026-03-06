import re, os, base64

svg_path = 'docs/images/readme/solution-architecture.svg'
with open(svg_path, 'r', encoding='utf-8') as f:
    text = f.read()

def swap(m):
    fname = m.group(1)
    fpath = os.path.join('docs/images/readme', fname)
    if os.path.exists(fpath):
        with open(fpath, 'rb') as fp:
            d = base64.b64encode(fp.read()).decode()
            mime = 'image/png' if fname.endswith('.png') else 'image/svg+xml'
            return 'href=\"data:' + mime + ';base64,' + d + '\"'
    return m.group(0)

# Replace 'href="FileName.png"' (ignoring data: and # anchors)
text = re.sub(r'href=\"([^#d][^\"]+\.(?:png|svg))\"', swap, text)
with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
