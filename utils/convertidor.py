

class Convertidor:

    def __init__(self):
        pass

    def Binarizador(self, number):
        Binarios = []
        NumeroInicial = number
        Numero = NumeroInicial

        for i in range(0 ,Numero) :
            Cociente = Numero // 2
            Residuo = Numero % 2
            Binarios.append(Residuo)
            Numero = Cociente
            i = i + 1
            if Cociente == 0 :
                break
        
        Binarios.reverse()


        return (Binarios)
    
    def ConvASCI(self, string):
        newArr = []
        for i in range(len(string)):
            charAscci = ord(string[i])
            newArr.append(charAscci)
        return newArr
    
    def desAscci(self, array):
        newArr = []
        for i in range(len(array)):
            charAscci = chr(array[i])
            newArr.append(charAscci)
        return newArr
    

    def conArrStr(self, array):
        newString = ''
        for i in range(len(array)):
            character = array[i]
            newString = newString + character
        return newString
    
    def es_primo(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def Decimalizador(self, NumeroInicial):
        Numeros = 0
        i = 0
        x = 0
        Digitos = len(NumeroInicial) - 1
        NumeroInicial = NumeroInicial[::-1]

        while i <= Digitos:
            #print("i: ", i)
            #print("x: ", x)
            NumeroNuevo = NumeroInicial[x]
            #print("Numero Nuevo: ", NumeroNuevo)
            variable = int(NumeroNuevo) * (2**i)
            #print("variable: ", variable)
            Numeros += variable
            #print("Numeros: ", Numeros)
            i += 1
            x += 1
        return Numeros
