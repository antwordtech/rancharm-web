with open('dashboard.html') as f:
    c = f.read()
before = c

old_markup = '''  <a class="drawer-link" href="subscription.html"><i class="fa-solid fa-crown"></i>Subscription</a>

  <div class="drawer-link" style="cursor:pointer;" onclick="toggleTheme()">'''

new_markup = '''  <a class="drawer-link" href="subscription.html"><i class="fa-solid fa-crown"></i>Subscription</a>
  <a class="drawer-link" href="admin-dashboard.html" id="adminLink" style="display:none;"><i class="fa-solid fa-shield-halved"></i>Admin</a>

  <div class="drawer-link" style="cursor:pointer;" onclick="toggleTheme()">'''

if old_markup not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

old_import = "import { auth, getUserProfile, getOrCreateWallet, ANIMALS } from './firebase-config.js?v=3';"
new_import = "import { auth, getUserProfile, getOrCreateWallet, isAdmin, ANIMALS } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT PATTERN NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_js = '''    document.getElementById('drawerTier').textContent = animal.name + ' \\u00b7 Ranch Level';

    document.body.classList.add('ready');'''
new_js = '''    document.getElementById('drawerTier').textContent = animal.name + ' \\u00b7 Ranch Level';

    if (isAdmin(user)) {
      document.getElementById('adminLink').style.display = 'flex';
    }

    document.body.classList.add('ready');'''
if old_js not in c:
    print('JS PATTERN NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
