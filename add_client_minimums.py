with open('ecg.html') as f:
    c = f.read()
before = c

old = "if (!amount || Number(amount) <= 0) { toast('Enter a valid amount', 'error'); return; }"
new = "if (!amount || Number(amount) < 5) { toast('Minimum top-up is GHS 5', 'error'); return; }"

if old not in c:
    print('ECG PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('ecg.html', 'w') as f:
    f.write(c)
print('ecg.html', 'OK' if c != before else 'NO CHANGE')

with open('water.html') as f:
    c2 = f.read()
before2 = c2

old2 = "if (!amount || Number(amount) <= 0) { toast('Enter a valid amount', 'error'); return; }"
new2 = "if (!amount || Number(amount) < 1) { toast('Minimum payment is GHS 1', 'error'); return; }"

if old2 not in c2:
    print('WATER PATTERN NOT FOUND - check manually')
c2 = c2.replace(old2, new2)

with open('water.html', 'w') as f:
    f.write(c2)
print('water.html', 'OK' if c2 != before2 else 'NO CHANGE')
