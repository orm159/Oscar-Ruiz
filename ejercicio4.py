"""Ampliació de l'exercici 3 però tractant el cas que siguin iguals."""
PRIMER = input("Digues els primer numero a comparar:")
PRIMER = int(PRIMER)
SEGON = input("Digues els segon numero a comparar:")
SEGON = int(SEGON)


if PRIMER > SEGON:
    print("El primer es el mes gran")
if PRIMER > SEGON:
    print("El segon es el mes gran")
else:
    print("Els numeros son iguals")
