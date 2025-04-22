import time
from utils.convertidor import  Convertidor

class KeyPair:
    def __init__(self):
        self.convertidor = Convertidor()
        self.clave_publica = None
        self.clave_privada = None
        self.NamePublica = "PruebaClavePublica"
        self.NamePrivada = "PruebaClavePrivada"
    
    def generate_keys(self):
        self.clave_publica = "clave pública de prueba"
        self.clave_privada = "clave privada de prueba"
        self.save_keys()

    def save_keys(self):
        self.almacenar(self.NamePublica, self.clave_publica)
        self.almacenar(self.NamePrivada, self.clave_privada)
    
    def almacenar(self, NameforFile, valor):
        NameforFile = NameforFile.strip()
        nombre = NameforFile + ".txt"

        f = open(nombre, "a")
        f.write("\n")
        f.write("\n")
        f.write("*****************")
        f.write("La fecha de ejecucion es: ")
        fecha = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(fecha)
        f.write("\n")
        f.write("Clave: ")
        f.write(valor)
        f.close()
    
    def Cifrar(self, mensaje, Publickey):
        new = self.convertidor.ConvASCI(Publickey)
        bini = []
        unos = 1
        for i in range(len(new)):
            binario = self.convertidor.Binarizador(new[i])
            bini.append(binario)
        print(bini)
        for i in range(len(bini)):
            for j in range(len(bini[i])):
                numero = bini[i][j]
                if numero == 1:
                    unos += 1
        print(unos)
        other = self.convertidor.ConvASCI(mensaje)
        print(other)
        for i in range(len(other)):
            temp = other[i] + unos
            print("Temporal: ", temp)
            if (temp) > 127:
                nuevo = temp - 127
                print("Nuevo: ", nuevo)
                other[i] = nuevo
            else:
                other[i] += unos
        print(other)
        mensajeCifrado = self.convertidor.desAscci(other)
        print(mensajeCifrado)
        stringCifrado = self.convertidor.conArrStr(mensajeCifrado)
        print(stringCifrado)
        self.almacenar("Mensaje Cifrado", stringCifrado)







