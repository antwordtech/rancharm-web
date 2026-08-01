files = ["complete-profile.html", "dashboard.html", "index.html", "kyc.html",
         "leaderboard.html", "login.html", "marketplace.html", "my-ranch.html",
         "profile.html", "ranch-store.html", "referrals.html", "tasks.html"]

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c

    # Generic placeholder-dash fixes (safe everywhere)
    c = c.replace(">—</div>", ">...</div>")
    c = c.replace("|| '—';", "|| '...';")
    c = c.replace('|| "—";', '|| "...";')

    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'placeholder pass:', 'changed' if c != before else 'no change')

# File-specific sentence-level fixes
specific = {
    "complete-profile.html": [
        ("One last step — complete your profile", "One last step: complete your profile"),
        ("Required — used for account verification", "Required for account verification"),
    ],
    "index.html": [
        ("Rancharm — Grow Your Ranch, Earn Real Rewards", "Rancharm: Grow Your Ranch, Earn Real Rewards"),
        ("first Ranch animal — free, no payment needed.", "first Ranch animal, free with no payment needed."),
        ("feed it — the bigger the animal, the bigger the reward.", "feed it. The bigger the animal, the bigger the reward."),
    ],
    "leaderboard.html": [
        ("No rankings yet — be the first to earn points!", "No rankings yet. Be the first to earn points!"),
    ],
    "login.html": [
        ("Required — used for account verification", "Required for account verification"),
    ],
    "referrals.html": [
        ("Team full — <a", "Team full. <a"),
    ],
    "tasks.html": [
        ("right now — check back soon.", "right now. Check back soon."),
    ],
}

for fname, pairs in specific.items():
    with open(fname) as f:
        c = f.read()
    before = c
    for old, new in pairs:
        if old not in c:
            print(fname, 'MISSING:', old)
        c = c.replace(old, new)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'sentence pass:', 'changed' if c != before else 'no change')

print("DONE")
