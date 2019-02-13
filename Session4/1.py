gold =  ["500"]
pouch = ["flint", 'twine' , 'gemstone']
backpack = ['xylophone', 'dagger', 'bedroll', 'bread loaf']
for i in range (len(gold)):
    print ( gold[i] )
for i in range (len(pouch)):
    print ( pouch[i] )
for i in range (len(backpack)):
    print ( backpack[i] )
pocket = ['seashell', 'strange berry', 'lint']
backpack.remove('dagger')
for i in range (len(backpack)):
    print ( backpack[i] )
gold.append('50')
for i in range (len(gold)):
    print ( gold[i] )