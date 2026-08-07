files = ['airtime.html', 'data.html', 'utility.html', 'booster.html', 'ecg.html', 'water.html', 'withdraw.html']

old = 'uid: currentUser.uid,'
new = 'uid: currentUser.uid,\n          idToken: await currentUser.getIdToken(),'

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c
    if old not in c:
        print(fname, 'PATTERN NOT FOUND - check manually')
        continue
    c = c.replace(old, new, 1)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')
