import json

items = open("item.json","r")
items = json.load(items)

def cmdGet():
    cmd = input()
    mainCmd = cmd.split(" ")[0].strip()
    if len(cmd.split(" --")) == 1:
        otherCmd = {}
    otherCmd = cmd.split(" --")[1:]
    otherCmd = {x.split(":")[0].strip():x.split(":")[1].strip() for x in otherCmd}

    cmdLog = {"main":mainCmd,
                "descr":otherCmd}
    
    return cmdLog

while True:
    cmd = cmdGet()

    if cmdGet['main'] == "add":
        details = {"unitNo":int,
                    "name":int,
                    "workloadHr":int,
                    "completed":bool,
                    "compulsory":bool,
                    "sems":[],
                    "prereq":[[]],
                    "prereqCount":[[]],
                    "next":[],
                    "similiarUnallowed":[],
                    "interest":["Not interested","Mid","Interested"]}
