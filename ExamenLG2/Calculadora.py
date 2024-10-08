def metros_pies():
      metros = float(input("Ingrese los metros: "))
      calc1 = metros * 3.28084
      print(f"la conversion es: {calc1} pies")
      try:
          with open("historial.txt", "a") as archivo:
              archivo.write(str(calc1) + "\n")
      except Exception as e:
               print(f"Ocurrió un error al intentar escribir en el archivo: {e}")

def kilos_libras():
    kilos = float(input("Ingrese los kilogramos: "))
    calc2 = kilos * 2.2046
    print(f"la conversion es: {calc2} lb")
    try:
          with open("historial.txt", "a") as archivo:
              archivo.write(str(calc2) + "\n")
    except Exception as e:
               print(f"Ocurrió un error al intentar escribir en el archivo: {e}")

def cm3_onzas():
    cm3 = float(input("Ingrese los cm3: "))
    calc3 = cm3 * 0.03333
    print(f"la conversion es: {calc3} onzas")
    try:
          with open("historial.txt", "a") as archivo:
              archivo.write(str(calc3) + "\n")
    except Exception as e:
               print(f"Ocurrió un error al intentar escribir en el archivo: {e}")

def temperatura():
    cº = float(input("Ingrese los cº: "))
    calc4 = ((cº * 9) / 5) + 32
    print(f"la conversion es: {calc4} fº")
    try:
          with open("historial.txt", "a") as archivo:
              archivo.write(str(calc4) + "\n")
    except Exception as e:
               print(f"Ocurrió un error al intentar escribir en el archivo: {e}")

def mostrar_historial():
    try:
        with open("historial.txt", "r") as archivo:
            print("Historial de conversiones:")
            for linea in archivo:
                print(linea.strip())
    except Exception as e:
        print(f"Ocurrió un error al intentar leer el archivo: {e}")


def main():
    historial = []
    while True:
        print("\nMenú de Conversiones:")
        print("1. Metros a Pies")
        print("2. Kilogramos a Libras")
        print("3. Cm3 a onzas")
        print("4. Cº a Fº")
        print("5. Historial")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '1':
            metros_pies()
        elif opcion == '2':
            kilos_libras()
        elif opcion == '3':
            cm3_onzas()
        elif opcion == '4':
            temperatura()
        elif opcion == '5':
            mostrar_historial()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()