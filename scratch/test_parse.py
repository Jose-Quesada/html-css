with open('site/css/practicas-posicionamiento-flexbox-grid-canvas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

canvases = soup.find_all('canvas')
print('Found canvases count:', len(canvases))
for i, c in enumerate(canvases):
    print(f'Canvas {i}: id={c.get("id")} parent={c.parent.name} class={c.parent.get("class")}')
