import re

with open('docs/images/readme/solution-architecture.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# We want the three images. I'll print their bounding rects and positions.
# They are the ones with widths 36, 50, 50.
pattern = r'<image\s+(href="[^"]+")\s+(x="\d+"\s+y="\d+"\s+width="\d+"\s+height="\d+"\s+preserveAspectRatio="[^"]+")'
for m in re.finditer(r'<image.*?x="(\d+)".*?y="(\d+)".*?width="(\d+)".*?>', text):
    start = max(0, m.start() - 150)
    end = min(len(text), m.end() + 150)
    context = text[start:m.start()] + "<IMAGE>" + text[m.end():end]
    print(f"Image at {m.group(1)},{m.group(2)} ({m.group(3)}w)")
    print(context)
    print("-" * 40)
