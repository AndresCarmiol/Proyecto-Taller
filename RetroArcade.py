import os
import random

etapas_ahorcado = [
    """
  +---+
      |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

intentos_maximos_ahorcado = len(etapas_ahorcado) - 1

lista_de_palabras = [
    "barril",
    "bastón",
    "casa",
    "lápiz",
    "tijeras",
    "pizza",
    "torre",
    "comida",
    "queso",
    "ciudad",
    "neumonoultramicroscopicsilicovolcanoconiosis"
    "lobo",
    "gato",
    "perro",
    "trebol",
    "chinchilla",
    "contendiente",
    "dictamen",
    "presidente",
    "ausente",
    "ajedrez",
    "pelota",
    "ayuda",
    "idea",
    "supercalifragilisticoespialidoso",
    "queso",
    "ritmo",
]


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_titulo(titulo):
    linea = "=" * 50
    print(f"\n{linea}")
    print(f"   {titulo.upper()}")
    print(f"{linea}\n")


def presionar_enter():
    input("\nPresiona Enter para continuar...")


def mostrar_menu_principal():
    mostrar_titulo("Retro Arcade")
    print("  [1] Adivina el número")
    print("  [2] Ahorcado")
    print("  [3] Código")
    print("  [4] Revoltijo de palabra")
    print("  [5] Salir")
    print()
    opcion = input("  Selecciona una opción: ").strip()
    return opcion


def ejecutar_menu():
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_principal()

        if opcion == "1":
            limpiar_pantalla()
            jugar_adivina_numero()
            presionar_enter()
        elif opcion == "2":
            limpiar_pantalla()
            jugar_ahorcado()
            presionar_enter()
        elif opcion == "3":
            limpiar_pantalla()
            jugar_codigo()
            presionar_enter()
        elif opcion == "4":
            limpiar_pantalla()
            jugar_revoltijo()
            presionar_enter()
        elif opcion == "5":
            limpiar_pantalla()
            print("\n  ¡Hasta luego! Gracias por jugar Retro Arcade.\n")
            break
        else:
            print("\n  Opción no válida. Intenta de nuevo.")
            presionar_enter()


def jugar_adivina_numero():
    pass


def jugar_ahorcado():
    pass


def jugar_codigo():
    pass


def jugar_revoltijo():
    palabra = random.choice(lista_de_palabras)
    palabra_desordenada = desordenar_palabra(palabra)
    intentos = 3
    while intentos > 0:
        actualizar_revoltijo(palabra_desordenada, intentos)
        respuesta = input("¡Adivina la palabra!: ")
        if respuesta == palabra:
            print("\n🎊🎉🎈 ¡Felicitaciones, adivinaste la palabra! 🎈🎉🎊")
            return
        intentos -= 1
        if intentos > 0:
            print("\n❌ Incorrecto, intentalo de nuevo... ❌")
            input()
    actualizar_revoltijo(palabra_desordenada, intentos)
    print(f"¡Adivina la palabra!: {respuesta}")
    print("\n❌ Incorrecto ❌\n")
    print(f"La palabra correcta era: {palabra}")
    print("Mejor suerte la próxima...")


def desordenar_palabra(palabra):
    lista_temporal = list(palabra)
    nueva_lista = []
    while len(lista_temporal) > 0:
        indice_random = random.randint(0, len(lista_temporal) - 1)
        letra = lista_temporal.pop(indice_random)
        nueva_lista.append(letra)
    return "".join(nueva_lista)


def actualizar_revoltijo(palabra_desordenada, intentos):
        limpiar_pantalla()
        mostrar_titulo("Revoltijo de Palabras")
        print(f"{palabra_desordenada}\n")
        print(f"Intentos restantes: {intentos}")


# ============================================================================================= #

ejecutar_menu()
