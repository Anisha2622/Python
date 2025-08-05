import os
folders = os.listdir("data")

print(os.getwd()) # print working directory

os.chdir("/Users") # change working directory
print(os.getcwd())

for folders in folders:
    print(folders) #print all folders
    print(os.listdir(f"data/{folders}")) # show contain in given files 