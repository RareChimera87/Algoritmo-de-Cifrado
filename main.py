from core.crea import KeyPair

class Main:
    def __init__(self):
        self.KeyPair = KeyPair()
    def iniciar(self):
        self.KeyPair.generate_keys()
        self.KeyPair.Cifrar("Hola como estas", "clave pública de prueba")


Main().iniciar()