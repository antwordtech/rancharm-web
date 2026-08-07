with open('admin-task-submissions.html') as f:
    c = f.read()
before = c

old_import = "import { auth, db, doc, updateDoc, increment, isAdmin, getUserProfile, collection, query, where, getDocs } from './firebase-config.js?v=3';"
new_import = "import { auth, db, doc, updateDoc, increment, addDoc, isAdmin, getUserProfile, collection, query, where, getDocs } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_btn = '''<button onclick="approveSubmission('${subId}', '${sub.uid}', ${sub.pointsReward}, this)">Approve</button>'''
new_btn = '''<button onclick="approveSubmission('${subId}', '${sub.uid}', ${sub.pointsReward}, '${sub.taskTitle}', this)">Approve</button>'''
if old_btn not in c:
    print('BUTTON NOT FOUND - check manually')
c = c.replace(old_btn, new_btn)

old_fn = '''  window.approveSubmission = async function(subId, uid, pointsReward, btn) {
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
    try {
      await Promise.all([
        updateDoc(doc(db, "taskSubmissions", subId), { status: "approved" }),
        updateDoc(doc(db, "wallets", uid), { points: increment(pointsReward) })
      ]);'''
new_fn = '''  window.approveSubmission = async function(subId, uid, pointsReward, taskTitle, btn) {
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
    try {
      await Promise.all([
        updateDoc(doc(db, "taskSubmissions", subId), { status: "approved" }),
        updateDoc(doc(db, "wallets", uid), { points: increment(pointsReward) }),
        addDoc(collection(db, "transactions"), {
          uid: uid,
          type: "task_reward",
          amount: pointsReward,
          description: "Task approved: " + taskTitle,
          createdAt: Date.now()
        })
      ]);'''
if old_fn not in c:
    print('FUNCTION NOT FOUND - check manually')
c = c.replace(old_fn, new_fn)

with open('admin-task-submissions.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
