import re

def simple_markdown_to_html(markdown):
    """Convert basic markdown to HTML"""
    lines = markdown.split('\n')
    html_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        # Lists
        elif line.startswith('- '):
            if html_lines and html_lines[-1] == '<ul>':
                html_lines.append(f'<li>{line[2:]}</li>')
            else:
                html_lines.append('<ul>')
                html_lines.append(f'<li>{line[2:]}</li>')
        elif line.startswith('1. '):
            if html_lines and html_lines[-1] == '<ol>':
                html_lines.append(f'<li>{line[3:]}</li>')
            else:
                html_lines.append('<ol>')
                html_lines.append(f'<li>{line[3:]}</li>')
        # Blockquote
        elif line.startswith('> '):
            html_lines.append(f'<blockquote>{line[2:]}</blockquote>')
        # Code block
        elif line.startswith('```'):
            html_lines.append('<pre><code>')
        elif line == '```':
            html_lines.append('</code></pre>')
        # Paragraph
        else:
            # Simple inline formatting
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            line = re.sub(r'_(.*?)_', r'<i>\1</i>', line)
            line = re.sub(r'`(.*?)`', r'<code>\1</code>', line)
            line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', line)
            line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)
            html_lines.append(f'<p>{line}</p>')
    
    # Close any open lists
    if html_lines and html_lines[-1] in ['<ul>', '<ol>']:
        html_lines.append('</ul>' if html_lines[-1] == '<ul>' else '</ol>')
    
    return '\n'.join(html_lines)
