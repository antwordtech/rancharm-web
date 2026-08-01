with open('firebase-config.js') as f:
    c = f.read()
before = c

# Add Firebase Storage import
c = c.replace(
    'import { getFirestore, doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";',
    'import { getFirestore, doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";\nimport { getStorage, ref, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-storage.js";'
)

# Export storage instance
c = c.replace(
    'export const db = getFirestore(app);',
    'export const db = getFirestore(app);\nexport const storage = getStorage(app);'
)

# Default new users to "unverified" KYC status
c = c.replace(
    '    lastFedDate: null,\n    subscriptionTier: "free",\n    teamCount: 0,',
    '    lastFedDate: null,\n    subscriptionTier: "free",\n    teamCount: 0,\n    kycStatus: "unverified",'
)

# Add the KYC submission function (after createUserProfile)
c = c.replace(
    'export { doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit };',
    '''export async function submitKYC(user, { fullName, idType, idNumber, idFile, selfieFile }) {
  const idRef = ref(storage, `kyc/${user.uid}/id-photo.jpg`);
  await uploadBytes(idRef, idFile);
  const idPhotoUrl = await getDownloadURL(idRef);

  const selfieRef = ref(storage, `kyc/${user.uid}/selfie.jpg`);
  await uploadBytes(selfieRef, selfieFile);
  const selfiePhotoUrl = await getDownloadURL(selfieRef);

  await setDoc(doc(db, "kyc", user.uid), {
    fullName,
    idType,
    idNumber,
    idPhotoUrl,
    selfiePhotoUrl,
    status: "pending",
    submittedAt: Date.now()
  });

  await updateDoc(doc(db, "users", user.uid), { kycStatus: "pending" });
}

export { doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit };'''
)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE - check manually')
