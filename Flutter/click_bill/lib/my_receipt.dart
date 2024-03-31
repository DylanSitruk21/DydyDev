import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_pdfviewer/pdfviewer.dart';
import 'dart:io';

class MyReceipt extends StatefulWidget {
  const MyReceipt({Key? key}) : super(key: key);

  @override
  State<MyReceipt> createState() => _MyReceiptState();
}

class _MyReceiptState extends State<MyReceipt> {
  Map userData = {};
  @override
  Widget build(BuildContext context) {
    userData = ModalRoute.of(context)?.settings.arguments as Map;
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[800],
        title: const Text('Your receipt'),
        centerTitle: true,
        foregroundColor: Colors.white,
      ),
      body: Center(
          child: SfPdfViewer.file(
              File(userData['pdfPath']),
          )
      )
    );
  }
}
