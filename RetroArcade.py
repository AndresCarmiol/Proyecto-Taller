import os

ETAPAS_AHORCADO = [
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
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]

MAX_INTENTOS_AHORCADO = len(ETAPAS_AHORCADO) - 1

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


# Juego 2: Ahorcado

def mostrar_estado_ahorcado(intentos_fallidos, letras_usadas, progreso):
    print(ETAPAS_AHORCADO[intentos_fallidos])
    print(f"\n  Palabra: {' '.join(progreso)}")
    print(f"  Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else '-'}")
    print(f"  Intentos fallidos: {intentos_fallidos}/{MAX_INTENTOS_AHORCADO}\n")

def obtener_letra_usuario(letras_usadas):
    while True:
        entrada = input("  Ingresa una letra: ").strip().lower()
        if len(entrada) == 1 and entrada.isalpha():
            if entrada in letras_usadas:
                print("  Ya usaste esa letra. Elige otra.")
            else:
                return entrada
        else:
            print("  Entrada no válida. Ingresa una sola letra.")



ejecutar_menu()
