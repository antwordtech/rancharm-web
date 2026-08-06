with open('admin-tasks.html') as f:
    c = f.read()
before = c

old = '''    if (!title || !pointsReward) { toast('Title and points reward are required', 'error'); return; }'''

new = '''    if (!title || !pointsReward) { toast('Title and points reward are required', 'error'); return; }
    if (link && link.toLowerCase().includes('rancharm.com')) { toast('Destination link cannot point to rancharm.com', 'error'); return; }'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('admin-tasks.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
