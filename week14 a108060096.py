a = float(input("請輸入身高”))
b = float(input("請輸入體重”))
c = b/(a*a)
print(c)
if  c>=30:
    print("肥胖“)    
elif c>=20:
    print("過重“)
elif c>=18.5:
    print("正常“)
else:
    print("體重過低")
    

    



