import time
import random
import requests
import json
import os

timeDelay = random.randint(100,300)/100
timer = time.time()
count = 4
countLimit = 10


class accessState:
    allItems = False

def rateLimit():
    global timeDelay
    global timer
    global count
    global countLimit 

    if time.time() - timer < timeDelay:
        time.sleep(timeDelay - (time.time() - timer))

    timer = time.time()
    timeDelay = random.randint(300,1000)/100

    if count > countLimit:
        print("System cooling down....!")
        time.sleep(60)
        
        count = 0
    else:
        count += 1


def request(url):
    rateLimit()
    response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    webpage = json.loads(response.text)

    return webpage

def saveFile(name, item):
    f = open(name,"w",encoding="utf-8")
    json.dump(item, f, indent=2)
    f.close()

#save all items
if accessState.allItems:
    allItems = request('https://api.nusmods.com/v2/2025-2026/moduleList.json')
    saveFile("allItems.json",allItems)
else:
    allItems = open("allItems.json","r",encoding="utf-8")
    allItems = json.load(allItems)

#get all codes
yearCodes = ["2025-2026","2024-2025","2023-2024","2022-2023","2021-2022","2020-2021"]
codes = [x['moduleCode'] for x in allItems]
print(f"Found info of {len(codes)}")

itemDetails = open("itemDetails.json","r",encoding="utf-8")
itemDetails = json.load(itemDetails)
presentCodes = [x['moduleCode'] for x in itemDetails]

codes = [x for x in codes if x not in presentCodes]
x = len(presentCodes)

for course in codes:
    print(f"{x+1}/{len(presentCodes)+len(codes)}")

    moduleInfo = request(f"https://api.nusmods.com/v2/2025-2026/modules/{course}.json")
    itemDetails.append(moduleInfo)
    saveFile("itemDetails.json",itemDetails)

    x += 1
    os.system('cls')