with open('utility.html') as f:
    c = f.read()
before = c

old = '''      <div class="id-type-option" data-value="BROADBAND" onclick="selectService(this)">
        <div class="id-type-option-name">Telecel Broadband</div>
      </div>
'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, '')

with open('utility.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
