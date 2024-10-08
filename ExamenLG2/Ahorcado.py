import random

def obtener_palabra_aleatoria():
    with open("palabras.txt", "r") as archivo:
        palabras = [linea.strip() for linea in archivo]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria


def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)


def jugar_ahorcado():
   print("Bienvenido, Adivina el animal secreto")
   palabra_secreta = obtener_palabra_aleatoria()
   letras_adivinadas = []
   intentos_restantes = 10

   while intentos_restantes>0:
       mostrar_tablero(palabra_secreta, letras_adivinadas)
       letra=input("Ingresa una letra: ").lower()

       if letra in letras_adivinadas:
           print("Esa letra ya existe, intenta nuevamente.")
           continue
       
       if letra in palabra_secreta:
           letras_adivinadas.append(letra)
           if set(letras_adivinadas)==set(palabra_secreta):
               print("felicidades mipan@, ganaste")
               break
       else:
               intentos_restantes-=1
               print(f"Letra incorrecta, te quedan {intentos_restantes}")
   if intentos_restantes==0:
             print(f"Has perdido mipan@, la oalabra era: {palabra_secreta}")

jugar_ahorcado()
