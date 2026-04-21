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

PALABRAS_AHORCADO = [
    "python",
    "computadora",
    "programa",
    "teclado",
    "monitor",
    "algoritmo",
    "variable",
    "función",
    "bucle",
    "lista",
    "diccionario",
    "cadena",
    "entero",
    "flotante",
    "lógico",
    "módulo",
    "clase",
    "objeto",
    "método",
    "herencia",
    "recursión",
    "compilador",
    "interprete",
    "memoria",
    "proceso",
    "archivo",
    "sistema",
    "red",
    "internet",
    "servidor",
    "cliente",
    "base",
    "dato",
    "tabla",
    "consulta"
    ]

PALABRAS_REVOLTIJO = [
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

MAX_INTENTOS_AHORCADO = len(ETAPAS_AHORCADO) - 1  # 7 partes del cuerpo

LONGITUD_CODIGO = 4
MAX_INTENTOS_CODIGO = 7

numero_secreto = random.randint(1, 100)
numeros_incorrectos = []
intentos = 6


def limpiar() -> None:
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_titulo(titulo: str) -> None:
    """Escribe el título especificado en mayúsculas y lo rodea con dos lineas decorativas de símbolos.
    
    Argumentos:
        titulo (str): Texto que se mostrará como título.
    """
    linea = "=" * 50
    print(f"\n{linea}")
    print(f"   {titulo.upper().center(44)}")
    print(f"{linea}\n")


def presionar_enter() -> None:
    """Indica al usuario que debe presionar Enter para continuar."""
    input("\nPresiona Enter para continuar...")


def mostrar_menu_principal() -> str:
    """Muestra la lista de opciones del menu principal.

    Retorna:
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
        limpiar()
        opcion = mostrar_menu_principal()

        if opcion == "1":
            limpiar()
            jugar_adivinar_numero()
            presionar_enter()
        elif opcion == "2":
            limpiar()
            jugar_ahorcado()
            presionar_enter()
        elif opcion == "3":
            limpiar()
            jugar_codigo()
            presionar_enter()
        elif opcion == "4":
            limpiar()
            jugar_revoltijo()
            presionar_enter()
        elif opcion == "5":
            limpiar()
            print("\n  ¡Hasta luego! Gracias por jugar Retro Arcade.\n")
            break
        else:
            print("\n  Opción no válida. Intenta de nuevo.")
            presionar_enter()

# === JUEGO ADIVINA EL NUMERO === #

def mostrar_menu():
    """Muestra el menú principal del juego."""
    limpiar()
    mostrar_titulo("MENÚ PRINCIPAL")
    print('\n[1]. Jugar a Adivinar el Número')
    print('[2]. Salir')
    
    opcion = input('\nRespuesta: ')
    if opcion == '1':
        jugar_adivinar_numero()
    elif opcion == '2':
        print('\n¡Gracias por jugar! 👋')
        exit()
    else:
        print('\n==================================================\n     No es una opción válida\n==================================================')
        input('\n-Pulsa ENTER para continuar-\n')
        mostrar_menu_principal()


def reinicio():
    """Reinicia las variables del juego."""
    global numero_secreto, numeros_incorrectos, intentos
    numero_secreto = random.randint(1, 100)
    numeros_incorrectos = []
    intentos = 6


def no_es_un_numero():
    """Maneja cuando el usuario no ingresa un número."""
    limpiar()
    print('\n==================================================\n              No es un número entero\n==================================================\n')
    input('\n-Pulsa ENTER para continuar-\n')
    return adivinar()


def numero_es_incorrecto(numero):
    """Procesa cuando el número ingresado es incorrecto."""
    global intentos, numeros_incorrectos
    
    if numero > 100 or numero < 1:
        limpiar()
        print('\n==================================================\n     El valor del número está entre 1 y 100\n==================================================\n')
        input('-Pulse ENTER para volver a adivinar-')
        return adivinar()
    
    if numero not in numeros_incorrectos:
        if numero < numero_secreto:
            limpiar()
            print(f'\n==================================================\n                     Más alto\n            El {numero} no es el número secreto\n==================================================')
        elif numero > numero_secreto:
            limpiar()
            print(f'\n==================================================\n                     Más bajo\n            El {numero} no es el número secreto\n==================================================')
        
        intentos -= 1
        numeros_incorrectos.append(numero)
        input('\n-Pulsa ENTER para volver a adivinar-\n')
        return adivinar()
    else:
        print('\n==================================================\n            Ya intentaste ese valor.\n==================================================\n')
        input('-Pulsa enter para volver a adivinar-\n')
        return adivinar()


def sin_intentos():
    """Maneja cuando el jugador se queda sin intentos."""
    global intentos
    limpiar()
    mostrar_titulo("Te quedaste sin intentos")
    print(f'\nEl número secreto era: {numero_secreto}')
    print('\n¿Qué vas a hacer ahora?\n[1]. Volver a intentarlo.\n[2]. Salir.')
    opcion = input('Respuesta: ')
    
    if opcion == '1':
        limpiar()
        reinicio()
        return adivinar()
    elif opcion == '2':
        limpiar()
        reinicio()
        mostrar_menu_principal()
    else:
        print('==================================================\n     No es una opción válida\n==================================================')
        input('\n-Pulsa ENTER para continuar-\n')
        sin_intentos()


def adivinar():
    """Función principal del juego para adivinar el número."""
    limpiar()
    global intentos, numero_secreto
    
    mostrar_titulo(f"Erróneos: {numeros_incorrectos}\nIntentos: {intentos}")
    
    if intentos == 0:
        sin_intentos()
        return
    
    entrada = input('\nDigite un número: ')
    
    # Validar que sea un número
    if not entrada.isdigit():
        no_es_un_numero()
        return
    
    numero = int(entrada)
    
    if numero == numero_secreto:
        limpiar()
        print(f'==================================================\n    ¡Felicidades! Acertaste el número.\n    Número secreto: {numero_secreto}\n==================================================')
        print('\n¿Qué vas a hacer ahora?\n[1]. Volver a intentarlo.\n[2]. Salir.')
        opcion = input('Respuesta: ')
        
        if opcion == '1':
            limpiar()
            reinicio()
            adivinar()
        elif opcion == '2':
            limpiar()
            reinicio()
            mostrar_menu_principal()
        else:
            limpiar()
            print('==================================================\n     No es una opción válida\n==================================================')
            input('\n-Pulsa ENTER para continuar-\n')
            reinicio()
            adivinar()
    else:
        numero_es_incorrecto(numero)


def jugar_adivinar_numero():
    """Inicia y procesa la lógica del juego 'Adivina el Número'."""
    limpiar()
    mostrar_titulo("ADIVINAR EL NÚMERO")
    print('¡Hola! 👋 Bienvenido al mini-juego "Adivinar el número".')
    print('El juego consiste en intentar adivinar un número en 6 intentos.')
    print('El número puede estar entre el 1 al 100.')
    print('\n¿Listo para comenzar?\n[1]. Comenzar\n[2]. Salir')
    
    opcion = input('Respuesta: ')
    
    if opcion == '1':
        limpiar()
        reinicio()
        adivinar()
    elif opcion == '2':
        limpiar()
        mostrar_menu_principal()
    else:
        limpiar()
        print('==================================================\n          No es una opción válida\n==================================================')
        input('\n-Pulsa ENTER para volver-\n')
        jugar_adivinar_numero()

# === JUEGO AHORCADO === #

def mostrar_estado_ahorcado(intentos_fallidos: int, letras_usadas: list, progreso: list, palabra_secreta: str) -> None:
    """Muestra el estado actual del juego de ahorcado.
    Argumentos:
        intentos_fallidos (int): Cantidad de fallos acumulados.
        letras_usadas (list): Lista de letras ya usadas por el jugador.
        progreso (list): Lista de caracteres con letras adivinadas y guiones.
        palabra_secreta (str): Cadena de caracteres que representa la palabra secreta.
    """
    limpiar()
    mostrar_titulo("Ahorcado")
    print(f"  La palabra tiene {len(palabra_secreta)} letras.\n")
    print(ETAPAS_AHORCADO[intentos_fallidos])
    print(f"\n  Palabra: {' '.join(progreso)}")
    print(f"  Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else '-'}")
    print(f"  Intentos fallidos: {intentos_fallidos}/{MAX_INTENTOS_AHORCADO}\n")


def obtener_letra_usuario(letras_usadas: list) -> str:
    """Solicita y valida una letra al usuario (A-Z, ignora mayúsculas).
    Argumentos:
        letras_usadas (list): Letras ya ingresadas para evitar repeticiones.
    Retorna:
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


def jugar_ahorcado() -> None:
    """Inicia y procesa la lógica del juego 'Ahorcado'.
    El programa elige una palabra aleatoria. El jugador adivina letra por letra.
    Dispone de MAX_INTENTOS_AHORCADO fallos antes de perder.
    Al terminar se revela la palabra si no fue adivinada.
    """
    palabra_secreta = random.choice(PALABRAS_AHORCADO)
    progreso = ["_"] * len(palabra_secreta)
    letras_usadas = []
    intentos_fallidos = 0
    gano = False

    while intentos_fallidos < MAX_INTENTOS_AHORCADO:
        mostrar_estado_ahorcado(intentos_fallidos, letras_usadas, progreso, palabra_secreta)

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

# === JUEGO CODIGO === # 

def generar_codigo_secreto():
    """
    Genera un código secreto de LONGITUD_CODIGO dígitos aleatorios (0-9).
    Returns:
        list: Lista de enteros que representan el código secreto.
    """
    return [random.randint(0, 9) for _ in range(LONGITUD_CODIGO)]
 
 
def obtener_codigo_usuario():
    """
    Pide y valida un código de LONGITUD_CODIGO dígitos al usuario.
    Repite la solicitud hasta recibir una entrada válida.
    Returns:
        list: Lista de enteros ingresados por el usuario.
    """
    while True:
        entrada = input(f"  Ingresa un código de {LONGITUD_CODIGO} dígitos (ej: 1234): ").strip()
        if len(entrada) == LONGITUD_CODIGO and entrada.isdigit():
            return [int(d) for d in entrada]
        print(f"  Código no válido. Debe tener exactamente {LONGITUD_CODIGO} dígitos numéricos.")
 
 
def comparar_codigo(secreto, intento):
    """
    Compara el intento con el código secreto posición por posición.
    Los dígitos correctos en su posición se incluyen en el resultado,
    los incorrectos se representan con un guión bajo.
    Args:
        secreto (list): Código secreto generado por el programa.
        intento (list): Código ingresado por el usuario.
    Returns:
        list: Lista con los dígitos correctos en su posición o '_' si es incorrecto.
    """
    resultado = []
    for i in range(LONGITUD_CODIGO):
        if intento[i] == secreto[i]:
            resultado.append(str(intento[i]))
        else:
            resultado.append("_")
    return resultado
 
 
def jugar_codigo():
    """
    El programa genera un código de 4 dígitos, el jugador adivina dígito
    a dígito, los dígitos correctos en su posición se revelan después de cada
    intento, tiene MAX_INTENTOS_CODIGO intentos antes de perder.
    Al terminar se revela el código si no fue adivinado.
    """
    print("\n" + "=" * 50)
    print("   CÓDIGO")
    print("=" * 50 + "\n")
 
    codigo_secreto = generar_codigo_secreto()
    progreso = ["_"] * LONGITUD_CODIGO
    intentos_usados = 0
    gano = False
 
    print(f"  He generado un código de {LONGITUD_CODIGO} dígitos.")
    print(f"  Tienes {MAX_INTENTOS_CODIGO} intentos.\n")
 
    while intentos_usados < MAX_INTENTOS_CODIGO:
        print(f"  Código actual:      {' '.join(progreso)}")
        print(f"  Intentos restantes: {MAX_INTENTOS_CODIGO - intentos_usados}\n")
 
        intento = obtener_codigo_usuario()
        intentos_usados += 1
        resultado = comparar_codigo(codigo_secreto, intento)
 
        for i in range(LONGITUD_CODIGO):
            if resultado[i] != "_":
                progreso[i] = resultado[i]
 
        aciertos = sum(1 for r in resultado if r != "_")
        print(f"\n  Resultado: {' '.join(resultado)}  ({aciertos} acierto(s) en posición correcta)\n")
 
        if "_" not in progreso:
            gano = True
            break
 
    if gano:
        print(f"  ¡Ganaste! El código era: {''.join(str(d) for d in codigo_secreto)}")
    else:
        print(f"  ¡Perdiste! El código era: {''.join(str(d) for d in codigo_secreto)}")

# === JUEGO REVOLTIJO DE PALABRAS === #

def jugar_revoltijo() -> None:
    """Inicia y procesa la lógica del juego 'Revoltijo de Palabras'."""
    palabra = random.choice(PALABRAS_REVOLTIJO)
    palabra_desordenada = desordenar_palabra(palabra)
    intentos = 3
    while intentos > 0:
        actualizar_revoltijo(palabra_desordenada, intentos)
        respuesta = input("¡Adivina la palabra!: ")
        if respuesta == palabra:
            print("\n🎊🎉🎈 ¡Felicitaciones, adivinaste la palabra! 🎈🎉🎊")
            return
        if respuesta == "":
            print("\n🔘 Respuesta vacía, no se consumieron intentos... 🔘")
            input()
        else:
            intentos -= 1
        if intentos > 0 and respuesta != "":
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
    
    Retorna:
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
    limpiar()
    mostrar_titulo("Revoltijo de Palabras")
    print(f"{palabra_desordenada}\n")
    print(f"Intentos restantes: {intentos}")


# ============================================================================================= #

ejecutar_menu()
