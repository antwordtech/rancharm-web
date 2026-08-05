with open('subscription.html') as f:
    c = f.read()
before = c

old_import = "import { auth, getUserProfile, SUBSCRIPTIONS } from './firebase-config.js?v=3';"
new_import = "import { auth, db, doc, updateDoc, getUserProfile, SUBSCRIPTIONS } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_click = '''  window.subscribeClick = (btn) => {
    const key = btn.dataset.subKey;
    window.location.href = 'checkout.html?type=subscription&key=' + key;
  };'''

new_click = '''  window.subscribeClick = async (btn) => {
    const key = btn.dataset.subKey;

    if (key === 'free') {
      btn.disabled = true;
      btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
      try {
        await updateDoc(doc(db, "users", auth.currentUser.uid), { subscriptionTier: 'free' });
        toast('Downgraded to Free plan', 'success');
        setTimeout(function() { window.location.reload(); }, 1000);
      } catch (e) {
        toast('Something went wrong. Try again.', 'error');
        btn.disabled = false;
        btn.innerHTML = 'Subscribe';
      }
      return;
    }

    window.location.href = 'checkout.html?type=subscription&key=' + key;
  };'''

if old_click not in c:
    print('CLICK NOT FOUND - check manually')
c = c.replace(old_click, new_click)

with open('subscription.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
