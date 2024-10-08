import random

print("----------")
print("Piedra, papel o Tijera")
print("----------")

listadeobjetos = ["P", "p", "T"]

puntosdeljugador = 0
puntosdelcomputador = 0
i = 1

vecesajugar = int(input("Cuantas veces desea jugar?"))

while i <= vecesajugar:
    selecciondelpc = str(random.choice(listadeobjetos))
    seleccionusuario = input("Escojes: Piedra, papel o Tijera: (usa: P, p, T):").upper()

    if seleccionusuario == selecciondelpc:
        print("Empate, tu y la pc Escojieron lo mismo")

    elif seleccionusuario == "P":
        print("La pc escojio: ", selecciondelpc)
        if selecciondelpc == "p":
            print("Perdiste, El papel cubre a la piedra")
            puntosdelcomputador += 1
        else:
            print("Ganaste, La piedra daña a la tijera")
            puntosdeljugador += 1
    
    elif seleccionusuario == "p":
        print("La pc escojio: ", selecciondelpc)
        if selecciondelpc == "T":
            print("Perdiste, La tijera corta el papel")
            puntosdelcomputador += 1
        else:
            print("Ganaste, El papel cubre a la piedra")
            puntosdeljugador += 1


    else:
        print(":(")

    print("\n\t*****Puntos*****")
    print(f"\t Tu: {puntosdeljugador}  --- Pc: {puntosdelcomputador} ")
    print(f"Juego #:[{i}]")
    print("================")


    i += 1

    print("\n\n#### Juego Terminado ####")
    print("********************************")

    if puntosdeljugador < puntosdelcomputador:
        print("Perdiste la partida, gano la pc con una puntuacion de: ", puntosdelcomputador)
    elif puntosdeljugador == puntosdelcomputador:
        print("La partida quedo empatada, juega nuevamente")
    else:
        print("Tu ganaste, el marcador es de: ", puntosdeljugador)