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

# Going into project folder and then /lib folder
os.chdir(projectsFolder+"/"+projectName+"/lib")

# Making folders that I ususally make for my Flutter projects
os.makedirs("widgets")
print("Widgets folder made...")
os.makedirs("pages")
print("Pages folder made...")
