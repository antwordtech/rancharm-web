files = ['dashboard.html', 'leaderboard.html', 'marketplace.html', 'my-ranch.html', 'profile.html', 'ranch-store.html', 'referrals.html']

old = '<a class="drawer-link" href="leaderboard.html"><i class="fa-solid fa-ranking-star"></i>Leaderboard</a>'
new = '<a class="drawer-link" href="leaderboard.html"><i class="fa-solid fa-ranking-star"></i>Leaderboard</a>\n  <a class="drawer-link" href="transactions.html"><i class="fa-solid fa-receipt"></i>Transactions</a>'

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c
    if old not in c:
        print(fname, 'PATTERN NOT FOUND - check manually')
        continue
    c = c.replace(old, new)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')
