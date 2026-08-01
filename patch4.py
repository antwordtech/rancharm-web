drawer_files = ["ranch-store.html","my-ranch.html","tasks.html","referrals.html","profile.html"]

leaderboard_link = '  <a class="drawer-link" href="leaderboard.html"><i class="fa-solid fa-ranking-star"></i>Leaderboard</a>\n'
dark_mode_anchor = '  <div class="drawer-link" style="cursor:pointer;" onclick="toggleTheme()">'

for fname in drawer_files:
    with open(fname) as f:
        c = f.read()
    before = c
    c = c.replace(dark_mode_anchor, leaderboard_link + dark_mode_anchor)
    c = c.replace('<i class="fa-solid fa-moon"></i>', '<i class="fa-solid fa-circle-half-stroke"></i>')
    c = c.replace('<div class="page-loader" id="pageLoader">', '<div class="page-loader page-loader-app" id="pageLoader">')
    c = c.replace('content="#ffffff" id="metaTheme"', 'content="#0f9d8c" id="metaTheme"')
    c = c.replace("isDark ? '#0b1210' : '#ffffff'", "isDark ? '#0b1210' : '#0f9d8c'")
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, "OK" if c != before else "NO CHANGE - check manually")

for fname in ["login.html", "complete-profile.html"]:
    with open(fname) as f:
        c = f.read()
    before = c
    c = c.replace('content="#ffffff" id="metaTheme"', 'content="#0f9d8c" id="metaTheme"')
    c = c.replace("isDark ? '#0b1210' : '#ffffff'", "isDark ? '#0b1210' : '#0f9d8c'")
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, "OK" if c != before else "NO CHANGE - check manually")

with open('firebase-config.js') as f:
    c = f.read()
before = c
c = c.replace(
    'increment, collection, query, where, getDocs } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";',
    'increment, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";'
)
c = c.replace(
    'export { doc, getDoc, setDoc, updateDoc, increment, collection, query, where, getDocs };',
    'export { doc, getDoc, setDoc, updateDoc, increment, collection, query, where, getDocs, orderBy, limit };'
)
with open('firebase-config.js', 'w') as f:
    f.write(c)
print('firebase-config.js', "OK" if c != before else "NO CHANGE - check manually")

print("DONE")
