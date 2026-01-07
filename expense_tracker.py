import json
import os
import time
from datetime import date
print("Welcome! This will track your expense.")
time.sleep(2)
print("You can add all your expenses and their category and where and why you spent it")
filename="expenses.json"
if os.path.exists(filename):
    with open(filename,"r") as f:
        expenses=json.load(f)
else:
    expenses=[]
total=0
while True:
    today=date.today().isoformat()
    spent=input("Did you spend anything today?(Yes/no):").lower()
    if spent=="no":
        print("No Expenses Today.")
    else:
        expenses_day=[{"day":today}]
        print(f"Add {today}'s expenses")
        while True:
            l=["amount","category","description"]
            dict={}
            for r in l:
                enter=input(f"{r}:")    
                dict[r]=enter
            expenses_day.append(dict)
            add_stop=input("Enter add or stop:")
            if("add"==add_stop.lower()):
                print("add")
            else:
                print('stop')
                break
        expenses.append(expenses_day)
        print(expenses_day)
        for index, i in enumerate(expenses_day):
            print(f"expense{index+1}:")
            if(i=={"day":today}):
                continue
            for r in l:
                print(f"{r}:{i[r]}")
            money=int(i["amount"])
            total+=money
    print(f"Total money spent till now:{total}")
    print(f"Total expenses till now are:\n{expenses}")
    stop=input("Enter exit or continue")
    if(stop.lower()=="exit"):
        break
with open(filename,"w") as f:
    json.dump(expenses,f,indent=4)
print("Done!")
