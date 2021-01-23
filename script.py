import os

# Changing to flutter folder
os.chdir("/Users/hrvojebencik/Documents/Projects/Flutter")
projectsFolder = os.getcwd()

# Getting name for a project
print("Enter name for your project:")
projectName = input()

# Making a Flutter project
print("Creating Flutter project...")
os.system("flutter create " + projectName)

# Opening project folder in VS Code
os.chdir(projectsFolder+"/"+projectName)
print("Opening project folder in VS Code...")
os.system("code .")

# Going into project folder and then /lib folder
os.chdir(projectsFolder+"/"+projectName+"/lib")

# Making folders that I ususally make for my Flutter projects
os.makedirs("widgets")
print("Widgets folder created...")
os.makedirs("screens")
print("Screens folder created...")
os.makedirs("models");
print("Models foldred created...")

MAIN_CONTENT = '''import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
      child: Text("Hello World"),
        ),
      ),
    );
    
  }
}'''

#Changing content of main.dart, setting up default project
mainFile = projectsFolder+"/"+projectName+"/lib/main.dart";
with open(mainFile, 'w') as filetowrite:
    filetowrite.write(MAIN_CONTENT)
print("Updated main.dart content")

# Opening the iOS simulator and running the app
print("Opening iOS simulator...")
os.system("open -a Simulator.app")
print("Running the app...")
os.system("flutter run -d iPhone")
