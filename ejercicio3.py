"""3. Algorisme que llegeix dos nombres i mostra com a resultat
    quin és el més gran."""

PRIMER = input("Digues els primer numero a comparar:")
PRIMER = int(PRIMER)
SEGON = input("Digues els segon numero a comparar:")
SEGON = int(SEGON)


if PRIMER > SEGON:
    print("El primer es el mes gran")
if SEGON > PRIMER:
    print("El segon es el mes gran")
