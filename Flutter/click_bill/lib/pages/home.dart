import 'package:flutter/material.dart';
import 'package:click_bill/google_auth.dart' as gg;
import 'package:click_bill/firestore.dart' as fs;

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  void awaitSignIn(context) async {
    gg.user = await gg.signInWithGoogle();
    debugPrint("${gg.user?.displayName} is signing in");
    fs.addUser(gg.user);
    Navigator.pushNamed(context, '/my_qr_code', arguments: {
      'userName' : gg.user?.displayName,
      'userMail' : gg.user?.email,
    });
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[800],
        centerTitle: true,
        title:
          const Text('Welcome to ClickBill'),
          foregroundColor: Colors.white,
      ),
      body: Center(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(0, 100, 0, 12),
              child: ElevatedButton.icon(
                  onPressed: () async {
                    debugPrint("Google sign in");
                    awaitSignIn(context);
                  },
                  icon: const Icon(
                    Icons.create_rounded
                  ),
                  label: const Text("Sign in with Google")
              ),
            )
          ],
        ),
      ),
    );
  }
}

