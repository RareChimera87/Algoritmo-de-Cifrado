

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