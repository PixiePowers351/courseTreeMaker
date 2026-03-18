def flatten(l):
    last = []
    for x in l:
        if type(x) is list:
            last += flatten(x)
        else:
            last += [x]
    
    return last

i = flatten(["h","e",["l","l",[["0"]]]])
""