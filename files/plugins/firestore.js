const admin = require("firebase-admin");

let firebaseApp;
let db;

const getFirebaseApp = (options) => {
  if (!firebaseApp) {
    firebaseApp = admin.initializeApp(options);
  }
  return firebaseApp;
};

const getFirestore = (firebaseAppOptions) => {
  if (!db) {
    db = getFirebaseApp(firebaseAppOptions).firestore();
  }
  return db;
};

module.exports = {
  addBlogPost({ firebaseAppOptions, slug, post }) {
    return new Promise(resolve => {
      getFirestore(firebaseAppOptions).collection("posts").doc(slug).set(post).then(() => {
        resolve(null);
      });
    });
  }
};
