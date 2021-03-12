import 'package:flutter/material.dart';
import 'package:news_app_api/views/pillbox/newReminder.dart';

class PillBoxHome extends StatefulWidget {
  @override
  _PillBoxHomeState createState() => _PillBoxHomeState();
}

class _PillBoxHomeState extends State<PillBoxHome> {
  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
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
                height: height * 0.05,
              ),
              Center(
                child: Text(
                  "My Pill Box",
                  style: TextStyle(
                    color: Colors.red,
                    fontWeight: FontWeight.bold,
                    fontSize: 35.0,
                  ),
                ),
              ),
              SizedBox(
                height: 8.0,
              ),
              Text(
                "Touch the + to add a new reminder",
                style: TextStyle(
                  color: Colors.grey,
                  fontSize: 20.0,
                ),
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(context,
              MaterialPageRoute(builder: (context) => NewReminderPage()));
        },
        backgroundColor: Colors.red,
        child: Icon(
          Icons.add,
        ),
      ),
    );
  }
}
