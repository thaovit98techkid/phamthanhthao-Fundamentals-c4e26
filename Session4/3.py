Dovui1 = {
    "Dapan1" : 35,
    "Dapan2" : 36,
    "Dapan3" : 40,
    "Dapan4" : 44 
}
print ("Answer the follwing algebra question")
print ("If x = 8 , then what is the value of 4(x + 3) ? ")
print ("1. ",Dovui1["Dapan1"])
print ("2. ",Dovui1["Dapan2"])
print ("3. ",Dovui1["Dapan3"])
print ("4. ",Dovui1["Dapan4"])

x = int(input (print ("Your choice: ")))
if x == 4:
    print ("Bingo")
    dem = 1
else :
    print (":(")
    dem = 0 
Dovui2 = {
    "Dapan1": "About 55",
    "Dapan2" : "About 65",
    "Dapan3" : "About 75",
    "Dapan4": "About 85"
}
print ("1. ",Dovui2[ "Dapan1"])
print ("2. ",Dovui2[ "Dapan2"])
print ("3. ",Dovui2[ "Dapan3"])
print ("4. ",Dovui2[ "Dapan4"])
print ("You correctly answer ", dem, "out of 2 questions" )
print ("Estimate this answer (exact calculation not needed")
print ("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? ")
x = int (input (print ("Your choice: ")))
if x == 2:
    print ("Bingo")
    dem += 1 
print ("You correctly answer ", dem, "out of 2 questions" )
