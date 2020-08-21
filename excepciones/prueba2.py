#esta funcion dividir no tendrá ningun argumento
def main():
    try:
        a=(float(input("introduce el primer numero: ")))
        b=(float(input("introduce el segundo numero: ")))

        print("La division es: " + str(a/b))

    except ValueError:
        print("El valor introducido es erroneo... ")
    except ZeroDivisionError:
        print("No es posible dividir entre cero... ")
    finally
        print("Final...")
        #lo que se ejecuta dentro del finally se ejecutará de todas maneras. 
if __name__ == '__main__':
    main()
