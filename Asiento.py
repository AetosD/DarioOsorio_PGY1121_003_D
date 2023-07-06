class Asiento:
    rut = ''

    def __init__(self):
        self.rut = '11111111'

    def setrut(self, rut):
        if len(rut) == 8 and rut.isdigit():
            self.rut = rut
            return True
        else:
            print("Formato de rut no valido")
            return False
