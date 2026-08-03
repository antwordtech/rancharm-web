with open('data.html') as f:
    c = f.read()
before = c

old = '  window.buyBundle = async function(bundleId, price) {'
new = '''  window.buyBundleClick = function(btn) {
    const id = btn.dataset.bundleId;
    const price = parseFloat(btn.dataset.bundlePrice);
    buyBundle(id, price);
  };

  async function buyBundle(bundleId, price) {'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

# Also fix the closing brace style since buyBundle is no longer `window.buyBundle = async function...` (arrow-style close with `};` stays fine as a function declaration too)
with open('data.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
