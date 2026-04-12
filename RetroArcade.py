import os

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



ejecutar_menu()
