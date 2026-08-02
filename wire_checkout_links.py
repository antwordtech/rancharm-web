with open('ranch-store.html') as f:
    c = f.read()
before = c

old = """  window.buyAnimal = (key) => {
    toast('Payment flow for ' + key + ' coming later (deposit on hold for now)');
  };"""

new = """  window.buyAnimal = (key) => {
    window.location.href = 'checkout.html?type=animal&key=' + key;
  };"""

if old not in c:
    print('ranch-store.html PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('ranch-store.html', 'w') as f:
    f.write(c)
print('ranch-store.html', 'OK' if c != before else 'NO CHANGE')

with open('subscription.html') as f:
    c2 = f.read()
before2 = c2

old2 = """  window.subscribeClick = (btn) => {
    toast('Subscription payments coming later (deposit on hold for now)');
  };"""

new2 = """  window.subscribeClick = (btn) => {
    const key = btn.dataset.subKey;
    window.location.href = 'checkout.html?type=subscription&key=' + key;
  };"""

if old2 not in c2:
    print('subscription.html PATTERN NOT FOUND - check manually')
c2 = c2.replace(old2, new2)

with open('subscription.html', 'w') as f:
    f.write(c2)
print('subscription.html', 'OK' if c2 != before2 else 'NO CHANGE')
