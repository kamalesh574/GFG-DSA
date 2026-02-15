import os
import math

easy = medium = hard = 0

for root, dirs, files in os.walk("problems"):
    for d in dirs:
        name = d.lower()
        if "easy" in name:
            easy += 1
        elif "medium" in name:
            medium += 1
        elif "hard" in name:
            hard += 1

total = easy + medium + hard

def percent(x):
    return 0 if total == 0 else int((x/total)*100)

easy_p = percent(easy)
medium_p = percent(medium)
hard_p = percent(hard)

radius = 45
circumference = 2 * math.pi * radius
progress = 0 if total == 0 else min(1, total / 100)
offset = circumference * (1 - progress)

svg = f"""
<svg width="700" height="250" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0d1117" rx="20"/>

  <text x="30" y="40" fill="#58a6ff" font-size="24" font-family="Segoe UI">
    GeeksforGeeks Dashboard
  </text>

  <circle cx="120" cy="140" r="{radius}" stroke="#30363d" stroke-width="10" fill="none"/>
  <circle cx="120" cy="140" r="{radius}" stroke="#3fb950" stroke-width="10"
    fill="none"
    stroke-dasharray="{circumference}"
    stroke-dashoffset="{offset}"
    transform="rotate(-90 120 140)"/>

  <text x="120" y="145" fill="#ffffff" font-size="24" text-anchor="middle">
    {total}
  </text>
  <text x="120" y="170" fill="#8b949e" font-size="12" text-anchor="middle">
    Solved
  </text>

  <text x="250" y="110" fill="#3fb950" font-size="18">Easy: {easy}</text>
  <rect x="250" y="120" width="350" height="10" fill="#30363d" rx="5"/>
  <rect x="250" y="120" width="{3.5*easy_p}" height="10" fill="#3fb950" rx="5"/>

  <text x="250" y="150" fill="#d29922" font-size="18">Medium: {medium}</text>
  <rect x="250" y="160" width="350" height="10" fill="#30363d" rx="5"/>
  <rect x="250" y="160" width="{3.5*medium_p}" height="10" fill="#d29922" rx="5"/>

  <text x="250" y="190" fill="#f85149" font-size="18">Hard: {hard}</text>
  <rect x="250" y="200" width="350" height="10" fill="#30363d" rx="5"/>
  <rect x="250" y="200" width="{3.5*hard_p}" height="10" fill="#f85149" rx="5"/>
</svg>
"""

with open("gfg-dashboard.svg","w") as f:
    f.write(svg)
