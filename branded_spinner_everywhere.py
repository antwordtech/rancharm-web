files = ["dashboard.html", "ranch-store.html", "my-ranch.html", "tasks.html",
         "referrals.html", "profile.html", "leaderboard.html", "marketplace.html",
         "kyc.html", "subscription.html", "checkout.html", "complete-profile.html",
         "admin-dashboard.html", "admin-kyc.html", "admin-tasks.html"]

dotlottie_script = '<script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.4/dist/dotlottie-wc.js" type="module"></script>\n'
old_spinner = '<i class="fa-solid fa-spinner fa-spin" style="font-size:32px;color:var(--brand);"></i>'
new_spinner = '<dotlottie-wc src="https://lottie.host/455b3c68-8f9a-4345-b369-2fd3162bc953/Qc4CNAKTcR.json" style="width:80px;height:80px;" autoplay loop></dotlottie-wc>'

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c

    if 'dotlottie-wc.js' not in c:
        if '<link rel="stylesheet" href="styles.css?v=2">' in c:
            c = c.replace('<link rel="stylesheet" href="styles.css?v=2">',
                           dotlottie_script + '<link rel="stylesheet" href="styles.css?v=2">', 1)
        else:
            print(fname, 'NO STYLES.CSS ANCHOR - script not added, check manually')

    if old_spinner in c:
        c = c.replace(old_spinner, new_spinner)
    else:
        print(fname, 'SPINNER PATTERN NOT FOUND - check manually')

    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')

print("DONE")
