import json

courseInfo = open("itemDetails.json","r",encoding="utf-8")
courseInfo = json.load(courseInfo)

def saveFile(name, item):
    f = open(name,"w",encoding="utf-8")
    json.dump(item, f, indent=2)
    f.close()

file = open("basics.json","r")
file = json.load(file)

fileModules = [x['moduleCode'] for x in file]
courseInfo = [x for x in courseInfo if x['moduleCode'] not in fileModules]

for course in courseInfo:
    key = course['moduleCode']
    details = {"name":course['title'],
    "year":"2025-2026",
    "department":course['department'],
    "faculty":course['faculty'],
    "details":course['description'],
    "prereq":[],
    "prereqCount":[0],
    "next":[],
    "similarUnallowed":[],
    "similarUnallowedCount":[0]}
    
    #check for prereqs and update based on my preferences
    ""