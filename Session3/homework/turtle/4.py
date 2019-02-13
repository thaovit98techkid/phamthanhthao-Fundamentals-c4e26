sl = int (input ("Dan cuu cua ban co bao nhieu con"))
a = []
for j in range (sl ):
    x = int (input ("Can nang cua chu cuu dau tien la: "))
    a.insert(j, x)
print ("Hello, my name is Thao and these are my ship size")
for j in range (sl):
    print (a[j], end = " , ")
print (" ] ")
tong = a[0]
for i in range (0,sl):
     if tong < a[i]:
        tong = a[i]
print ("\nNow my biggest sheep has size ", tong, " let's shear it ")
lay = a.index (tong)
a[lay] = int ("8")
print ("After shearing, here is my flock \n")
for i in range (sl):
    print ('[ ', a[i], )
tongkg = 0 
for i in range (3):
    print ("Month " , i+1)
    print ("One month hass passed, now here is my flock")
    for i in range (sl):
        a[i] = a[i] + 50 
    for i in range (sl):
        print (a[i], sep = " , ")
    tong = a[0]
    for i in range (0,sl):
        if tong < a[i]:
            tong = a[i]
    for i in range (0,sl):
        tongkg = tongkg + a[i]
    print ("Now my biggest sheep has size ", tong, " let's shear it ")
    print ("After shearing, here is my flock \n")
    lay = a.index (tong)
    a[lay] = 8
    for i in range (sl):
        print ('[ ', a[i], )

print ("My flock has size in total: ", tongkg )
tien = tongkg *2
print (" i would get ", tongkg , " *2$ = ", tien )