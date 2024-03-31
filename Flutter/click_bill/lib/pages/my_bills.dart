import 'dart:io';
import 'package:flutter/material.dart';
import 'package:click_bill/bill.dart' as bl;
import 'package:cunning_document_scanner/cunning_document_scanner.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:path_provider/path_provider.dart';
import 'package:date_field/date_field.dart';

class MyBills extends StatefulWidget {
  const MyBills({Key? key}) : super(key: key);

  @override
  State<MyBills> createState() => _MyBillsState();
}

class _MyBillsState extends State<MyBills> {

  dynamic date;
  dynamic store;
  final storeController = TextEditingController();

  List<String> _pictures = [];
  List<bl.Bill> bills = bl.bills;
  int _selectedIndex = 1;

  @override
  void initState() {
    super.initState();
    storeController.addListener((updateText));
  }

  void updateText(){
    setState(() {
      store = storeController.text;
    });
  }

  Widget billTemplate(bill) {
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
                  bill.shop,
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
                      bill.date,
                      style: TextStyle(
                        fontSize: 14.0,
                        color: Colors.grey[800],
                      ),
                    ),
                    TextButton(
                        onPressed: () =>
                            showDialog<String>(
                              context: context,
                              builder: (BuildContext context) =>
                                  AlertDialog(
                                    title: const Text('Are you sure ?'),
                                    actions: <Widget>[
                                      TextButton(
                                        onPressed: () =>
                                            Navigator.pop(context, 'Cancel'),
                                        child: const Text('Cancel'),
                                      ),
                                      TextButton(
                                        onPressed: () {
                                          setState(() {
                                            bills.remove(bill);
                                          });
                                          Navigator.pop(context, 'Yes');
                                        },
                                        child: const Text('Yes'),
                                      ),
                                    ],
                                  ),
                            ),
                        child: const Icon(Icons.delete, size: 20)
                    ),
                  ],
                ),
              ],
            ),
          )
      ),
    );
  }

  void _onCardTapped(bl.Bill bill) {
    debugPrint('Open the receipt');
    Navigator.pushNamed(context, '/my_receipt', arguments: {
      'pdfPath': bill.pdfPath
    });
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
      if (_selectedIndex == 0) {
        bl.bills = bills;
        Navigator.pushReplacementNamed(context, '/my_qr_code');
      }
    });
  }

  void _newBill(String store, String date) async {
    List<String> pictures;
    try {
      pictures = await CunningDocumentScanner.getPictures(true) ?? [];
      if (!mounted) return;
      setState(() {
        _pictures = pictures;
      });
      final pdf = pw.Document();
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
      Directory appDocumentsDir = await getApplicationDocumentsDirectory();
      final now = DateTime.now();
      debugPrint('${appDocumentsDir.path}/$now.pdf');
      final file = File('${appDocumentsDir.path}/$now.pdf');
      await file.writeAsBytes(await pdf.save());
      setState(() {
        bills.add(bl.Bill(store, date, file.path));
      });
      debugPrint("Scan succeed !");
    } catch (exception) {
      debugPrint(exception.toString());
      debugPrint("Scan failed ..");
    }
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[800],
        title: const Text('My Bills'),
        centerTitle: true,
        foregroundColor: Colors.white,
      ),
      body: bills.isEmpty ?
      const Center(
          child: Text("You have no bills yet"),
      ):
      Column(
        children: bills.map((bill) => billTemplate(bill)).toList()
      ),
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
