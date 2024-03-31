import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

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
                  onPressed: () {
                    debugPrint("Create a new account");
                    Navigator.pushNamed(context, '/generateQR');
                  },
                  icon: const Icon(
                    Icons.create_rounded
                  ),
                  label: const Text("Create a new account")
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: ElevatedButton.icon(
                  onPressed: () {
                    debugPrint("Login");
                  },
                  icon: const Icon(
                      Icons.create_rounded
                  ),
                  label: const Text("Log to my account")
              ),
            )
          ],
        ),
      ),
    );
  }
}

