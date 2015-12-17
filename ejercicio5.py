"""5. Algorisme que llegeix 3 nombres i diu quin és el major."""
PRIMER = input("Digues els primer numero a comparar:")
PRIMER = int(PRIMER)
SEGON = input("Digues els segon numero a comparar:")
SEGON = int(SEGON)
TERCER = input("Digues el tercer numero a comparar:")
TERCER = int(TERCER)

if PRIMER > SEGON and PRIMER > TERCER:
    print("El primer es el mes gran")
if SEGON > PRIMER  and SEGON > TERCER:
    print("El segon es el mes gran")
if TERCER > PRIMER and TERCER > SEGON:
    print("El tercer es el mes gran")
