n = int (input ("Nhap so bat ky\t"))
a =  n//2
if n % 2 != 0 :
    print ("x", end = "")
    for i in range (1,a+1):
        print (" * ",end = "x")
else :
    for i in range (1,a+1):
        print ("x", end = " * ")