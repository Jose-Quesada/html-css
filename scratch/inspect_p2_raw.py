with open('docs/css/practicas-posicionamiento-flexbox-grid.md', 'r', encoding='utf-8') as f:
    text = f.read()

pos_p2 = text.find('## Práctica 2:')
pos_p3 = text.find('## Práctica 3:')
p2_block = text[pos_p2:pos_p3]

lines = p2_block.split('\n')
print(f"Total lines in P2 block: {len(lines)}")
for idx, line in enumerate(lines[:60]):
    print(f"{idx+1:3d}: {repr(line[:40])}")
