import re
from pathlib import Path

MEDIA_MAP = {
    "mp4": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4",
    "webm": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm",
    "ogv": "https://www.w3schools.com/html/mov_bbb.ogg",
    "mp3": "https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3",
    "ogg": "https://www.w3schools.com/html/horse.ogg",
    "vtt": "https://interactive-examples.mdn.mozilla.net/media/examples/friday.vtt"
}

def replace_media_url(match):
    attr = match.group(1) # src or href
    quote = match.group(2) # " or '
    url = match.group(3)
    
    if url.startswith("http://") or url.startswith("https://") or url.startswith("data:"):
        return match.group(0)
        
    ext = url.split(".")[-1].lower()
    if ext in MEDIA_MAP:
        return f'{attr}={quote}{MEDIA_MAP[ext]}{quote}'
        
    return match.group(0)

def process_file(file_path):
    content = file_path.read_text(encoding="utf-8")
    
    # Matches src="..." or href="..." ending in media extensions
    pattern = r'\b(src|href)=(["\'])([^"\']+?\.(?:mp4|webm|ogv|ogg|mp3|wav|vtt))\2'
    new_content = re.sub(pattern, replace_media_url, content, flags=re.IGNORECASE)
    
    if content != new_content:
        print(f"Updated media in {file_path}")
        file_path.write_text(new_content, encoding="utf-8")

def main():
    dirs = [
        Path("docs/html"),
        Path("docs/css"),
        Path("E:/00. Clases/Apuntes/Desarrollo_Interfaces"),
        Path("E:/00. Clases/Apuntes/Diseño interfaces"),
        Path("E:/00. Clases/Apuntes/Presentaciones")
    ]
    for d in dirs:
        if not d.exists():
            continue
        for md in d.rglob("*.md"):
            process_file(md)

if __name__ == "__main__":
    main()
