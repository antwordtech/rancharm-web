with open('firebase-config.js') as f:
    c = f.read()
before = c

old = '''export function getTeamLevel(teamCount) {
  const count = teamCount || 0;
  if (count >= 200) return { title: "Ranch Master", next: null, current: 200 };
  if (count >= 50) return { title: "Ranch Leader", next: 200, current: 50 };
  if (count >= 10) return { title: "Ranch Manager", next: 50, current: 10 };
  return { title: "Member", next: 10, current: 0 };
}'''

new = '''export function getTeamLevel(teamCount) {
  const count = teamCount || 0;
  if (count >= 200) return { title: "Ranch Master", next: null, current: 200, bonusPct: 35 };
  if (count >= 50) return { title: "Ranch Leader", next: 200, current: 50, bonusPct: 20 };
  if (count >= 10) return { title: "Ranch Manager", next: 50, current: 10, bonusPct: 10 };
  return { title: "Member", next: 10, current: 0, bonusPct: 0 };
}'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
