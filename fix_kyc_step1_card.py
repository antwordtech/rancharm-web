with open('kyc.html') as f:
    c = f.read()
before = c

old = '<div class="profile-card" style="margin-bottom:16px;">'
new = '<div style="margin-bottom:16px;">'

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('kyc.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
