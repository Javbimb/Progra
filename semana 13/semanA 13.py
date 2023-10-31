class circulo():
    def __init__(self, radio):
        self.radio= radio

    def ob_peri(self):
        return float (self.radio) * 2 * 3.14
    def obt_area(self): 
        return float(self.radio)**2 * 3.14
    def obt_vol(self):
        return float(self.radio)**3 * 4 *3.14 / 3
    
circulo1=circulo(7)
print(circulo1.ob_peri())
print(circulo1.obt_area())
print(circulo1.obt_vol())
