with open('index.html') as f:
    c = f.read()
before = c

replacements = [
    ('max-width:320px;margin:0 auto;', 'width:min(90%,340px);margin:0 auto;'),
    ('max-width:400px;margin:0 auto;padding:0 20px;', 'width:min(94%,600px);margin:0 auto;padding:0 20px;'),
    ('max-width:500px;margin:0 auto 24px;padding:0 20px;', 'width:min(94%,700px);margin:0 auto 24px;padding:0 20px;'),
    ('max-width:340px;margin:8px auto 40px;padding:0 20px;', 'width:min(90%,340px);margin:8px auto 40px;padding:0 20px;'),
]

for old, new in replacements:
    if old not in c:
        print('MISSING:', old)
    c = c.replace(old, new)

with open('index.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
