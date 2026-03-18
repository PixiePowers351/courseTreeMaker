import json
de = ["unitNo", "workloadHr","compulsory","graded"]

file = open("item.json","r")
file = json.load(file)

for x in file.keys():
    for y in de:
        if y in file[x].keys():
            del file[x][y]
    
f = open("item.json","w")
json.dump(file,f,indent=4)
f.close()