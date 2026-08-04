with open('my-ranch.html') as f:
    c = f.read()
before = c

old_import = "import { auth, db, doc, updateDoc, increment, getUserProfile, ANIMALS } from './firebase-config.js?v=3';"
new_import = "import { auth, db, doc, updateDoc, increment, getUserProfile, ANIMALS, getTeamLevel } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_tail = '''      await Promise.all([
        updateDoc(userRef, { lastFedDate: today, totalProfit: increment(currentAnimal.dailyPoints) }),
        updateDoc(walletRef, { points: increment(currentAnimal.dailyPoints), lastUpdated: Date.now() })
      ]);'''

new_tail = '''      const rankBonus = getTeamLevel(profileData.teamCount || 0).bonusPct;
      const earnedPoints = Math.round(currentAnimal.dailyPoints * (1 + rankBonus / 100));

      await Promise.all([
        updateDoc(userRef, { lastFedDate: today, totalProfit: increment(earnedPoints) }),
        updateDoc(walletRef, { points: increment(earnedPoints), lastUpdated: Date.now() })
      ]);'''

if old_tail not in c:
    print('TAIL NOT FOUND - check manually')
c = c.replace(old_tail, new_tail)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
