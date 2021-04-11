class Fraccion:

    def __init__(self,arriba,abajo):

        self.num = arriba
        self.den = abajo

    def mostrar(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,numero):
        numero2 = numero.den


miF = Fraccion(2,3)
print(miF)
print("Comí", miF , "de la pizza")
print(miF)