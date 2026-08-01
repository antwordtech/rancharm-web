with open('my-ranch.html') as f:
    c = f.read()
before = c

# 1) Update card copy — no bonus points, just "unlock feeding" framing
old_card_text = '''    <div style="font-weight:800;font-size:16px;margin-bottom:4px;">Watch Ads for Bonus Points</div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:16px;">Watch 5 ads to earn <span id="adsBonusAmount">0</span> bonus points today</div>'''

new_card_text = '''    <div style="font-weight:800;font-size:16px;margin-bottom:4px;">Watch Ads to Unlock Feeding</div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:16px;">Watch 5 ads today before you can feed your animal</div>'''

if old_card_text not in c:
    print('CARD TEXT PATTERN NOT FOUND - check manually')
c = c.replace(old_card_text, new_card_text)

# 2) Replace the feed-gate + ads-status block in renderRanch, and drop the bonus-claim logic
old_logic = '''    feedBtn.disabled = fedToday;
    feedBtn.innerHTML = fedToday ? 'Already Fed Today' : 'Feed Now';
    feedBtn.onclick = window.feedAnimal;

    const adsToday = (data.adsWatchedDate === today) ? (data.adsWatchedCount || 0) : 0;
    const adsBonusClaimed = (data.adsWatchedDate === today) && data.adsBonusClaimed === true;
    const bonusAmount = Math.round(currentAnimal.dailyPoints * 0.5);
    document.getElementById('adsBonusAmount').textContent = bonusAmount;
    document.getElementById('adsProgressText').textContent = adsToday + ' / 5 ads watched';
    document.getElementById('adsProgressFill').style.width = Math.min(100, (adsToday / 5) * 100) + '%';

    const watchBtn = document.getElementById('watchAdBtn');
    if (adsBonusClaimed) {
      watchBtn.disabled = true;
      watchBtn.innerHTML = 'Bonus Claimed Today';
    } else if (adsToday >= 5) {
      watchBtn.disabled = false;
      watchBtn.innerHTML = 'Claim Bonus';
      watchBtn.onclick = window.claimAdsBonus;
    } else {
      watchBtn.disabled = false;
      watchBtn.innerHTML = 'Watch Ad (' + adsToday + '/5)';
      watchBtn.onclick = window.watchAd;
    }
  }'''

new_logic = '''    const adsToday = (data.adsWatchedDate === today) ? (data.adsWatchedCount || 0) : 0;
    document.getElementById('adsProgressText').textContent = adsToday + ' / 5 ads watched';
    document.getElementById('adsProgressFill').style.width = Math.min(100, (adsToday / 5) * 100) + '%';

    const watchBtn = document.getElementById('watchAdBtn');
    if (adsToday >= 5) {
      watchBtn.disabled = true;
      watchBtn.innerHTML = 'All Ads Watched Today';
    } else {
      watchBtn.disabled = false;
      watchBtn.innerHTML = 'Watch Ad (' + adsToday + '/5)';
      watchBtn.onclick = window.watchAd;
    }

    if (fedToday) {
      feedBtn.disabled = true;
      feedBtn.innerHTML = 'Already Fed Today';
    } else if (adsToday < 5) {
      feedBtn.disabled = true;
      feedBtn.innerHTML = 'Watch 5 Ads First';
    } else {
      feedBtn.disabled = false;
      feedBtn.innerHTML = 'Feed Now';
      feedBtn.onclick = window.feedAnimal;
    }
  }'''

if old_logic not in c:
    print('LOGIC PATTERN NOT FOUND - check manually')
c = c.replace(old_logic, new_logic)

# 3) Remove the now-unused claimAdsBonus function
old_claim = '''  window.claimAdsBonus = async () => {
    const btn = document.getElementById('watchAdBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Claiming...';
    try {
      const bonusAmount = Math.round(currentAnimal.dailyPoints * 0.5);
      await Promise.all([
        updateDoc(doc(db, "users", currentUid), { adsBonusClaimed: true }),
        updateDoc(doc(db, "wallets", currentUid), { points: increment(bonusAmount), lastUpdated: Date.now() })
      ]);
      profileData.adsBonusClaimed = true;
      toast('+' + bonusAmount + ' bonus points!', 'success');
      await renderRanch(profileData);
    } catch (e) {
      toast('Something went wrong. Try again.', 'error');
      btn.disabled = false;
    }
  };'''

if old_claim not in c:
    print('CLAIM FUNCTION NOT FOUND - check manually')
c = c.replace(old_claim, '')

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
