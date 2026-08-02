with open('firebase-config.js') as f:
    c = f.read()
before = c

dup_block = '''export const ADMIN_EMAIL = "antwordtech@gmail.com";
export function isAdmin(user) {
  return !!user && user.email === ADMIN_EMAIL;
}

export const ADMIN_EMAIL = "antwordtech@gmail.com";
export function isAdmin(user) {
  return !!user && user.email === ADMIN_EMAIL;
}'''

single_block = '''export const ADMIN_EMAIL = "antwordtech@gmail.com";
export function isAdmin(user) {
  return !!user && user.email === ADMIN_EMAIL;
}'''

if dup_block not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(dup_block, single_block)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
