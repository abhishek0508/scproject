import 'package:flutter/material.dart';
import 'package:news_app_api/views/YourBuddy/ybRegVol.dart';

class YBHome extends StatefulWidget {
  @override
  _YBHomeState createState() => _YBHomeState();
}

class _YBHomeState extends State<YBHome> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0.0,
        actions: [
          Padding(
            padding: const EdgeInsets.all(15.0),
            child: GestureDetector(
              onTap: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => VolunteerRegistration()));
              },
              child: Icon(
                Icons.add,
                size: 35.0,
              ),
            ),
          ),
        ],
        actionsIconTheme: IconThemeData(
          color: Colors.black54,
        ),
      ),
      body: Container(
        height: double.infinity,
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Text(
                  "YourBuddy",
                  textAlign: TextAlign.start,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 25.0,
                    color: Colors.green,
                  ),
                ),
              ),
              SizedBox(
                height: 15.0,
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Text(
                  "What is YourBuddy?",
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 20.0,
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Text(
                  "YourBuddy is a brand new initiative by us to help you enjoy some quality time with youngsters who love to spend their free time with elders!\n The volunteers are all manually verified by our team and we have made it a priority to include only those who actually want to help and socialize!\n\nRemember to use your mask and maintain social distancing when your buddy arrives. Stay safe!\n\n",
                  // textAlign: TextAlign.center,
                ),
              ),
              SizedBox(
                height: 5.0,
              ),
              Image.asset('assets/images/soc.png'),
            ],
          ),
        ),
      ),
    );
  }
}
