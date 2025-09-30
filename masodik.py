a = int(input("Add meg az első oldal hosszát:"))
b = int(input("Add meg a második opldal hosszát:"))
c = int(input("Add meg a haradik oldal hosszát:"))

if a < (b + c) and b < (a + c) and c < (a + b):
    print("A megadott szakaszok alkothatnak háromszöget.")
else:
    print("A megadott szakaszok nem alkothatnak háromszöget.")





