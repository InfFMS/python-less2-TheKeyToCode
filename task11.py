
while(1):
    a1,b1=map(int,input("Введите первый отрезок:").split())
    a2,b2=map(int,input("Введите первый отрезок:").split())
    if(a1<a2):
        if(b1<a2):
            print("Empty")
        elif(b1==a2):
            print(b1)
        else:
            if(b1>b2):
                print(a2,b2)
            else:
                print(a2,b1)
    else:
        if(b2<a1):
            print("Empty")
        elif(b2==a1):
            print(b2)
        else:
            if(b2>b1):
                print(a1,b1)
            else:
                print(a1,b2)

