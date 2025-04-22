import time
from utils.convertidor import  Convertidor

class KeyPair:
    def __init__(self):
        self.convertidor = Convertidor()
        self.clave_publica = None
        self.clave_privada = None
        self.NamePublica = "PruebaClavePublica"
        self.NamePrivada = "PruebaClavePrivada"
        self.extension = ".txt"
        self.carpeta = "docs/"
    
    def generate_keys(self):
        self.clave_publica = "clave pública de prueba"
        self.clave_privada = "clave privada de prueba"
        self.save_keys()

    def save_keys(self):
        self.almacenar(self.NamePublica, self.clave_publica)
        self.almacenar(self.NamePrivada, self.clave_privada)
    
    def almacenar(self, NameforFile, valor, mensaje=None):
        NameforFile = NameforFile.strip()
        nombre = NameforFile + self.extension
        ruta = self.carpeta + nombre

        f = open(ruta, "a")
        f.write("\n")
        f.write("\n")
        f.write("*****************")
        f.write("La fecha de ejecucion es: ")
        fecha = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(fecha)
        f.write("\n")
        if mensaje != None:
            f.write("\n")
            f.write("Valor Original: ")
            f.write(mensaje)
            f.write("\n")
        
        f.write("Valor: ")
        if type(valor) == list:
            f.write("Its a List")
            f.write("\n")
            for item in valor:
                if type(valor) == list:
                    for itemcito in item:                    
                        f.write(str(itemcito))
                else:
                   f.write(str(item)) 
        else:
            f.write("Its a string")
            f.write("\n")
            f.write(valor)
        f.close()
    
    def Cifrar(self, mensaje, Publickey):
        mensaje_cifrado = (mensaje.encode('utf-8'))
        bytesMessage = list(mensaje_cifrado)
        Publickey_Cifrado = Publickey.encode('utf-8')
        bytesKey = list(Publickey_Cifrado)
        new = []
        nose = 0
        for i in range(len(bytesKey)):
            if (self.convertidor.es_primo(bytesKey[i])):
                new.append(bytesKey[i])
        for i in range(len(new)): 
            nose += new[i]
        key = int(nose / len(new))
        binarios = []
        for byte in bytesMessage:
            eleva = byte ** key
            binarios.append(self.convertidor.Binarizador(eleva))
        lista_decimal = []
        for i in range(len(binarios)):
            numero = self.convertidor.Decimalizador(binarios[i])
            numero = int(numero)
            lista_decimal.append(numero)
        #print(lista_decimal)
        nueva_lista = []
        for i in range(len(lista_decimal)):
            num = lista_decimal[i]
            num_bytes = (num.bit_length() + 7) // 8 # Para calcular cuantos bytes necesita
            bytes_resultado = num.to_bytes(num_bytes, byteorder='big')
            nueva_lista.append(list(bytes_resultado))
        #print(nueva_lista)
        final = []
        for i in range(len(nueva_lista)):
            for j in range(len(nueva_lista[i])):
                number = nueva_lista[i][j]
                if number == 0:
                    number = "."
                    final.append(number)
                    continue
                number = ((number - 32) % 95) + 32  # Siempre cae entre 32 y 126
                final.append(chr(number))
        newFinal = self.convertidor.conArrStr(final)
        self.almacenar("Mensaje Cifrado", newFinal, mensaje)
        







