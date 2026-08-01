with open('firebase-config.js') as f:
    c = f.read()
before = c

# Fix Cock's team capacity to 0 (matches "no team-building on free tier")
old_cock = 'benefits: ["Basic tasks", "Basic rewards", "Beginner access", "Starter Team"], teamCapacity: 5 }'
new_cock = 'benefits: ["Basic tasks", "Basic rewards", "Beginner access", "Starter Team"], teamCapacity: 0 }'
if old_cock not in c:
    print('COCK PATTERN NOT FOUND - check manually')
c = c.replace(old_cock, new_cock)

# Replace referral logic: pay flat points (100 Cock / 200 Duck+), still gate team-count by capacity
old_referral = '''  if (code) {
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

new_referral = '''  if (code) {
    const q = query(collection(db, "users"), where("referralCode", "==", code));
    const snap = await getDocs(q);
    if (!snap.empty) {
      const referrerDoc = snap.docs[0];
      referredBy = referrerDoc.id;
      const referrerData = referrerDoc.data();
      const referrerTier = referrerData.animalTier || "cock";
      const referrerAnimal = ANIMALS.find(a => a.key === referrerTier);
      const capacity = referrerAnimal ? referrerAnimal.teamCapacity : 0;
      const currentCount = referrerData.referralCount || 0;

      // Flat referral point reward: 100 pts if referrer is Cock, 200 pts for Duck and above.
      const rewardPoints = referrerTier === "cock" ? 100 : 200;
      await updateDoc(doc(db, "wallets", referredBy), { points: increment(rewardPoints) });

      // Team count only grows while under this tier's capacity (Cock's capacity is 0, so never grows).
      if (currentCount < capacity) {
        await updateDoc(doc(db, "users", referredBy), { referralCount: increment(1) });
      }
    }
  }'''

if old_referral not in c:
    print('REFERRAL PATTERN NOT FOUND - check manually')
c = c.replace(old_referral, new_referral)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
