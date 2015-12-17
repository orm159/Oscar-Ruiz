"""2. Algorisme que llegeix un nombre i ens indica si és major que 10 o no."""

COMP = input("Escriu el numero a comparar amb 10:")
COMP = int(COMP)

if COMP < 10:
    print("El numero es mes petit que 10")
else:
    print("El numero es mes gran o igual que 10")
