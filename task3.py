n = int(input("Введите кол-во лет: "))
if(n%10==1):
    print(n,"год")
elif(n%10==0 or (n%10<=9 and n%10>4)):
    print(n, "лет")
else:
    print(n, "года")
