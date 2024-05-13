import 'dart:async';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_pdfviewer/pdfviewer.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:click_bill/google_auth.dart' as gg;

class MyReceipt extends StatefulWidget {
  const MyReceipt({Key? key}) : super(key: key);

  @override
  State<MyReceipt> createState() => _MyReceiptState();
}

class _MyReceiptState extends State<MyReceipt> {
  Map userData = {};
  Uint8List pdfData = Uint8List.fromList([0]);

  FutureOr<Uint8List> _getPdf(String path) async {
    final gsReference = FirebaseStorage.instance.ref().child('${gg.user?.displayName}/$path');
    try{
      final Uint8List? data = await gsReference.getData();
      pdfData = data!;
      return pdfData;
    } on FirebaseException catch (e) {
      print("Failed with error '${e.code}': ${e.message}");
      return Uint8List.fromList([0]);
    }
  }

  void updatePdfData(String path) async{
    Uint8List pdfDataTemp = await _getPdf(path);
    setState(() {
      pdfData = pdfDataTemp;
    });
  }

  Uint8List _pdfData(String path) {
    updatePdfData(path);
    return pdfData;
  }

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
          child: SfPdfViewer.memory(
            //File(userData['pdfPath']),
            _pdfData(userData['pdfPath']),
          )
      )
    );
  }
}
