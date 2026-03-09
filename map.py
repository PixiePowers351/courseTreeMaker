import json
import webbrowser

items = open("item.json","r")
items = json.load(items)

def cmdGet():
    cmd = input()
    mainCmd = cmd.split(" ")[0].strip()
    if len(cmd.split(" --")) == 1:
        otherCmd = {}
    otherCmd = cmd.split(" --")[1:]
    otherCmd = {x.split(":")[0].strip():"" if len(x.split(":"))==1 else x.split(":")[1].strip() for x in otherCmd}

    cmdLog = {"main":mainCmd,
                "descr":otherCmd}
    
    return cmdLog

def itemFill(val,info=True):
    global details
    global items

    r = ""

    if type(val) == dict:
        if "ref" in val.keys():
            if val["ref"][:4] == "var_":
                val['ref'] = eval(val['ref'].split("var_")[1],globals())

            print(val['ref'])
        
        if "range" in val.keys():
            r = val['range']

        val = val["t"]

    if val == str:
        return input(info)
    
    if val == int:
        return int(input(info))
    
    if val == float:
        return float(input(info))

    if val == bool:
        val = input(info)
        if val.lower() == "true":
            return True
        else:
            return False
    
    if type(val) == list:
        val = val[0]
        return json.loads(input(info))
    
    return input(info)

def flatten(l):
    last = []
    for x in l:
        if type(x) is list:
            last += flatten(x)
        else:
            last += [x]
    
    return last

while True:
    cmd = cmdGet()

    if cmd['main'] == "add":
        courses = []
        if "blanks" in cmd['descr'].keys():
            missingRecords = []
            for course in items.keys():
                i = flatten(items[course]['prereq']) + items[course]["next"] + flatten(items[course]["similarUnallowed"])
                missingRecords += i
            
            missingRecords = list(set(missingRecords))
            missingRecords = [x for x in missingRecords if x not in items.keys() and "*" not in list(x)]

            courses = missingRecords
            print(f"Found {len(courses)} courses")

        if len(courses) == 0:
            courses.append(input("Enter course code: "))
        
        for course in courses:
            print(course)
            webbrowser.open(f"https://nusmods.com/courses/{course}")

            details = {"name":str,
                        "completed":bool,
                        "sems":[str],
                        "prereq":[str],
                        "prereqCount":{"t":[str],"ref":"var_details['prereq']"},
                        "next":[str],
                        "similarUnallowed":[str],
                        "similarUnallowedCount":[str],
                        "interest":{"t":int,"ref":["Not interested","Mid","Interested"]}}
        

            if course in items.keys():
                i = itemFill({"t":bool,"ref":"var_items['course']"}, info="Do you want to replace data? ")
                if not i:
                    continue
            
            for field in details.keys():
                details[field] = itemFill(details[field], info=f"Enter {field}: ")
            
            items[course] = details

            file = open("item.json","w")
            json.dump(items, file, indent=4)
            file.close()
