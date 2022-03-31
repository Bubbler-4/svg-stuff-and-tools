#!/usr/bin/env python
inpt = open('input.txt').read().split('\n')
rows = len(inpt)
cols = max(len(row) for row in inpt)
inpt = [row.ljust(cols) for row in inpt]
print(f'<svg xmlns="http://www.w3.org/2000/svg" width="{cols}" height="{rows}">')
defs = '''
  <defs>
    <rect id="t" width="1" height="1" fill="#ffc0c0" />
    <rect id="v" width="1" height="1" fill="#ffffc0" />
    <rect id="r" width="1" height="1" fill="#c0ffc0" />
    <rect id="s" width="1" height="1" fill="#c0ffff" />
    <rect id="q" width="1" height="1" fill="#c0c0ff" />
    <rect id="u" width="1" height="1" fill="#ffc0ff" />
    
    <rect id="l" width="1" height="1" fill="#ff0000" />
    <rect id="n" width="1" height="1" fill="#ffff00" />
    <rect id="j" width="1" height="1" fill="#00ff00" />
    <rect id="k" width="1" height="1" fill="#00ffff" />
    <rect id="i" width="1" height="1" fill="#0000ff" />
    <rect id="m" width="1" height="1" fill="#ff00ff" />
    
    <rect id="d" width="1" height="1" fill="#c00000" />
    <rect id="f" width="1" height="1" fill="#c0c000" />
    <rect id="b" width="1" height="1" fill="#00c000" />
    <rect id="c" width="1" height="1" fill="#00c0c0" />
    <rect id="a" width="1" height="1" fill="#0000c0" />
    <rect id="e" width="1" height="1" fill="#c000c0" />
    
    <rect id="B" width="1" height="1" fill="#000000" />
    <rect id="W" width="1" height="1" fill="#ffffff" />
  </defs>
'''
print(defs)
for r in range(rows):
    for c in range(cols):
        ch = inpt[r][c]
        ch = {' ': 'B', '?': 'W'}.get(ch, ch)
        print(f'  <use x="{c}" y="{r}" href="#{ch}" />')
print('</svg>')