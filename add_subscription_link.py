files = ["dashboard.html", "ranch-store.html", "my-ranch.html", "tasks.html",
         "referrals.html", "profile.html", "leaderboard.html", "marketplace.html"]

anchor_active = '<a class="drawer-link active" href="marketplace.html"><i class="fa-solid fa-fire"></i>Marketplace</a>'
anchor_plain = '<a class="drawer-link" href="marketplace.html"><i class="fa-solid fa-fire"></i>Marketplace</a>'
insert = '\n  <a class="drawer-link" href="subscription.html"><i class="fa-solid fa-crown"></i>Subscription</a>'

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c
    if anchor_active in c:
        c = c.replace(anchor_active, anchor_active + insert)
    elif anchor_plain in c:
        c = c.replace(anchor_plain, anchor_plain + insert)
    else:
        print(fname, 'ANCHOR NOT FOUND - check manually')
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')

print("DONE")
