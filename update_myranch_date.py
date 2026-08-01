with open('my-ranch.html') as f:
    c = f.read()
before = c

WORKER_URL = "https://rancharm-worker.antwordtech.workers.dev"

c = c.replace(
    "let currentUid = null;\n  let currentAnimal = null;\n  let profileData = null;",
    "let currentUid = null;\n  let currentAnimal = null;\n  let profileData = null;\n\n  async function getServerDate() {\n    const res = await fetch('" + WORKER_URL + "/current-date');\n    const data = await res.json();\n    return data.date;\n  }"
)

c = c.replace("function renderRanch(data) {", "async function renderRanch(data) {")
c = c.replace(
    "    const feedBtn = document.getElementById('feedBtn');\n    const today = new Date().toISOString().split('T')[0];\n    const fedToday = data.lastFedDate === today;",
    "    const feedBtn = document.getElementById('feedBtn');\n    const today = await getServerDate();\n    const fedToday = data.lastFedDate === today;"
)

c = c.replace("    renderRanch(profile);", "    await renderRanch(profile);")
c = c.replace("      renderRanch(profileData);", "      await renderRanch(profileData);")

c = c.replace(
    "    const today = new Date().toISOString().split('T')[0];\n    const userRef = doc(db, \"users\", currentUid);",
    "    const today = await getServerDate();\n    const userRef = doc(db, \"users\", currentUid);"
)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
