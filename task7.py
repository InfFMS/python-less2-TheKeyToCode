def easy_number_hehehe(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

n = int(input("Введите число: "))
for i in range(2,n+1):
    if(easy_number_hehehe(i) ):
        print(i)
