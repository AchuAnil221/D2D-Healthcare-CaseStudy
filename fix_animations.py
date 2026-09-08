import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove opacity:0 and its transform
content = re.sub(r'opacity:0;\s*transform:[^;]+;', '', content)
content = re.sub(r'opacity:0;', '', content)

# Remove GSAP animations involving opacity:0 or opacity:1
# (But preserve parallax like scrub ones which don't have opacity in them)

# Remove gsap.from and gsap.to that include 'opacity:0' or 'opacity:1'
content = re.sub(r'gsap\.(from|to|fromTo)\([^\{]+\{[^\}]*opacity:\s*(0|1)[^\}]*\}\s*(?:,\s*\{[^\}]*\})?\s*\);', '', content)
# For loops like: ['sel', 'sel'].forEach((sel, i) => { gsap.from(...) });
# We can remove the lines that have gsap.from or gsap.to with opacity
lines = content.split('\n')
new_lines = []
skip_next = 0
for i, line in enumerate(lines):
    if skip_next > 0:
        skip_next -= 1
        continue
        
    if 'gsap.from' in line or 'gsap.to' in line:
        if 'opacity' in line:
            continue # skip this line
            
    if 'forEach' in line and 'gsap.from' in lines[i+1] and 'opacity' in lines[i+1]:
        # skip this and next 2 lines (forEach, gsap, }); )
        if '});' in lines[i+2] or '})' in lines[i+2]:
            skip_next = 2
            continue

    if 'forEach' in line and 'gsap.to' in lines[i+1] and 'opacity' in lines[i+1]:
        if '});' in lines[i+2] or '})' in lines[i+2]:
            skip_next = 2
            continue

    new_lines.append(line)

with open('index.html', 'w') as f:
    f.write('\n'.join(new_lines))
