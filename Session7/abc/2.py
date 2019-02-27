def is_inside (diem,hcn):
    if diem[0]<hcn[0] or diem[1]<hcn[1] or  diem[0] > hcn[3] + hcn[0] or diem[1]> hcn[1]+hcn[2]:
        check = False
    else :
        check = True 
    print (check)
is_inside ([200, 120], [140, 60, 100, 200])
is_inside ([100,120], [140,60,100, 200 ])
