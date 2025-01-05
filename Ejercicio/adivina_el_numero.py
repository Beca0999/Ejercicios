import random

def adivina_el_numero():
    numero_secreto=random.radint(1,100)
    intentos=0
    print("\n¡Adivina el número emtre 1 y 100!")

    while True:
        intento=int(input("Introduce tu número:"))
        intentos+=1
        if intento<numero_secreto:
            print("¡Muy bajo!")
        elif intento>numero_secreto:
            print("¡Muy alto!")
        else:
            print(f"¡Correcto! Lo adivinaste en {intentos}intentos.\n")
            ar=input("Pulsa Enter para continuar...\n")
            new_var=input("Pulsa Enter para continuar...\n")
            break
