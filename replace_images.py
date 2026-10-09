import os
import re
import glob
from pathlib import Path
import urllib.parse

IMAGE_EXTS = {"jpg", "jpeg", "png", "gif", "webp", "avif", "svg", "ico"}

def get_dummy_url(img_url):
    filename = img_url.split("/")[-1]
    width, height = 800, 600
    if "400" in filename:
        width, height = 400, 300
    elif "1200" in filename:
        width, height = 1200, 400
    elif any(kw in filename.lower() for kw in ["avatar", "icono", "logo", "papelera", "favicon"]):
        width, height = 200, 200
        
    encoded_filename = urllib.parse.quote_plus(filename)
    return f"https://dummyimage.com/{width}x{height}/ccc/000.png&text={encoded_filename}"

def replace_simple_url(match):
    attr = match.group(1) # src, poster, href, etc
    quote = match.group(2)
    img_url = match.group(3)
    
    if img_url.startswith("http://") or img_url.startswith("https://") or img_url.startswith("data:"):
        return match.group(0)
        
    ext = img_url.split(".")[-1].lower()
    if ext not in IMAGE_EXTS:
        return match.group(0)
        
    new_url = get_dummy_url(img_url)
    return f'{attr}={quote}{new_url}{quote}'

def replace_css_url(match):
    quote = match.group(1)
    img_url = match.group(2)
    
    if img_url.startswith("http://") or img_url.startswith("https://") or img_url.startswith("data:"):
        return match.group(0)
        
    ext = img_url.split(".")[-1].lower()
    if ext not in IMAGE_EXTS:
        return match.group(0)
        
    new_url = get_dummy_url(img_url)
    return f'url({quote}{new_url}{quote})'

def replace_srcset(match):
    quote = match.group(1)
    content = match.group(2)
    
    parts = content.split(",")
    new_parts = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
            
        tokens = part.split(" ")
        img_url = tokens[0]
        
        if img_url.startswith("http://") or img_url.startswith("https://") or img_url.startswith("data:"):
            new_parts.append(part)
            continue
            
        ext = img_url.split(".")[-1].lower()
        if ext not in IMAGE_EXTS:
            new_parts.append(part)
            continue
            
        new_url = get_dummy_url(img_url)
        new_part = part.replace(img_url, new_url)
        new_parts.append(new_part)
        
    return 'srcset=' + quote + ', '.join(new_parts) + quote

def main():
    import sys
    
    dirs = sys.argv[1:]
    if not dirs:
        dirs = [
            "docs/html", 
            "docs/css", 
            "E:/00. Clases/Apuntes/Desarrollo_Interfaces", 
            "E:/00. Clases/Apuntes/Diseño interfaces"
        ]
        
    for arg in dirs:
        target_dir = Path(arg)
        if not target_dir.exists():
            print(f"Directory not found: {target_dir}")
            continue
            
        for file_path in target_dir.rglob("*.md"):
            content = file_path.read_text(encoding="utf-8")
            
            # Replace src, poster, href
            # matches: attr="url" or attr='url'
            new_content = re.sub(r'\b(src|poster|href)=(["\'])([^"\']+?\.(?:jpg|jpeg|png|gif|webp|avif|svg|ico))\2', replace_simple_url, content, flags=re.IGNORECASE)
            
            # Replace css url()
            # matches: url("...") or url('...') or url(...)
            new_content = re.sub(r'url\((["\']?)([^)"\']+?\.(?:jpg|jpeg|png|gif|webp|avif|svg|ico))\1\)', replace_css_url, new_content, flags=re.IGNORECASE)
            
            # Replace srcset
            new_content = re.sub(r'\bsrcset=(["\'])(.*?)\1', replace_srcset, new_content, flags=re.IGNORECASE)
            
            if content != new_content:
                print(f"Updated {file_path}")
                file_path.write_text(new_content, encoding="utf-8")

if __name__ == "__main__":
    main()
