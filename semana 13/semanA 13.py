class circulo():
    def __init__(self, radio):
        self.radio= radio

    def ob_peri(self):
        return float (self.radio) * 2 * 3.14
    def obt_area(self): 
        return float(self.radio)**2 * 3.14
    def obt_vol(self):
        return float(self.radio)**3 * 4 *3.14 / 3
    

ncir=int(input("cuantos circulos desea: "))
listacirculo=[]

for i in range(ncir):
   circulo1=circulo(float(input("introduzca el radio del circulo numero "+str(i+1)+": ")))

for y in range(ncir):
  resultado=circulo1.ob_peri()
  print("del circulo numero "+str(y+1)+":")
  print(resultado)
  resultado1= circulo1.obt_area()
  print("area del circulo numero "+str(y+1)+":")
  print(resultado1)
  resultado2= circulo1.obt_vol()
  print("volumen del circulo numero "+str(y+1)+":")
  print(resultado2)