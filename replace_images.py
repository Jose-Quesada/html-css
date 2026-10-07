import os
import re
import glob
from pathlib import Path
import urllib.parse

def replace_image_url(match):
    full_url = match.group(1)
    
    # Check if it's already an absolute URL
    if full_url.startswith("http://") or full_url.startswith("https://") or full_url.startswith("data:"):
        return match.group(0)
    
    # Check if it's an image
    ext = full_url.split(".")[-1].lower()
    if ext not in ["jpg", "jpeg", "png", "gif", "webp", "svg"]:
        return match.group(0)
    
    filename = full_url.split("/")[-1]
    
    # Try to guess size from filename or use default
    width, height = 800, 600
    if "400" in filename:
        width, height = 400, 300
    elif "1200" in filename:
        width, height = 1200, 400
    elif "avatar" in filename or "icono" in filename or "logo" in filename or "papelera" in filename:
        width, height = 200, 200
        
    encoded_filename = urllib.parse.quote_plus(filename)
    new_url = f"https://dummyimage.com/{width}x{height}/ccc/000.png&text={encoded_filename}"
    
    return match.group(0).replace(full_url, new_url)

def replace_srcset(match):
    # match.group(1) is the whole content of srcset="..."
    content = match.group(1)
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
        if ext not in ["jpg", "jpeg", "png", "gif", "webp", "svg"]:
            new_parts.append(part)
            continue
            
        filename = img_url.split("/")[-1]
        width, height = 800, 600
        if "400" in filename:
            width, height = 400, 300
        elif "1200" in filename:
            width, height = 1200, 400
            
        encoded_filename = urllib.parse.quote_plus(filename)
        new_url = f"https://dummyimage.com/{width}x{height}/ccc/000.png&text={encoded_filename}"
        
        new_part = part.replace(img_url, new_url)
        new_parts.append(new_part)
        
    return 'srcset="' + ', '.join(new_parts) + '"'

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python replace_images.py <dir1> [<dir2> ...]")
        return
        
    for arg in sys.argv[1:]:
        target_dir = Path(arg)
        if not target_dir.exists():
            print(f"Directory not found: {target_dir}")
            continue
            
        for file_path in target_dir.rglob("*.md"):
            content = file_path.read_text(encoding="utf-8")
            
            # Replace src="..."
            new_content = re.sub(r'src="([^"]+)"', replace_image_url, content)
            
            # Replace srcset="..."
            new_content = re.sub(r'srcset="([^"]+)"', replace_srcset, new_content)
            
            # Also replace poster="..." for videos
            new_content = re.sub(r'poster="([^"]+)"', replace_image_url, new_content)
            
            if content != new_content:
                print(f"Updated {file_path}")
                file_path.write_text(new_content, encoding="utf-8")

if __name__ == "__main__":
    main()
