import 'package:flutter/material.dart';
import 'package:click_bill/user.dart';

class GenerateQR extends StatefulWidget {
  const GenerateQR({Key? key}) : super(key: key);

  @override
  State<GenerateQR> createState() => _GenerateQRState();
}

class _GenerateQRState extends State<GenerateQR> {

  dynamic userName;
  dynamic userMail;
  dynamic userNum;
  final nameController = TextEditingController();
  final mailController = TextEditingController();
  final numController = TextEditingController();
  List<User> users = [];

  @override
  void initState() {
    super.initState();
    nameController.addListener((updateText));
    mailController.addListener((updateText));
    numController.addListener((updateText));
  }

  void updateText(){
    setState(() {
      userName = nameController.text;
      userMail = mailController.text;
      userNum = numController.text;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title:
            const Text('Generate your QR code'),
            foregroundColor: Colors.white,
          centerTitle: true,
          backgroundColor: Colors.grey[800],
        ),
        body: Padding(
          padding: const EdgeInsets.all(10),
          child: Center(
            child: Column(
                children: [
                    Padding(
                      padding: const EdgeInsets.fromLTRB(8,0,8,0),
                      child: TextFormField(
                        controller: nameController,
                        decoration: const InputDecoration(
                          border: OutlineInputBorder(),
                          labelText: 'Enter your name',
                        ),
                      ),
                    ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: TextFormField(
                      controller: mailController,
                      decoration: const InputDecoration(
                        border: OutlineInputBorder(),
                        labelText: 'Enter your mail',
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.fromLTRB(8,0,8,0),
                    child: TextFormField(
                      controller: numController,
                      decoration: const InputDecoration(
                        border: OutlineInputBorder(),
                        labelText: 'Enter your phone number',
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: ElevatedButton.icon(
                        onPressed: (){
                          debugPrint('GENERATED: $userName, $userMail, $userNum');
                          Navigator.pushReplacementNamed(context, '/my_qr_code', arguments: {
                            'userName' : userName,
                            'userMail' : userMail,
                            'userNum' : userNum,
                          });

                        },
                        icon: const Icon(
                            Icons.qr_code
                        ),
                        label: const Text('Generate my QRcode')
                    ),
                  )
                ]
            ),
          ),
        )
    );
  }
}