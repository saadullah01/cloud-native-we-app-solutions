import * as functions from "firebase-functions";

export default functions.firestore
  .document('posts/{slug}')
  .onCreate((snapshot: functions.firestore.DocumentSnapshot,
context: functions.EventContext) => {
  console.log(`New post created with slug: ${context.params.slug}. Post: ${JSON.stringify(snapshot.data())}`)
});

