class TV:
    #Atributos
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        TV._numTV += 1


    #Getters y Setters
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca
    
    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):
        if (canal >= 0) and (canal <= 120) and (self._estado):
            self._canal = canal
    
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio
    
    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if (volumen >= 0) and (volumen<=7) and (self._estado):
            self._volumen = volumen

    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    #Methods
    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if (self._canal >= 1) and (self._canal < 120):
            self.setCanal(self._canal + 1)
    
    def canalDown(self):
        if (self._canal > 1) and (self._canal <= 120):
            self.setCanal(self._canal - 1)
    
    def volumenUp(self):
        if (self._volumen >= 0) and (self._volumen < 7):
            self.setVolumen(self._volumen + 1)
    
    def volumenDown(self):
        if (self._volumen > 1) and (self._volumen <= 7):
            self.setVolumen(self._volumen - 1)

