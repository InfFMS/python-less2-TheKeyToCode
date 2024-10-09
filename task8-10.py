def print_field(field):
    for n in range(2,10):
        s=""
        for m in range(2,10):
            s+= field[n][m] + " "
        print(s)
    
field = []
for i in range(0,12):
    field.append([".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."])
type_chess = input("Введите только один из символов на русском(С - Слон, К - Конь, Ф - Ферзь): ")
column, line = map(int,input().split())
column+=1
line+=1
column1, line1 = map(int,input().split())
column1+=1
line1+=1

if(type_chess == "С" or type_chess == "C"):
    for i in range(2,11):
        for j in range(2,11):
            if(i + j == column+line or line - j == column-i):
                field[i][j] = "*"
if(type_chess == "K" or type_chess == "К" or type_chess == "Л" or type_chess == "R"):
    field[column-1][line-2] = "*"
    field[column+1][line-2] = "*"
    field[column-1][line+2] = "*"
    field[column+1][line+2] = "*"
    field[column-2][line-1] = "*"
    field[column+2][line-1] = "*"
    field[column-2][line+1] = "*"
    field[column+2][line+1] = "*"
if (type_chess == "Ф" or type_chess == "A"):
    for i in range(2,11):
        for j in range(2,11):
            if(i + j == column+line or line - j == column-i or i == column or j == line):
                field[i][j] = "*"
field[column][line]=type_chess
print_field(field)
if(field[column1][line1]=="*"):
    print("YES")
else:
    print("NO")
