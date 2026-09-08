import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove empty comment blocks in the script
script_comments = re.findall(r'/\* ╌+.*?╌+ \*/', content, re.DOTALL)
for comment in script_comments:
    # If the comment is followed closely by another comment or by nothing but spaces/newlines until end or another comment,
    # or we can just run a generic cleanup in the script section
    pass

# We will just use regex to clean up the script block:
# Look for comment blocks that are immediately followed by another comment block (with only whitespace between them)
# and remove the first one.
for _ in range(5):
    content = re.sub(r'/\* ╌+[^/]+╌+ \*/\s*(?=(/\* ╌+|</script>))', '', content, flags=re.DOTALL)

# 2. Remove unused IDs from HTML elements
# These IDs were previously used by GSAP, which we just deleted.
unused_ids = [
    'heroClientLabel', 'heroH1', 'heroDescCol', 'heroFooter',
    'stmtLargeImg', 'stmtEyebrow', 'stmtText', 'stmtCards',
    'techTitle', 'techIntro', 'techEyebrow', 'techList',
    'impEyebrow', 'impTitle', 'mb1', 'mb2', 'mb3',
    'whyEyebrow', 'visionText', 'outroH', 'outroBottom',
    'stmtCaption', 'stmtTags'
]

for uid in unused_ids:
    content = re.sub(r' id="' + uid + r'"', '', content)

# 3. Clean up empty lines in the script block
# Replace 3 or more newlines with 2 newlines
content = re.sub(r'\n{3,}', '\n\n', content)

with open('index.html', 'w') as f:
    f.write(content)
