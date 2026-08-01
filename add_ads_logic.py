with open('my-ranch.html') as f:
    c = f.read()
before = c

SMARTLINK_URL = "https://www.effectivecpmnetwork.com/b27gbbgvi?key=45b99abc87be0f94221817c51efc936d"

old_render_tail = '''    feedBtn.disabled = fedToday;
    feedBtn.innerHTML = fedToday ? 'Already Fed Today' : 'Feed Now';
    feedBtn.onclick = window.feedAnimal;
  }'''

new_render_tail = '''    feedBtn.disabled = fedToday;
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

if old_render_tail not in c:
    print('RENDER TAIL PATTERN NOT FOUND - check manually')
c = c.replace(old_render_tail, new_render_tail)

old_feed_end = '''    } catch (e) {
      feedBtn.innerHTML = original;
      feedBtn.classList.remove('btn-loading');
      toast('Something went wrong. Try again.', 'error');
    }
  };'''

new_feed_end = '''    } catch (e) {
      feedBtn.innerHTML = original;
      feedBtn.classList.remove('btn-loading');
      toast('Something went wrong. Try again.', 'error');
    }
  };

  window.watchAd = () => {
    window.open('""" + SMARTLINK_URL + """', '_blank');
    const btn = document.getElementById('watchAdBtn');
    btn.disabled = true;
    let seconds = 15;
    btn.innerHTML = 'Watching... ' + seconds + 's';
    const interval = setInterval(() => {
      seconds--;
      if (seconds <= 0) {
        clearInterval(interval);
        recordAdWatched();
      } else {
        btn.innerHTML = 'Watching... ' + seconds + 's';
      }
    }, 1000);
  };

  async function recordAdWatched() {
    const today = await getServerDate();
    const alreadyToday = profileData.adsWatchedDate === today;
    const newCount = (alreadyToday ? (profileData.adsWatchedCount || 0) : 0) + 1;
    await updateDoc(doc(db, "users", currentUid), { adsWatchedDate: today, adsWatchedCount: newCount });
    profileData.adsWatchedDate = today;
    profileData.adsWatchedCount = newCount;
    toast('Ad watched! (' + newCount + '/5)', 'success');
    await renderRanch(profileData);
  }

  window.claimAdsBonus = async () => {
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

if old_feed_end not in c:
    print('FEED END PATTERN NOT FOUND - check manually')
c = c.replace(old_feed_end, new_feed_end)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
