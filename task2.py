months = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
m = int(input("Ввелите номер меяца: "))
if(m<1 or m>12):
    print("Неверный номер меяца")
else:
    print(months[m-1])
