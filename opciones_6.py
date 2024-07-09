print("ESTE ES UN ALGORITMO DONDE PUEDE ELEGIR ENTRE VER")
print("SU IMC, SU PGC Y SU TASA METABOLICA BASAL")

print("opcion 1: IMC")
print("opcion 1: PGC")
print("opcion 1: TMB")

opcion= int(input("elija la opcion 1, 2, 3: "))

if opcion == 1:
    peso = float(input("Digite su peso: "))

    altura = float(input("digite su altura: ")) 

    imc= peso / (altura**2)

    print(f"su IMC es {imc}")

