import * as functions from 'firebase-functions';

exports.onBookingCreated = functions.firestore.document('/bookings/{id}')
  .onCreate(async (snapshot, context) => {
    return await snapshot.ref.set({
      showProbability: Math.random()
    }, {
        merge: true
    });
  });