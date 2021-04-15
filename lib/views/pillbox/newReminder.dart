import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class NewReminderPage extends StatefulWidget {
  @override
  _NewReminderPageState createState() => _NewReminderPageState();
}

class _NewReminderPageState extends State<NewReminderPage> {
  final _formKey = GlobalKey<FormState>();
  String medname;
  String dosage;
  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0.0,
        title: Text(
          "Add a new reminder",
          style: TextStyle(
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
      body: Container(
        height: double.infinity,
        child: SingleChildScrollView(
          child: Column(
            children: [
              SizedBox(
                height: 50.0,
              ),
              Center(
                child: Form(
                  key: _formKey,
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      SizedBox(
                        width: width * 0.9,
                        child: TextFormField(
                          decoration:
                              InputDecoration(hintText: "Medicine Name"),
                          validator: (val) {
                            return val.isEmpty ? "Enter Medicine Name" : null;
                          },
                          onChanged: (val) {
                            medname = val;
                          },
                        ),
                      ),
                      SizedBox(
                        width: width * 0.9,
                        child: TextFormField(
                          decoration: InputDecoration(hintText: "Dosage in mg"),
                          validator: (val) {
                            return val.isEmpty ? "Enter dosage in mg" : null;
                          },
                          onChanged: (val) {
                            dosage = val;
                          },
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              SizedBox(
                height: 50.0,
              ),
              Container(
                height: 40.0,
                width: width * 0.65,
                decoration: BoxDecoration(
                  color: Colors.red,
                  borderRadius: BorderRadius.circular(20.0),
                ),
                child: Center(
                  child: Text(
                    "Pick a time",
                    style: TextStyle(
                      color: Colors.white,
                    ),
                  ),
                ),
              ),
              SizedBox(
                height: 50.0,
              ),
              // Spacer(),
              GestureDetector(
                onTap: () {
                  Fluttertoast.showToast(msg: "Submitted Successfully");
                },
                child: Container(
                  height: 60.0,
                  width: width * 0.9,
                  decoration: BoxDecoration(
                    color: Colors.red,
                    borderRadius: BorderRadius.circular(30.0),
                  ),
                  child: Center(
                    child: Text(
                      "Submit",
                      style: TextStyle(
                        color: Colors.white,
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
