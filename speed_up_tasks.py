with open('tasks.html') as f:
    c = f.read()
before = c

old_auth = '''  onAuthStateChanged(auth, async function(user) {
    if (!user) { window.location.href = 'login.html'; return; }
    const profile = await getUserProfile(user.uid);
    if (!profile) { window.location.href = 'complete-profile.html'; return; }
    currentUser = user;
    userTierRank = TIER_RANK[profile.subscriptionTier || 'free'] || 0;

    await loadSubmissions();
    await loadTasks();
    document.body.classList.add('ready');
  });

  async function loadSubmissions() {
    const snap = await getDocs(query(collection(db, "taskSubmissions"), where("uid", "==", currentUser.uid)));
    snap.forEach(function(docSnap) {
      const sub = docSnap.data();
      submittedTaskIds[sub.taskId] = sub.status;
    });
  }

  async function loadTasks() {
    const list = document.getElementById('tasksList');
    const snap = await getDocs(query(collection(db, "tasks"), where("active", "==", true)));

    const eligible = [];'''

new_auth = '''  onAuthStateChanged(auth, async function(user) {
    if (!user) { window.location.href = 'login.html'; return; }

    const [profile, submissionsSnap, tasksSnap] = await Promise.all([
      getUserProfile(user.uid),
      getDocs(query(collection(db, "taskSubmissions"), where("uid", "==", user.uid))),
      getDocs(query(collection(db, "tasks"), where("active", "==", true)))
    ]);

    if (!profile) { window.location.href = 'complete-profile.html'; return; }
    currentUser = user;
    userTierRank = TIER_RANK[profile.subscriptionTier || 'free'] || 0;

    submissionsSnap.forEach(function(docSnap) {
      const sub = docSnap.data();
      submittedTaskIds[sub.taskId] = sub.status;
    });

    renderTasks(tasksSnap);
    document.body.classList.add('ready');
  });

  function renderTasks(snap) {
    const list = document.getElementById('tasksList');

    const eligible = [];'''

if old_auth not in c:
    print('AUTH BLOCK NOT FOUND - check manually')
c = c.replace(old_auth, new_auth)

with open('tasks.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
