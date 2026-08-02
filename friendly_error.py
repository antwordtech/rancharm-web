files = ["admin-dashboard.html", "admin-kyc.html", "admin-tasks.html",
         "complete-profile.html", "dashboard.html", "kyc.html",
         "leaderboard.html", "login.html", "marketplace.html", "my-ranch.html",
         "profile.html", "ranch-store.html", "referrals.html", "tasks.html"]

old_fn = """function showPageError(msg) {
  var loader = document.getElementById('pageLoader');
  if (!loader) { console.error('Page error:', msg); return; }
  loader.innerHTML = '<div style="text-align:center;padding:24px;max-width:320px;">' +
    '<div style="color:#f43f5e;font-weight:800;margin-bottom:10px;font-size:15px;">Page Error</div>' +
    '<div style="font-size:12px;color:var(--text-dim);word-break:break-word;">' + msg + '</div></div>';
  loader.style.opacity = '1';
  loader.style.pointerEvents = 'auto';
}"""

new_fn = """function showPageError(msg) {
  console.error('Page error:', msg);
  var loader = document.getElementById('pageLoader');
  if (!loader) return;
  loader.innerHTML = '<div style="text-align:center;padding:24px;max-width:320px;">' +
    '<i class="fa-solid fa-cloud-arrow-down" style="font-size:32px;color:var(--brand);margin-bottom:14px;display:block;"></i>' +
    '<div style="font-weight:800;font-size:16px;margin-bottom:8px;">Having Trouble Loading</div>' +
    '<div style="font-size:13px;color:var(--text-dim);margin-bottom:18px;">Check your internet connection and try again.</div>' +
    '<button onclick="location.reload()" style="width:auto;padding:10px 20px;">Retry</button></div>';
  loader.style.opacity = '1';
  loader.style.pointerEvents = 'auto';
}"""

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c
    if old_fn not in c:
        print(fname, 'PATTERN NOT FOUND - check manually')
    c = c.replace(old_fn, new_fn)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')

print("DONE")
