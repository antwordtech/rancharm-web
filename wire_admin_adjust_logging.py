with open('admin-users.html') as f:
    c = f.read()
before = c

old_import = "import { auth, db, doc, updateDoc, increment, isAdmin, ANIMALS, collection, getDocs } from './firebase-config.js?v=3';"
new_import = "import { auth, db, doc, updateDoc, increment, addDoc, isAdmin, ANIMALS, collection, getDocs } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_fn = '''    btn.disabled = true;
    try {
      await updateDoc(doc(db, "wallets", uid), { points: increment(sign * amount) });
      toast(sign > 0 ? 'Points added' : 'Points deducted', 'success');
      await loadUsers();'''
new_fn = '''    btn.disabled = true;
    try {
      await Promise.all([
        updateDoc(doc(db, "wallets", uid), { points: increment(sign * amount) }),
        addDoc(collection(db, "transactions"), {
          uid: uid,
          type: "admin_adjustment",
          amount: sign * amount,
          description: sign > 0 ? "Admin added points" : "Admin deducted points",
          createdAt: Date.now()
        })
      ]);
      toast(sign > 0 ? 'Points added' : 'Points deducted', 'success');
      await loadUsers();'''
if old_fn not in c:
    print('FUNCTION NOT FOUND - check manually')
c = c.replace(old_fn, new_fn)

with open('admin-users.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
