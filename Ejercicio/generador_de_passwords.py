import random
import string

def generador_de_passwords():
    caracteres=string.ascii_letters+string.digits+"!@#$%^&*()"
    longitud=int (input("\n¿Qué longitud debe tener tu contraseña?"))
    
    contraseña="".join(random.choice(caracteres) for _ in range(longitud))
    print(f"Tu nueva contraseña es: {contraseña}\n")
    new_var=input("Pulsa Enter para continuar...\n")
    