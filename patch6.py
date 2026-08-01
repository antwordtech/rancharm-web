# 1) FIX THE REAL BUG: firebase-config.js never exported arrayUnion, breaking tasks.html
with open('firebase-config.js') as f:
    c = f.read()
before = c
c = c.replace(
    'increment, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";',
    'increment, arrayUnion, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";'
)
c = c.replace(
    'export { doc, getDoc, setDoc, updateDoc, increment, collection, query, where, getDocs, orderBy, limit };',
    'export { doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit };'
)
with open('firebase-config.js', 'w') as f:
    f.write(c)
print('firebase-config.js', "FIXED (arrayUnion now exported)" if c != before else "NO CHANGE - check manually, bug may still exist")

# 2) Bump firebase-config.js cache version everywhere so browsers pick up the fix
all_files = ["login.html","complete-profile.html","dashboard.html","ranch-store.html","my-ranch.html","tasks.html","referrals.html","profile.html","leaderboard.html"]
for fname in all_files:
    with open(fname) as f:
        c = f.read()
    before = c
    c = c.replace("firebase-config.js?v=2", "firebase-config.js?v=3")
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, "version bumped" if c != before else "no v=2 reference found")

# 3) Replace hamburger with a back arrow on every authenticated page except dashboard
back_files = ["ranch-store.html","my-ranch.html","tasks.html","referrals.html","profile.html","leaderboard.html"]
old_icon_btn = '<button class="icon-btn" onclick="openDrawer()"><i class="fa-solid fa-bars"></i></button>'
new_icon_btn = "<button class=\"icon-btn\" onclick=\"window.location.href='dashboard.html'\"><i class=\"fa-solid fa-arrow-left\"></i></button>"

for fname in back_files:
    with open(fname) as f:
        c = f.read()
    before = c
    c = c.replace(old_icon_btn, new_icon_btn)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, "back arrow applied" if c != before else "NO CHANGE - check manually")

print("DONE")
