import os
import random

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

PALABRAS = [
    "python", "computadora", "programa", "teclado", "monitor",
    "algoritmo", "variable", "funcion", "bucle", "lista",
    "diccionario", "cadena", "entero", "flotante", "logico",
    "modulo", "clase", "objeto", "metodo", "herencia",
    "recursion", "compilador", "interprete", "memoria", "proceso",
    "archivo", "sistema", "red", "internet", "servidor",
    "cliente", "base", "dato", "tabla", "consulta"
    ]

MAX_INTENTOS_AHORCADO = len(ETAPAS_AHORCADO) - 1  # 7 partes del cuerpo

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
    """
    Muestra el estado actual del juego de ahorcado.

    Args:
        intentos_fallidos (int): Cantidad de fallos acumulados.
        letras_usadas (list): Lista de letras ya usadas por el jugador.
        progreso (list): Lista de caracteres con letras adivinadas y guiones.
    """
    print(ETAPAS_AHORCADO[intentos_fallidos])
    print(f"\n  Palabra: {' '.join(progreso)}")
    print(f"  Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else '-'}")
    print(f"  Intentos fallidos: {intentos_fallidos}/{MAX_INTENTOS_AHORCADO}\n")


def obtener_letra_usuario(letras_usadas):
    """
    Solicita y valida una letra al usuario (A-Z, ignora mayúsculas).

    Args:
        letras_usadas (list): Letras ya ingresadas para evitar repeticiones.

    Returns:
        str: Letra válida y no repetida ingresada por el usuario.
    """
    while True:
        entrada = input("  Ingresa una letra: ").strip().lower()
        if len(entrada) == 1 and entrada.isalpha():
            if entrada in letras_usadas:
                print("  Ya usaste esa letra. Elige otra.")
            else:
                return entrada
        else:
            print("  Entrada no válida. Ingresa una sola letra.")


def jugar_ahorcado():
    """
    Juego 'Ahorcado'.

    El programa elige una palabra aleatoria. El jugador adivina letra por letra.
    Dispone de MAX_INTENTOS_AHORCADO fallos antes de perder.
    Al terminar se revela la palabra si no fue adivinada.
    """
    mostrar_titulo("Ahorcado")
    palabra_secreta = random.choice(PALABRAS)
    progreso = ["_"] * len(palabra_secreta)
    letras_usadas = []
    intentos_fallidos = 0
    gano = False

    print(f"  La palabra tiene {len(palabra_secreta)} letras.\n")

    while intentos_fallidos < MAX_INTENTOS_AHORCADO:
        mostrar_estado_ahorcado(intentos_fallidos, letras_usadas, progreso)

        if "_" not in progreso:
            gano = True
            break

        letra = obtener_letra_usuario(letras_usadas)
        letras_usadas.append(letra)

        if letra in palabra_secreta:
            for i, caracter in enumerate(palabra_secreta):
                if caracter == letra:
                    progreso[i] = letra
            print(f"  ✓ ¡Correcto! La letra '{letra}' está en la palabra.\n")
        else:
            intentos_fallidos += 1
            print(f"  ✗ La letra '{letra}' no está en la palabra.\n")

    # Verificar si ganó después del último intento
    if "_" not in progreso:
        gano = True

    if gano:
        print(f"\n  ¡Ganaste! La palabra era: {palabra_secreta}")
    else:
        print(ETAPAS_AHORCADO[MAX_INTENTOS_AHORCADO])
        print(f"\n  ¡Perdiste! La palabra era: {palabra_secreta}")


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
