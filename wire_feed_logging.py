with open('my-ranch.html') as f:
    c = f.read()
before = c

old_import = "import { auth, db, doc, updateDoc, increment, getUserProfile, ANIMALS, getTeamLevel } from './firebase-config.js?v=3';"
new_import = "import { auth, db, doc, updateDoc, increment, addDoc, collection, getUserProfile, ANIMALS, getTeamLevel } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_feed = '''      await Promise.all([
        updateDoc(userRef, { lastFedDate: today, totalProfit: increment(earnedPoints) }),
        updateDoc(walletRef, { points: increment(earnedPoints), lastUpdated: Date.now() })
      ]);'''
new_feed = '''      await Promise.all([
        updateDoc(userRef, { lastFedDate: today, totalProfit: increment(earnedPoints) }),
        updateDoc(walletRef, { points: increment(earnedPoints), lastUpdated: Date.now() }),
        addDoc(collection(db, "transactions"), {
          uid: currentUid,
          type: "feed",
          amount: earnedPoints,
          description: "Fed " + currentAnimal.name + (rankBonus > 0 ? " (+" + rankBonus + "% team bonus)" : ""),
          createdAt: Date.now()
        })
      ]);'''
if old_feed not in c:
    print('FEED NOT FOUND - check manually')
c = c.replace(old_feed, new_feed)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
