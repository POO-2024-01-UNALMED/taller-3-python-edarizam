from tv import TV

class Control:
    #Atributo
    def __init__(self, tv):
        self._tv = tv
    
    #Getter y Setter
    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv

    #Methods
    def turnOn(self):
        TV.turnOn()
    
    def turnOff(self):
        TV.turnOff()

    def canalUp(self):
        TV.canalUp()
    
    def canalDown(self):
        TV.canalDown()
        
    def volumenUp(self):
        TV.volumenUp()
    
    def volumenDown(self):
        TV.volumenDown()

    def setCanal(self,canal):
        TV.setCanal(canal)
    
    def setVolumen(self,volumen):
        TV.setVolumen(volumen)

    def enlazar(self, tv):
        TV.setControl(self)
        self._tv = tv 

