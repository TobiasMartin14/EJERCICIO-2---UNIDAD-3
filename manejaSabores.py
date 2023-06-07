import csv
from claseSabor import Sabor

class ManejaSabores:
    __listaS: list
    
    def __init__(self):
        self.__listaS = []
        
    def cargar_sabores(self):
        archivo = open('sabores.csv', encoding = 'utf-8')
        reader = csv.reader(archivo, delimiter=';')

        for fila in reader:
            sabor = Sabor(int(fila[0]), fila[1], fila[2])
            self.__listaS.append(sabor)
        print('Los sabores han sido cargados con éxito')
        archivo.close()
    
    def mostrarCarga(self):
        for sab in self.__listaS:
            print("{}" .format(sab))
        
    def getSabores(self):
        return self.__listaS
    
    def get_sabor(self, pos):
        return self.__listaS[pos]
    
    def mostrar_sabores(self):
        for i in range(len(self.__listaS)):
            print('{}: '.format(i+1) + self.__listaS[i].getNombre())
