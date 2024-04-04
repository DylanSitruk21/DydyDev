import 'package:click_bill/google_auth.dart' as gg;
import 'package:flutter/material.dart';
import 'package:qr_flutter/qr_flutter.dart';
// import 'package:pretty_qr_code/pretty_qr_code.dart';

class MyQRCode extends StatefulWidget {
  const MyQRCode({Key? key}) : super(key: key);

  @override
  State<MyQRCode> createState() => _MyQRCodeState();
}

class _MyQRCodeState extends State<MyQRCode> {

  Object? userData = {};
  int _selectedIndex = 0;

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
      if (_selectedIndex == 1){
        Navigator.pushReplacementNamed(context, '/my_bills');
      }
    });
  }

  void awaitSignOut(context) async{
    await gg.signOutWithGoogle();
    debugPrint("${gg.user?.displayName} is signing out");
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {

    userData = ModalRoute.of(context)?.settings.arguments;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[800],
        title:
          const Text('My QR code'),
          foregroundColor: Colors.white,
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.exit_to_app_rounded),
            onPressed: () {
              debugPrint("User sign out");
              awaitSignOut(context);
            },
          ),
        ],
      ),
      body: Center(
        child: QrImageView(
          data: userData.toString(),
          size: 400,
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.qr_code),
            label: 'My QR code',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.payment),
            label: 'My Bills',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.amber[800],
        onTap: _onItemTapped,
      ),
    );
  }
}