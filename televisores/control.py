import tv

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
        tv.turnOn()
    
    def turnOff(self):
        tv.turnOff
    
    def canalUp(self):
        tv.canalUp()
    
    def canalDown(self):
        tv.canalDown
        
    def volumenUp(self):
        tv.volumenUp()
    
    def volumenDown(self):
        tv.volumenDown()

    def setCanal(self,canal):
        tv.setCanal(canal)
    
    def setVolumen(self,volumen):
        tv.setVolumen(volumen)

    def enlazar(self, tv):
        tv.setControl(self)
        self._tv = tv 
   
