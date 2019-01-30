cm = int (input ("Moi ban nhap chieu cao (cm) "))
kg = int (input ("Moi ban nhap can nang (kg) "))
doi = cm/100
bmi = kg / ( doi * doi )
print ("Chi so BMI cua ban la: ", bmi)
if bmi < 16:
    print ("Ban dang thieu can 1 cach nghiem trong :( ")
elif bmi <18.5:
    print ("Ban dang thieu can :(  ")
elif bmi <25:
    print ("Ban dang rat on hay phat huy nhe :D ")
elif bmi <30:
    print ("Ban dang thua can :( ")
else:
    print ("Beo phi ruii ")