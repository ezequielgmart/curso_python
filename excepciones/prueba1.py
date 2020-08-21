def main():
    while True:
        try:
            a = int(input("ingresa un numero: "))
            b =  int(input("ingresa otro numero: "))
            break

        except ValueError:
            print("Imposible con strings")
            return "Operacion erronea"
    dividir(a,b)    

def dividir(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Imposible dividir entre cero")
        return "Operacion erroea"



if __name__ == '__main__':
    main()
