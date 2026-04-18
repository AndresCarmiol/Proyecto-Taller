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


def limpiar_pantalla() -> None:
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_titulo(titulo: str) -> None:
    """Escribe el título especificado y lo rodea con dos lineas decorativas de símbolos.
    
    Argumentos:
        titulo (str): Texto que se mostrará como título.
    """
    linea = "=" * 50
    print(f"\n{linea}")
    print(f"   {titulo.upper()}")
    print(f"{linea}\n")


def presionar_enter() -> None:
    """Indica al usuario que debe presionar Enter para continuar."""
    input("\nPresiona Enter para continuar...")


def mostrar_menu_principal() -> str:
    """Muestra la lista de opciones del menu principal.

    Devuelve:
        str: El texto escrito por el usuario
    """
    mostrar_titulo("Retro Arcade")
    print("  [1] Adivina el número")
    print("  [2] Ahorcado")
    print("  [3] Código")
    print("  [4] Revoltijo de palabra")
    print("  [5] Salir")
    print()
    opcion = input("  Selecciona una opción: ").strip()
    return opcion


def ejecutar_menu() -> None:
    """Inicia y procesa la lógica del Menú Principal."""
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


def jugar_adivina_numero() -> None:
    """Inicia y procesa la lógica del juego 'Adivina el Número'."""
    pass

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


def jugar_ahorcado() -> None:
    """Inicia y procesa la lógica del juego 'Ahorcado'."""
    pass


def jugar_codigo() -> None:
    """Inicia y procesa la lógica del juego 'Código'."""
    pass


def jugar_revoltijo() -> None:
    """Inicia y procesa la lógica del juego 'Revoltijo de Palabras'."""
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


def desordenar_palabra(palabra: str) -> str:
    """Desordena las letras de una palabra.

    Argumentos:
        palabra (str): Palabra por desordenar.
    
    Devuelve:
        str: La palabra desordenada.
    """
    lista_temporal = list(palabra)
    nueva_lista = []
    while len(lista_temporal) > 0:
        indice_random = random.randint(0, len(lista_temporal) - 1)
        letra = lista_temporal.pop(indice_random)
        nueva_lista.append(letra)
    return "".join(nueva_lista)


def actualizar_revoltijo(palabra_desordenada: str, intentos: str) -> None:
    """Limpia la consola y reescribe: el título, la palabra desordenada y los intentos restantes del juego 'Revoltijo de Palabras'.
    
    Argumentos:
        palabra_desordenada (str): Palabra desordenada por reescribir.
        
        intentos (str): Número de intentos al momento de reescribir.
    """
    limpiar_pantalla()
    mostrar_titulo("Revoltijo de Palabras")
    print(f"{palabra_desordenada}\n")
    print(f"Intentos restantes: {intentos}")


# ============================================================================================= #


ejecutar_menu()
