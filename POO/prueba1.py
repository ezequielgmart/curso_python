#crear una clase
class Coche():
    largo_chasis=250 #propiedad
    ancho_chasis=120
    ruedas=4
    en_marcha=False

    def arrancar(self):#todos los metodos deben de tener el SELF como primer parametro obligatorio
        self.en_marcha=True
    def getRuedas(self):
        return self.ruedas
    def estado(self):
        if(self.en_marcha):
            return "El carro está en marcha"
        else:
            return "El carro está detenido"

mazda=Coche() #instancia de clase Coche
mazda.arrancar()
print("El coche tiene: ", mazda.getRuedas())
print("El coche está: ", mazda.estado())
