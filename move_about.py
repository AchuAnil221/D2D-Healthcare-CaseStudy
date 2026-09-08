import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update CSS
content = content.replace('.about-inner .stmt-caption', '.impact-inner .stmt-caption')
content = content.replace('.about-inner .stmt-tags', '.impact-inner .stmt-tags')
content = content.replace('.about-inner .stmt-tag', '.impact-inner .stmt-tag')
# Make text legible on dark background
content = content.replace('color:rgba(8,15,30,0.7);\n      line-height:1.65;', 'color:rgba(255,255,255,0.7);\n      line-height:1.65;\n      margin: 0 auto; text-align: center;')
# Make sure tags container is centered
content = content.replace('display:flex; justify-content:center; gap:16px;', 'display:flex; justify-content:center; gap:16px;')

# 2. Extract content from s-about and remove s-about
about_match = re.search(r'<!-- [═]+ \n     07\.5 · ABOUT.*?<div class="about-inner">\n(.*?)</div>\n</section>', content, re.DOTALL)
if about_match:
    about_content = about_match.group(1)
    content = content.replace(about_match.group(0), '')
    
    # 3. Insert into s-impact
    impact_target = r'(<h2 class="impact-h2">.*?</h2>)'
    content = re.sub(impact_target, r'\1\n' + about_content, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
