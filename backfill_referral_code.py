with open('referrals.html') as f:
    c = f.read()
before = c

old_import = "import { auth, getUserProfile, ANIMALS, getTeamLevel } from './firebase-config.js?v=3';"
new_import = "import { auth, db, doc, updateDoc, getUserProfile, ANIMALS, getTeamLevel } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_line = "    document.getElementById('referralCode').textContent = profile.referralCode || '--------';"
new_line = '''    if (!profile.referralCode) {
      profile.referralCode = user.uid.substring(0, 8).toUpperCase();
      await updateDoc(doc(db, "users", user.uid), { referralCode: profile.referralCode });
    }
    document.getElementById('referralCode').textContent = profile.referralCode || '--------';'''
if old_line not in c:
    print('LINE NOT FOUND - check manually')
c = c.replace(old_line, new_line)

with open('referrals.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
