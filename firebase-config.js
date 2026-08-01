import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import { getFirestore, doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
import { getStorage, ref, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyDbEAloJNKfhVqP7mE6xCAHhIS_rC67Pgs",
  authDomain: "rancharmtech.firebaseapp.com",
  projectId: "rancharmtech",
  storageBucket: "rancharmtech.firebasestorage.app",
  messagingSenderId: "281311441496",
  appId: "1:281311441496:web:e12131915909bd8401502d"
};

export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);

export const ANIMALS = [
  { key: "cock",   name: "Cock",   price: 0,    tier: "Starter",  dailyPoints: 50,   image: null, lottie: "https://lottie.host/596eb98d-85c0-4779-b3e1-5e8db56a494f/zj1yYMqMHa.json", benefits: ["Basic tasks", "Basic rewards", "Beginner access", "Starter Team"], teamCapacity: 0 },
  { key: "duck",   name: "Duck",   price: 50,   tier: "Bronze",   dailyPoints: 100,  image: null, lottie: "https://lottie.host/e1bba21b-0fee-41af-ae55-26291082f468/ZOsTxfZBvR.json", benefits: ["More tasks", "Higher Point limit", "Bronze Team", "Better opportunities"], teamCapacity: 20 },
  { key: "pig",    name: "Pig",    price: 150,  tier: "Silver",   dailyPoints: 300,  image: null, lottie: "https://lottie.host/dc296098-4998-49a6-93f0-d592282e7de4/EthkkTygvZ.json", benefits: ["More activities", "Community tools", "Silver Team", "Higher rewards access"], teamCapacity: 50 },
  { key: "fox",    name: "Fox",    price: 500,  tier: "Gold",     dailyPoints: 1000, image: null, lottie: "https://lottie.host/41f6f306-fabd-42a7-adb4-0d7038a3c37e/wlbHGxS0ZC.json", benefits: ["Higher Point limit", "Gold Team", "Premium Tasks", "Higher Commission"], teamCapacity: 100 },
  { key: "monkey", name: "Monkey", price: 1000, tier: "Platinum", dailyPoints: 2000, image: null, lottie: "https://lottie.host/ece552b9-20a5-4c98-bfd1-f90a6eb22aad/fglkIKvYob.json", benefits: ["Advanced tools", "Platinum Team", "Premium campaigns", "Bigger community"], teamCapacity: 250, scale: 1.8 },
  { key: "parrot", name: "Parrot", price: 2000, tier: "VIP",      dailyPoints: 4000, image: null, lottie: "https://lottie.host/7849c0e2-0026-4e21-a353-db246b1a1bcf/HoxniEkE7X.json", benefits: ["VIP campaigns", "Higher privileges", "Priority access", "VIP Team"], teamCapacity: 500 },
  { key: "horse",  name: "Horse",  price: 5000, tier: "Elite",    dailyPoints: 10000, image: null, lottie: "https://lottie.host/e388d08e-854a-4c29-a88a-7b7a7cbc87b6/PeYW0lHF66.json", benefits: ["Maximum access", "Elite campaigns", "Highest limits", "Leadership features"], teamCapacity: 1000 }
];

export const SUBSCRIPTIONS = [
  { key: "free",    name: "Free",    price: 0,   benefits: ["Ads shown", "Basic tasks"] },
  { key: "premium", name: "Premium", price: 20,  benefits: ["Fewer ads", "More tasks", "Better features"] },
  { key: "vip",     name: "VIP",     price: 50,  benefits: ["VIP access", "Special campaigns"] },
  { key: "elite",   name: "Elite",   price: 200, benefits: ["Advanced tools", "Business features"] }
];

function generateReferralCode(uid) {
  return uid.substring(0, 8).toUpperCase();
}

// Single read, returns the data directly (or null) — no separate exists-check call needed.
export async function getUserProfile(uid) {
  const snap = await getDoc(doc(db, "users", uid));
  return snap.exists() ? snap.data() : null;
}

// Single read, creates the wallet only if missing, returns data either way.
export async function getOrCreateWallet(user) {
  const ref = doc(db, "wallets", user.uid);
  const snap = await getDoc(ref);
  if (snap.exists()) return snap.data();
  const fresh = { points: 0, coins: 0, lastUpdated: Date.now() };
  await setDoc(ref, fresh);
  return fresh;
}

export async function createUserProfile(user, phone, referralCodeInput) {
  let referredBy = null;
  const code = (referralCodeInput || sessionStorage.getItem('pendingReferralCode') || '').trim();

  if (code) {
    const q = query(collection(db, "users"), where("referralCode", "==", code));
    const snap = await getDocs(q);
    if (!snap.empty) {
      const referrerDoc = snap.docs[0];
      referredBy = referrerDoc.id;
      const referrerData = referrerDoc.data();
      const referrerTier = referrerData.animalTier || "cock";
      const referrerAnimal = ANIMALS.find(a => a.key === referrerTier);
      const capacity = referrerAnimal ? referrerAnimal.teamCapacity : 0;
      const currentCount = referrerData.teamCount || 0;

      // Flat referral point reward: 100 pts if referrer is Cock, 200 pts for Duck and above.
      const rewardPoints = referrerTier === "cock" ? 100 : 200;
      await updateDoc(doc(db, "wallets", referredBy), { points: increment(rewardPoints) });

      // referralCount = total people ever referred (always grows, this is "People Referred").
      await updateDoc(doc(db, "users", referredBy), { referralCount: increment(1) });

      // teamCount = active team members counted toward capacity (Cock's capacity is 0, so this stays 0 for Cock).
      if (currentCount < capacity) {
        await updateDoc(doc(db, "users", referredBy), { teamCount: increment(1) });
      }
    }
  }
  sessionStorage.removeItem('pendingReferralCode');

  await setDoc(doc(db, "users", user.uid), {
    email: user.email,
    phone: phone,
    animalTier: "cock",
    completedTasks: [],
    referralCode: generateReferralCode(user.uid),
    referredBy: referredBy,
    referralCount: 0,
    lastFedDate: null,
    subscriptionTier: "free",
    teamCount: 0,
    kycStatus: "unverified",
    createdAt: Date.now()
  }, { merge: true });

  await getOrCreateWallet(user);
}

export async function submitKYC(user, { mobileMoneyNumber, registeredName, idType, idFile, selfieFile }) {
  const idRef = ref(storage, `kyc/${user.uid}/id-photo.jpg`);
  await uploadBytes(idRef, idFile);
  const idPhotoUrl = await getDownloadURL(idRef);

  const selfieRef = ref(storage, `kyc/${user.uid}/selfie.jpg`);
  await uploadBytes(selfieRef, selfieFile);
  const selfiePhotoUrl = await getDownloadURL(selfieRef);

  await setDoc(doc(db, "kyc", user.uid), {
    mobileMoneyNumber,
    registeredName,
    idType,
    idPhotoUrl,
    selfiePhotoUrl,
    status: "pending",
    submittedAt: Date.now()
  });

  await updateDoc(doc(db, "users", user.uid), { kycStatus: "pending" });
}

export { doc, getDoc, setDoc, updateDoc, increment, arrayUnion, collection, query, where, getDocs, orderBy, limit };
