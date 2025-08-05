import os
os.mkdir("data")
for i in range(0,5):
    os.mkdir(f"data/Day{i+1}")


import os

if(not os.path.exists("data")):# check if data exist or not
    os.mkdir("data")

for i in range(0,5):
    os.mkdir(f"data/Day{i+1}")


