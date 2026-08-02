with open('firebase-config.js') as f:
    c = f.read()
before = c

c = c.replace(
    'import { getFirestore, doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";',
    'import { getFirestore, doc, getDoc, setDoc, updateDoc, deleteDoc, addDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";'
)

c = c.replace(
    'export const storage = getStorage(app);',
    '''export const storage = getStorage(app);

export const ADMIN_EMAIL = "antwordtech@gmail.com";
export function isAdmin(user) {
  return !!user && user.email === ADMIN_EMAIL;
}'''
)

c = c.replace(
    'export { doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit };',
    'export { doc, getDoc, setDoc, updateDoc, deleteDoc, addDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit };'
)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
