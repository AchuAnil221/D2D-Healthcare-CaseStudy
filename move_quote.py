import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update max-width in CSS
content = re.sub(r'color:#fff; max-width:900px;', r'color:#fff; max-width:100%;', content)
content = re.sub(r'font-size: 1.45rem; color: rgba\(255,255,255,0.7\); line-height: 1.6; max-width: 720px;\s*margin-bottom: 80px;', r'font-size: 1.45rem; color: rgba(255,255,255,0.7); line-height: 1.6; max-width: 100%;', content)

# Also add s-footer to CSS
footer_css = """
    .s-footer {
      background:var(--bg);
      padding: 40px var(--sp);
      display: flex;
      justify-content: center;
    }
    .s-footer .outro-inner { max-width:1280px; width:100%; }
"""
content = re.sub(r'/\* ─+ \*/\s*</style>', footer_css + '\n</style>', content)

# 2. Re-arrange HTML
# Find the s-outro block
outro_match = re.search(r'<!-- ═+ \n     08 · OUTRO\n ═+ -->\n<section class="s-outro".*?</section>', content, re.DOTALL)
if outro_match:
    outro_html = outro_match.group(0)
    # Remove from original location
    content = content.replace(outro_html, '')
    
    # Split the outro into quote block and footer block
    quote_html = re.sub(r'<div class="outro-bottom">.*?</div>', '', outro_html, flags=re.DOTALL)
    quote_html = re.sub(r'\s+</div>\n</section>', '\n  </div>\n</section>', quote_html) # cleanup spacing
    
    footer_bottom_match = re.search(r'<div class="outro-bottom">.*?</div>', outro_html, re.DOTALL)
    if footer_bottom_match:
        footer_inner = footer_bottom_match.group(0)
        footer_html = f"""
<!-- ════════════════════════════════════════════════════════════
     09 · FOOTER
═══════════════════════════════════════════════════════════════ -->
<footer class="s-footer">
  <div class="outro-inner">
    {footer_inner}
  </div>
</footer>
"""
        # Place footer after s-impact
        content = re.sub(r'(<section class="s-impact".*?</section>)', r'\1\n' + footer_html, content, flags=re.DOTALL)
        
        # Place the quote block (s-outro) after s-tech
        content = re.sub(r'(<section class="s-tech".*?</section>)', r'\1\n\n' + quote_html, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
