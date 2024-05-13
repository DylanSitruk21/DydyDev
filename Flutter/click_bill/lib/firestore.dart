import 'package:firebase_auth/firebase_auth.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:click_bill/google_auth.dart' as gg;


FirebaseFirestore db = FirebaseFirestore.instance;
CollectionReference users = db.collection('users');
Reference storageRef = FirebaseStorage.instance.ref();


Future<void> addUser(User? user) async {
  final CollectionReference users = db.collection('users');

  await users.doc(user?.uid).set({
    'displayName': user?.displayName,
    'email': user?.email,
    // Add any other user information you want to store
  });
}

void deletePdf(String path) async {
  final toDelRef = storageRef.child("${gg.user?.displayName}/$path");
  await toDelRef.delete();
  print("PDF successfully deleted");
}