with open('booster.html') as f:
    c = f.read()
before = c

old = '''      const data = await res.json();
      quotePrice = data.price || (data.data && data.data.price) || data.cost || data.total || 0;

      if (!quotePrice) { toast('Could not get a quote for this quantity', 'error'); return; }

      document.getElementById('quotePrice').textContent = 'GHS ' + quotePrice;
      document.getElementById('quotePoints').textContent = 'Costs ' + Math.round(quotePrice * 100).toLocaleString() + ' points';'''

new = '''      const data = await res.json();
      const basePrice = data.total_price_ghs || data.price || (data.data && data.data.price) || 0;

      if (!basePrice) { toast('Could not get a quote for this quantity', 'error'); return; }

      quotePrice = Math.round((basePrice + 5) * 100) / 100;

      document.getElementById('quotePrice').textContent = 'GHS ' + quotePrice;
      document.getElementById('quotePoints').textContent = 'Costs ' + Math.round(quotePrice * 100).toLocaleString() + ' points';'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('booster.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
