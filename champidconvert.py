ids = {}
inpt = None

while inpt != "":
    print(inpt)
    inpt = input()
    id = inpt[0:inpt.index(":")]
    champ = inpt[inpt.index(":")+2:]
    ids[str(id)] = champ
    print(ids)

print(ids)