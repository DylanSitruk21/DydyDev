import 'dart:io';
import 'package:flutter/material.dart';
import 'package:cunning_document_scanner/cunning_document_scanner.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:date_field/date_field.dart';
import 'package:click_bill/google_auth.dart' as gg;
import 'package:click_bill/firestore.dart' as fs;
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_storage/firebase_storage.dart';

class MyBills extends StatefulWidget {
  const MyBills({Key? key}) : super(key: key);

  @override
  State<MyBills> createState() => _MyBillsState();
}

class _MyBillsState extends State<MyBills> {
  dynamic date;
  dynamic store;
  final storeController = TextEditingController();
  bool isBillsEmpty = true;
  int billsNumber = 0;
  List<String> _pictures = [];
  CollectionReference<Map<String, dynamic>> bills =
      fs.users.doc(gg.user?.uid).collection('bills');
  List<DocumentSnapshot<Object?>> billDocs = [];
  int _selectedIndex = 1;

  void getData() async {
    updateBillsNum();
    await Future.delayed(const Duration(seconds: 2), () {
      print("Bills empty: $isBillsEmpty");
      print("Num of bills: $billsNumber");
    });
  }

  @override
  void initState() {
    super.initState();
    storeController.addListener((updateText));
    getData();
  }

  void updateText() {
    setState(() {
      store = storeController.text;
    });
  }

  Widget billTemplate(DocumentSnapshot bill) {
    return GestureDetector(
      onTap: () => _onCardTapped(bill),
      child: Card(
          margin: const EdgeInsets.fromLTRB(16.0, 16.0, 16.0, 0),
          child: Padding(
            padding: const EdgeInsets.all(12.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: <Widget>[
                Text(
                  bill["store"].toString(),
                  style: TextStyle(
                    fontSize: 18.0,
                    color: Colors.grey[600],
                  ),
                ),
                const SizedBox(height: 6.0),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      bill["date"].toString(),
                      style: TextStyle(
                        fontSize: 14.0,
                        color: Colors.grey[800],
                      ),
                    ),
                    TextButton(
                        onPressed: () => showDialog<String>(
                              context: context,
                              builder: (BuildContext context) => AlertDialog(
                                title: const Text('Are you sure ?'),
                                actions: <Widget>[
                                  TextButton(
                                    onPressed: () =>
                                        Navigator.pop(context, 'Cancel'),
                                    child: const Text('Cancel'),
                                  ),
                                  TextButton(
                                    onPressed: () {
                                      bills.doc(bill.id).delete();
                                      fs.deletePdf(bill['pdfPath']);
                                      updateBillsNum();
                                      Navigator.pop(context, 'Yes');
                                    },
                                    child: const Text('Yes'),
                                  ),
                                ],
                              ),
                            ),
                        child: const Icon(Icons.delete, size: 20)),
                  ],
                ),
              ],
            ),
          )),
    );
  }

  void _onCardTapped(DocumentSnapshot bill) {
    debugPrint('Open the receipt');
    Navigator.pushNamed(context, '/my_receipt',
        arguments: {'pdfPath': bill["pdfPath"]});
  }

  Future<List<DocumentSnapshot<Object?>>> _billDocs() async {
    final QuerySnapshot querySnapshot = await bills.get();
    return querySnapshot.docs;
  }

  Future<bool> _isBillsEmpty() async {
    final QuerySnapshot querySnapshot = await bills.get();
    return querySnapshot.docs.isEmpty;
  }

  Future<int> _howManyBills() async {
    final QuerySnapshot querySnapshot = await bills.get();
    return querySnapshot.docs.length;
  }

  void updateBillsNum() async {
    bool isBillsEmptyTemp = await _isBillsEmpty();
    int billsNumberTemp = await _howManyBills();
    List<DocumentSnapshot<Object?>> billDocsTemp = await _billDocs();
    setState(() {
      isBillsEmpty = isBillsEmptyTemp;
      billsNumber = billsNumberTemp;
      billDocs = billDocsTemp;
    });
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
      if (_selectedIndex == 0) {
        Navigator.pushReplacementNamed(context, '/my_qr_code', arguments: {
          'userName': gg.user?.displayName,
          'userMail': gg.user?.email,
        });
      }
    });
  }

  void _newBill(String store, String date) async {
    Map<String, dynamic> newBill = {"store": 0, "date": 0, "pdfPath": 0};
    List<String> pictures;
    final pdf = pw.Document();
    try {
      pictures = await CunningDocumentScanner.getPictures(true) ?? [];
      if (!mounted) return;
      setState(() {
        _pictures = pictures;
      });
      for (var picture in _pictures) {
        final image = pw.MemoryImage(
          File(picture).readAsBytesSync(),
        );
        pdf.addPage(pw.Page(build: (pw.Context context) {
          return pw.Center(
            child: pw.Image(image),
          );
        }));
      }
      debugPrint("Scan succeed !");
    } catch (exception) {
      debugPrint(exception.toString());
      debugPrint("Scan failed ..");
    }
    final now = DateTime.now();

    Reference storageRef = FirebaseStorage.instance.ref().child('${gg.user?.displayName}/$now');
    UploadTask uploadTask = storageRef.putData(await pdf.save());
    TaskSnapshot taskSnapshot = await uploadTask;
    await uploadTask.whenComplete(() => print('File uploaded successfully'));

    newBill["store"] = store;
    newBill["date"] = date;
    newBill["pdfPath"] = '$now';

    setState(() {
      bills.doc().set(newBill);
      updateBillsNum();
    });
  }

  void awaitSignOut(context) async {
    await gg.signOutWithGoogle();
    debugPrint("${gg.user?.displayName} is signing out");
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[800],
        title: const Text('My Bills'),
        centerTitle: true,
        foregroundColor: Colors.white,
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
      body: isBillsEmpty
          ? const Center(
              child: Text("You have no bills yet"),
            )
          : Column(
              children: billDocs
                  .map((DocumentSnapshot bill) => billTemplate(bill))
                  .toList()),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          showDialog(
            context: context,
            builder: (context) => AlertDialog(
              title: const Text("New receipt"),
              actions: <Widget>[
                TextFormField(
                  controller: storeController,
                  decoration: const InputDecoration(
                    labelText: 'Enter store name',
                  ),
                ),
                DateTimeFormField(
                  decoration: const InputDecoration(
                    labelText: 'Enter Date',
                  ),
                  initialPickerDateTime: DateTime.now(),
                  onChanged: (DateTime? value) {
                    date = value;
                  },
                ),
                TextButton(
                  onPressed: () {
                    _newBill(store.toString(), date.toString());
                    Navigator.pop(context);
                  },
                  child: const Text("Scan the receipt"),
                ),
              ],
            ),
          );
        },
        tooltip: 'Add a new bill',
        child: const Icon(Icons.add),
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
