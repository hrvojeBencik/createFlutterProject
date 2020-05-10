import os

# Changing to flutter folder
os.chdir("/Users/hrvoje/Documents/Projects/Flutter")
projectsFolder = os.getcwd()

# Getting name for a projetc
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
print("Widgets folder made...")
os.makedirs("pages")
print("Pages folder made...")

# Opening the iOS simulator and running the app
print("Opening iOS simulator...")
os.system("open -a Simulator.app")
print("Running the app...")
os.system("flutter run -d iPhone")
