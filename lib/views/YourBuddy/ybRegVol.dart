import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class VolunteerRegistration extends StatefulWidget {
  @override
  _VolunteerRegistrationState createState() => _VolunteerRegistrationState();
}

class _VolunteerRegistrationState extends State<VolunteerRegistration> {
  final _formKey = GlobalKey<FormState>();
  String name;
  String address;
  String phone;
  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    return Scaffold(
      appBar: AppBar(
        elevation: 0.0,
        backgroundColor: Colors.transparent,
      ),
      body: Container(
        height: double.infinity,
        child: SingleChildScrollView(
          child: Column(
            children: [
              SizedBox(
                height: 50.0,
              ),
              Text(
                "Register yourself",
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  color: Colors.green,
                  fontSize: 30.0,
                ),
              ),
              SizedBox(
                height: 20.0,
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
                          decoration: InputDecoration(hintText: "Name"),
                          validator: (val) {
                            return val.isEmpty ? "Enter Name" : null;
                          },
                          onChanged: (val) {
                            name = val;
                          },
                        ),
                      ),
                      SizedBox(
                        width: width * 0.9,
                        child: TextFormField(
                          decoration: InputDecoration(hintText: "Address"),
                          validator: (val) {
                            return val.isEmpty
                                ? "Enter complete address"
                                : null;
                          },
                          onChanged: (val) {
                            address = val;
                          },
                        ),
                      ),
                      SizedBox(
                        width: width * 0.9,
                        child: TextFormField(
                          decoration: InputDecoration(hintText: "Phone number"),
                          validator: (val) {
                            return val.isEmpty ? "Enter phone number" : null;
                          },
                          onChanged: (val) {
                            phone = val;
                          },
                        ),
                      ),
                      SizedBox(
                        height: 30.0,
                      ),
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 15.0),
                        child: Text(
                          "Upload photo ID for verification (Voter's ID, Driver's License, Aadhar Card):",
                        ),
                      ),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                        height: 30.0,
                        width: 70.0,
                        decoration: BoxDecoration(
                          color: Colors.grey[350],
                          borderRadius: BorderRadius.circular(3.0),
                        ),
                        child: Center(
                          child: Text(
                            "Upload",
                            style: TextStyle(
                              color: Colors.black,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              // SizedBox(
              //   height: 50.0,
              // ),
              // Container(
              //   height: 40.0,
              //   width: width * 0.65,
              //   decoration: BoxDecoration(
              //     color: Colors.red,
              //     borderRadius: BorderRadius.circular(20.0),
              //   ),
              //   child: Center(
              //     child: Text(
              //       "Pick a time",
              //       style: TextStyle(
              //         color: Colors.white,
              //       ),
              //     ),
              //   ),
              // ),
              SizedBox(
                height: 30.0,
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
                    color: Colors.green,
                    borderRadius: BorderRadius.circular(30.0),
                  ),
                  child: Center(
                    child: Text(
                      "Submit for Verification",
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
