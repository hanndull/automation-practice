import os
import sys
import datetime

req_path = input("Enter your path: ")

if not os.path.exists(req_path):
    print("Please provide valid path ")
    sys.exit(1)

if os.path.isfile(req_path):
    print("Please provide directory path ")
    sys.exit(2)

age = int(input("Look at files that are {x} number of days, or older: "))
today = datetime.datetime.now()

for file in os.listdir(req_path):
    file_path = os.path.join(req_path, file)
    
    if os.path.isfile(file_path):
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        days_old = (today - file_creation_date).days
        
        if days_old > age:
            print(file_path, days_old)

