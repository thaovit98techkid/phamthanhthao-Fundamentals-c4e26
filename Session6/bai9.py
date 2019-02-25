dsach = []
ketqua = []
sl = int (input (print ("So luong so ")))
for i in range (sl):
    n = int (input (print ("Moi nhap ")))
    dsach.append(n)
for i in range (sl):
    def get_even_list (x = dsach[i]):
        if x % 2 ==0:
            ketqua.append(x)
    get_even_list()
print (ketqua)