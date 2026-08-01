with open('firebase-config.js') as f:
    c = f.read()
before = c

old = '''  if (code) {
    const q = query(collection(db, "users"), where("referralCode", "==", code));
    const snap = await getDocs(q);
    if (!snap.empty) {
      referredBy = snap.docs[0].id;
      await updateDoc(doc(db, "users", referredBy), { referralCount: increment(1) });
    }
  }'''

new = '''  if (code) {
    const q = query(collection(db, "users"), where("referralCode", "==", code));
    const snap = await getDocs(q);
    if (!snap.empty) {
      const referrerDoc = snap.docs[0];
      referredBy = referrerDoc.id;
      const referrerData = referrerDoc.data();
      const referrerAnimal = ANIMALS.find(a => a.key === (referrerData.animalTier || "cock"));
      const capacity = referrerAnimal ? referrerAnimal.teamCapacity : 5;
      const currentCount = referrerData.referralCount || 0;
      if (currentCount < capacity) {
        await updateDoc(doc(db, "users", referredBy), { referralCount: increment(1) });
      }
    }
  }'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
else:
    c = c.replace(old, new)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
