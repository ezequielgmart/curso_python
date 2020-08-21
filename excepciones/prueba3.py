def main():
    intentos = 1
    mostrar=True
    while mostrar==True:
        print("Numeros de intentos: " + str(intentos))
        try:
            edad = int(input("Introduce tu edad "))
        except ValueError:
            print("Error: No puedes colocar caracteres Fin del programa")
            edad = int(input("Introduce tu edad "))
        print(evaluaEdad(edad))
        print("¿Quieres continuar...?")
        try:
            respuesta = int(input("1. Si / 2.No: "))
        except ValueError:
            print("Error: No puedes colocar caracteres")
            print("Intentelo de nuevamente")
            respuesta =int(input("1. Si / 2.No: "))

        if respuesta == 1:
            intentos =intentos+1
            continue
        elif respuesta == 2:
            print("Fin del programa")
            mostrar=False
def evaluaEdad(edad):
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Aun eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<99:
        return "cuidate"
    elif edad>=100:
        return "ese compa ya esta muerto, no más no le han avisado"

if __name__ == '__main__':
    main()
