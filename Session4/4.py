
for i in range (4):
    for j in range (4):
        if i == 1 and j == 1:
            print (" P ", end = " ") 
        elif i == 2 and j == 2:
            print (" B ", end = " ")
        elif i == 3 and j == 2:
            print (" S ", end = " ")
        else:
            print (" - ", end = " ")
    print ()
player = {
    "x" : 1,
    "y" : 1
}
box = {
    "x" : 2,
    "y" : 2
}
point = {
    "x" : 2,
    "y" : 3
}
while True:
    player_input = input (print ("Your next move? " )).upper()
    if player_input == "A":
        player ["x"] -= 1
    elif player_input == "D":
        player ["x"] +=1
    elif player_input == "S":
        player ["y"] +=1
    elif player_input == "W":
        player ["y"] -=1 
    print (player)
    if player ["y"] == 3 and player ["x"] == 2:
        print ("You win")
        break