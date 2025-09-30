a = int(input("Adja meg a háromszög a oldalát: "))
b = int(input("Adja meg a háromszög b oldalát: "))
c = int(input("Adja meg a háromszög c oldalát: "))

if a < b+c and b < a+c and c < a+b:
    print("Alkothatnak érvényes háromszöget.")
else :
    print("Nem alkothatnak érvényes háromszöget.")