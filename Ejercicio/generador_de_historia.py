def generador_de_historia():
    print("\n Vamos a crear una historia divertida.")
    nombre=input("Introduce un nombre:")
    lugar=input("Introduce un lugar:")
    verbo=input("Introduce un verbo:")

    objeto=input("Introduce un objeto:")
    historia = f"{nombre} fue a {lugar} para {verbo} con un/a {objeto}. ¡Qué aventura tan extraña!"
    print("\nTu historia:")
    print(historia + "\n")
    new_var = input("pulsa Enter para continuar ... \n")