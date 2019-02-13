iteams = ["T - shirt" , "Swearer"]
a = input (print ("Welcome to our shop, what do you want (C, R, U, D)?") )
if a == "R":
    print (iteams, sep = " , " )
if a == "C":
    them = input (print ("Enter new item: "))
    iteams.append (them)
    print (*iteams, sep = " , ")
if a == "U":
    b = int (input ("Update position? ") )
    new_iteam = input ("New item? ")
    iteams.insert(b-1, new_iteam)
    print (*iteams, sep = " , ")
if a == "D":
    del_iteam = int (input ("Delete position? "))
    iteams.pop(del_iteam-1)
    print (iteams)