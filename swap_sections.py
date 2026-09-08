import re

with open("index.html", "r") as f:
    content = f.read()

# Define the regex to match the flowing menu section and the tech section
flowing_menu_pattern = re.compile(r"(<!-- ════════════════════════════════════════════════════════════\n     14 · FLOWING MENU.*?</section>\n)", re.DOTALL)
tech_pattern = re.compile(r"(\n<!-- ════════════════════════════════════════════════════════════\n     05 · TECHNOLOGY.*?</section>\n)", re.DOTALL)

flowing_match = flowing_menu_pattern.search(content)
tech_match = tech_pattern.search(content)

if flowing_match and tech_match:
    flowing_text = flowing_match.group(1)
    tech_text = tech_match.group(1)
    
    # We replace the concatenated original block with the swapped version
    # The original order is flowing_text + tech_text
    original_combined = flowing_text + tech_text
    new_combined = tech_text.lstrip('\n') + "\n\n" + flowing_text
    
    new_content = content.replace(original_combined, new_combined)
    
    with open("index.html", "w") as f:
        f.write(new_content)
    print("Successfully swapped sections.")
else:
    print("Could not find sections.")

