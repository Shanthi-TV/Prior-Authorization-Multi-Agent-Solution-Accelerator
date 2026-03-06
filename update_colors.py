import re

with open('docs/images/readme/solution-architecture.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# Replace Box colors
# ACA Frontend (Next.js)
svg = svg.replace('<g transform="translate(288, 260)">\n    <rect width="460" height="90" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>',
                  '<g transform="translate(288, 260)">\n    <rect width="460" height="90" fill="#E1F0FA" stroke="#0078D4" stroke-width="1.5" rx="4"/>')
# ACA Backend (FastAPI)
svg = svg.replace('<g transform="translate(288, 420)">\n    <rect width="460" height="100" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>',
                  '<g transform="translate(288, 420)">\n    <rect width="460" height="100" fill="#E1F0FA" stroke="#0078D4" stroke-width="1.5" rx="4"/>')
# ACA Audit PDF
svg = svg.replace('<g transform="translate(288, 600)">\n    <rect width="215" height="140" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>',
                  '<g transform="translate(288, 600)">\n    <rect width="215" height="140" fill="#E1F0FA" stroke="#0078D4" stroke-width="1.5" rx="4"/>')
# App Insights
svg = svg.replace('<g transform="translate(533, 600)">\n    <rect width="215" height="140" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>',
                  '<g transform="translate(533, 600)">\n    <rect width="215" height="140" fill="#FFF4CE" stroke="#D83B01" stroke-width="1.5" rx="4"/>')

# Foundry Services (Purple)
svg = svg.replace('<g transform="translate(858, 250)">\n    <rect width="632" height="220" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>',
                  '<g transform="translate(858, 250)">\n    <rect width="632" height="220" fill="#F3E8FF" stroke="#5B4BDB" stroke-width="1.5" rx="4"/>')
svg = svg.replace('<g transform="translate(858, 500)">\n    <rect width="292" height="140" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>',
                  '<g transform="translate(858, 500)">\n    <rect width="292" height="140" fill="#F3E8FF" stroke="#5B4BDB" stroke-width="1.5" rx="4"/>')
svg = svg.replace('<g transform="translate(1182, 500)">\n    <rect width="308" height="140" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>',
                  '<g transform="translate(1182, 500)">\n    <rect width="308" height="140" fill="#F3E8FF" stroke="#5B4BDB" stroke-width="1.5" rx="4"/>')

# Inner Foundry agent boxes
svg = svg.replace('fill="#F3F2F1"', 'fill="#E6D8FF" stroke="#7E62EC" stroke-width="1" rx="2"', 4)

# External Tools boxes green
svg = svg.replace('<rect x="250" y="15" width="150" height="40" fill="#F3F2F1"/>', '<rect x="250" y="15" width="150" height="40" fill="#E6F4EA" stroke="#0B6A0B" stroke-width="1.5" rx="3"/>')
svg = svg.replace('<rect x="420" y="15" width="150" height="40" fill="#F3F2F1"/>', '<rect x="420" y="15" width="150" height="40" fill="#E6F4EA" stroke="#0B6A0B" stroke-width="1.5" rx="3"/>')
svg = svg.replace('<rect x="590" y="15" width="150" height="40" fill="#F3F2F1"/>', '<rect x="590" y="15" width="150" height="40" fill="#E6F4EA" stroke="#0B6A0B" stroke-width="1.5" rx="3"/>')
svg = svg.replace('<rect x="760" y="15" width="150" height="40" fill="#F3F2F1"/>', '<rect x="760" y="15" width="150" height="40" fill=\"#E6F4EA\" stroke=\"#0B6A0B\" stroke-width="1.5" rx=\"3\"/>') # Fix inner quotes if needed

# Payer / Reviewer boxes
svg = svg.replace('<rect width="146" height="80" fill="#FFFFFF" stroke="#D2D0CE" stroke-width="1"/>', '<rect width="146" height="80" fill="#F0F6FF" stroke="#0078D4" stroke-width="1.5" rx="6"/>')

# Cloud backgrounds
svg = svg.replace('<rect x="36" y="116" width="1528" height="836" rx="0" fill="#FAFAFA" stroke="#0078D4" stroke-width="2" stroke-dasharray="10 5"/>',
                  '<rect x="36" y="116" width="1528" height="836" rx="12" fill="#FAFAFA" stroke="#0078D4" stroke-width="2" stroke-dasharray="8 6"/>')

with open('docs/images/readme/solution-architecture.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
