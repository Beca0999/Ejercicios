from adivina_el_numero import adivina_el_numero
from generador_de_historia import generador_de_historia
from lanzar_dados import lanzar_dados
from conversor_de_emojis import conversor_de_emojis
from generador_de_passwords import generador_de_passwords

def mostrar_menu():
    while True:
        print("\nMenú de ejercicios divertidos:")
        print("1. Juego: Adivina el número")
        print("2. Generador de palabras locas (Mad Libs)")
        print("3. Simulador de dados")
        print("4. Calculadora de emojis")
        print("5. Creador de contraseñas aleatorias")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            adivina_el_numero()
        elif opcion == "2":
            generador_de_historia()
        elif opcion == "3":
            lanzar_dados()
        elif opcion == "4":
            conversor_de_emojis()
        elif opcion == "5":
            generador_de_passwords()
        elif opcion == "6":
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()
    