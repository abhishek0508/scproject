import 'package:flutter/material.dart';
import 'package:news_app_api/views/discoverPage.dart';
import 'package:news_app_api/views/homepage.dart';
import 'package:news_app_api/views/pillbox/pillboxhome.dart';

class MyBottomNavBar extends StatefulWidget {
  @override
  _MyBottomNavBarState createState() => _MyBottomNavBarState();
}

class _MyBottomNavBarState extends State<MyBottomNavBar> {
  final List<Widget> _children = [
    DiscoverHome(),
    PillBoxHome(),
  ];
  int _currentIndex = 0;

  void barFunction(int index) {
    setState(() {
      _currentIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _children[_currentIndex],
      backgroundColor: Colors.white,
      bottomNavigationBar: new Theme(
        data: Theme.of(context).copyWith(
          canvasColor: Colors.red,
          primaryColor: Colors.white,
          // disabledColor: Colors.grey,

          textTheme: Theme.of(context)
              .textTheme
              .copyWith(caption: new TextStyle(color: Colors.white)),
        ),
        child: BottomNavigationBar(
          onTap: barFunction,
          elevation: 3.0,
          currentIndex: _currentIndex,
          items: [
            BottomNavigationBarItem(
              icon: new Icon(Icons.search),
              title: new Text("Discover"),
            ),
            BottomNavigationBarItem(
              icon: new Icon(Icons.chat_bubble),
              title: new Text("Chat"),
            ),
            BottomNavigationBarItem(
              icon: new Icon(Icons.face),
              title: new Text("Profile"),
            ),
          ],
        ),
      ),
    );
  }
}
