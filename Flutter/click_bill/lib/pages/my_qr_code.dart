// import 'dart:io';
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

  // @override
  // Future<void> initState() async {
  //   final server = await ServerSocket.bind('localhost', 2714);
  //   server.listen((client) async {
  //     await File('1.zip').openRead().pipe(client);
  //   });
  //   super.initState();
  // }

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