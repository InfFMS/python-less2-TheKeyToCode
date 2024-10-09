for n in range(100,1000):
    if(n == int((n/100))**3 + int(((n/10)%10))**3 + int((n%10))**3):
        print(n)
