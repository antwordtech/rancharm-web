with open('firebase-config.js') as f:
    c = f.read()
before = c

old = '''      // Flat referral point reward: 100 pts if referrer is Cock, 200 pts for Duck and above.
      const rewardPoints = referrerTier === "cock" ? 100 : 200;
      await updateDoc(doc(db, "wallets", referredBy), { points: increment(rewardPoints) });

      // Team count only grows while under this tier's capacity (Cock's capacity is 0, so never grows).
      if (currentCount < capacity) {
        await updateDoc(doc(db, "users", referredBy), { referralCount: increment(1) });
      }'''

new = '''      // Flat referral point reward: 100 pts if referrer is Cock, 200 pts for Duck and above.
      const rewardPoints = referrerTier === "cock" ? 100 : 200;
      await updateDoc(doc(db, "wallets", referredBy), { points: increment(rewardPoints) });

      // referralCount = total people ever referred (always grows, this is "People Referred").
      await updateDoc(doc(db, "users", referredBy), { referralCount: increment(1) });

      // teamCount = active team members counted toward capacity (Cock's capacity is 0, so this stays 0 for Cock).
      if (currentCount < capacity) {
        await updateDoc(doc(db, "users", referredBy), { teamCount: increment(1) });
      }'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

old_field = '''    lastFedDate: null,
    subscriptionTier: "free",'''
new_field = '''    lastFedDate: null,
    subscriptionTier: "free",
    teamCount: 0,'''
if old_field not in c:
    print('FIELD PATTERN NOT FOUND - check manually')
c = c.replace(old_field, new_field)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
