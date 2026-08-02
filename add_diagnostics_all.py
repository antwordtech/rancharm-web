files = ["admin-dashboard.html", "admin-kyc.html", "admin-tasks.html",
         "complete-profile.html", "dashboard.html", "index.html", "kyc.html",
         "leaderboard.html", "login.html", "marketplace.html", "my-ranch.html",
         "profile.html", "ranch-store.html", "referrals.html", "tasks.html"]

diagnostic = '''<script>
function showPageError(msg) {
  var loader = document.getElementById('pageLoader');
  if (!loader) { console.error('Page error:', msg); return; }
  loader.innerHTML = '<div style="text-align:center;padding:24px;max-width:320px;">' +
    '<div style="color:#f43f5e;font-weight:800;margin-bottom:10px;font-size:15px;">Page Error</div>' +
    '<div style="font-size:12px;color:var(--text-dim);word-break:break-word;">' + msg + '</div></div>';
  loader.style.opacity = '1';
  loader.style.pointerEvents = 'auto';
}
window.addEventListener('error', function(e) {
  showPageError((e.message || 'Unknown error') + (e.filename ? ' (' + e.filename.split('/').pop() + ':' + e.lineno + ')' : ''));
});
window.addEventListener('unhandledrejection', function(e) {
  var msg = (e.reason && e.reason.message) ? e.reason.message : String(e.reason);
  showPageError(msg);
});
</script>
'''

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c
    marker = '<script src="toast.js?v=2"></script>'
    if marker in c:
        c = c.replace(marker, marker + '\n' + diagnostic, 1)
    else:
        print(fname, 'MARKER NOT FOUND - check manually')
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')

print("DONE")
