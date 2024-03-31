import 'package:flutter/material.dart';
import 'package:click_bill/pages/home.dart';
import 'package:click_bill/pages/generate_qr.dart';
import 'package:click_bill/pages/my_qr_code.dart';
import 'package:click_bill/pages/my_bills.dart';
import 'package:click_bill/my_receipt.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

void main() => runApp(MaterialApp(
    routes: {
      '/': (context) => const Home(),
      '/generateQR': (context) => const  GenerateQR(),
      '/my_qr_code': (context) => const MyQRCode(),
      '/my_bills': (context) => const MyBills(),
      '/my_receipt': (context) => const MyReceipt(),
    },
));

