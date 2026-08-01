with open('ranch-store.html') as f:
    c = f.read()
before = c

old = '''        <div class="animal-detail-price">${animal.price === 0 ? 'Free' : 'GHS ' + animal.price.toLocaleString()}</div>
        <div class="animal-benefits">${benefitsHtml}</div>'''

new = '''        <div class="animal-detail-price">${animal.price === 0 ? 'Free' : 'GHS ' + animal.price.toLocaleString()}</div>
        <div style="font-size:13px;font-weight:700;color:var(--brand-dark);margin-bottom:12px;"><i class="fa-solid fa-coins" style="margin-right:6px;"></i>Earn ${animal.dailyPoints.toLocaleString()} pts/day</div>
        <div class="animal-benefits">${benefitsHtml}</div>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('ranch-store.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
