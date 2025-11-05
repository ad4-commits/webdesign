def copy_dir(src, dest):
    """Copy directory recursively from src to dest"""
    import shutil
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

# Also make sure you have these other essential functions:
def markdown_to_html(markdown):
    """Convert markdown to HTML with proper formatting"""
    import re
    # Convert headers
    html = re.sub(r'^# (.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    html = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # Convert bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)
    
    # Convert italic
    html = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html)
    html = re.sub(r'_(.*?)_', r'<i>\1</i>', html)
    
    # Convert inline code
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
    
    # Convert blockquotes
    html = re.sub(r'^> (.*)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Convert images ![alt](src)
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2">', html)
    
    # Convert links [text](url)
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    
    # Convert unordered lists
    lines = html.split('\n')
    in_ul = False
    result_lines = []
    
    for line in lines:
        if line.strip().startswith('- '):
            if not in_ul:
                result_lines.append('<ul>')
                in_ul = True
            content = line.strip()[2:]
            result_lines.append(f'<li>{content}</li>')
        else:
            if in_ul:
                result_lines.append('</ul>')
                in_ul = False
            result_lines.append(line)
    
    if in_ul:
        result_lines.append('</ul>')
    
    html = '\n'.join(result_lines)
    
    # Convert ordered lists
    lines = html.split('\n')
    in_ol = False
    result_lines = []
    
    for line in lines:
        if re.match(r'^\d+\. ', line.strip()):
            if not in_ol:
                result_lines.append('<ol>')
                in_ol = True
            content = re.sub(r'^\d+\. ', '', line.strip())
            result_lines.append(f'<li>{content}</li>')
        else:
            if in_ol:
                result_lines.append('</ol>')
                in_ol = False
            result_lines.append(line)
    
    if in_ol:
        result_lines.append('</ol>')
    
    html = '\n'.join(result_lines)
    
    # Convert paragraphs
    lines = html.split('\n')
    result_lines = []
    in_paragraph = False
    current_paragraph = []
    
    for line in lines:
        line_stripped = line.strip()
        if line_stripped == '':
            if in_paragraph and current_paragraph:
                result_lines.append('<p>' + ' '.join(current_paragraph) + '</p>')
                in_paragraph = False
                current_paragraph = []
            result_lines.append('')
        elif line_stripped.startswith(('<h1>', '<h2>', '<ul>', '<ol>', '<li>', '<blockquote>', '<a ', '<img', '</ul>', '</ol>')):
            if in_paragraph and current_paragraph:
                result_lines.append('<p>' + ' '.join(current_paragraph) + '</p>')
                current_paragraph = []
            in_paragraph = False
            result_lines.append(line)
        else:
            in_paragraph = True
            current_paragraph.append(line_stripped)
    
    if in_paragraph and current_paragraph:
        result_lines.append('<p>' + ' '.join(current_paragraph) + '</p>')
    
    html = '\n'.join(result_lines)
    
    return html

def extract_title(markdown):
    """Extract title from markdown (first h1 header)"""
    import re
    match = re.search(r'^# (.*)$', markdown, re.MULTILINE)
    if match:
        return match.group(1)
    return "Default Title"
