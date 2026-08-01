with open('subscription.html') as f:
    c = f.read()
before = c

# Add error diagnostic (same as kyc.html) right after toast.js
c = c.replace(
    '<script src="toast.js?v=2"></script>\n</head>',
    '''<script src="toast.js?v=2"></script>
<script>
function showPageError(msg) {
  var loader = document.getElementById('pageLoader');
  if (!loader) return;
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
</head>'''
)

# Fix the malformed escaping in the Subscribe button (was producing literal backslashes, not quotes)
old_btn = '''(isCurrent ? '<div class="current-badge">Current Plan</div>' : '<button onclick="subscribe(\\'' + sub.key + '\\')">Subscribe</button>');'''
new_btn = '''(isCurrent ? '<div class="current-badge">Current Plan</div>' : '<button class="btn-small" data-sub-key="' + sub.key + '" onclick="subscribeClick(this)">Subscribe</button>');'''
if old_btn not in c:
    print('BUTTON PATTERN NOT FOUND - check manually')
c = c.replace(old_btn, new_btn)

# Add a helper that reads the key from data-attribute instead of inline string interpolation
c = c.replace(
    '''  window.subscribe = (key) => {
    toast('Subscription payments coming later (deposit on hold for now)');
  };''',
    '''  window.subscribeClick = (btn) => {
    toast('Subscription payments coming later (deposit on hold for now)');
  };'''
)

with open('subscription.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
