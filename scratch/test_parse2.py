from html.parser import HTMLParser

class TagTracker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tag_stack = []
        self.canvas_count = 0
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'canvas':
            self.canvas_count += 1
            print(f"Canvas #{self.canvas_count} opened! Stack depth: {len(self.tag_stack)}, id: {attrs_dict.get('id')}, stack top: {self.tag_stack[-3:] if len(self.tag_stack) >= 3 else self.tag_stack}")
        self.tag_stack.append(tag)
        
    def handle_endtag(self, tag):
        if tag == 'canvas':
            print(f"Canvas closed! Stack depth before pop: {len(self.tag_stack)}")
        if self.tag_stack:
            self.tag_stack.pop()

with open('site/css/practicas-posicionamiento-flexbox-grid-canvas/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tracker = TagTracker()
tracker.feed(html)
