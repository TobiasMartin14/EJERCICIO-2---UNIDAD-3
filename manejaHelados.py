from claseHelado import Helado
#from manejaSabores import ManejaSabores

class ManejaHelados:
    __listaH: list
    
    def __init__(self):
        self.__listaH = []
        
    def mostrarTipo(self):
        print('1 - 100gr - $400')
        print('2 - 150gr - $500')
        print('3 - 250gr - $800')
        print('4 - 500gr - $1500')
        print('5 - 1000gr - $2500')
        
    def seleccionarPeso(self):
        self.mostrarTipo()
        cod = int(input('Ingrese el codigo del tipo de Helado'))
        if cod == 1:
            peso = 100
        elif cod == 2:
            peso = 150
        elif cod == 3:
            peso = 250
        elif cod == 4:
            peso = 500
        elif cod == 5:
            peso = 1000
        return peso
    
    def seleccionarPrecio(self, peso):
        if peso == 100:
            precio = 400
        elif peso == 150:
            precio = 500
        elif peso == 250:
            precio = 800
        elif peso == 500:
            precio = 1500
        elif peso == 1000:
            precio = 2500
        return precio
    
    def registrarVenta(self, MS):
        sabores = []
        print('Ingrese el peso del Helado')
        peso = self.seleccionarPeso()
        cantidad = int(input('Ingrese la cantidad de sabores que quiere pedir (Entre 1 y 4)'))
        print('Ingrese el ID de el/los sabor/es a pedir')
        MS.mostrar_sabores()
        for i in range(cantidad):
            pos = int(input("Ingrese el ID del {}° sabor: ".format(i+1)))
            sabor = MS.get_sabor(pos-1)
            sabores.append(sabor)
        precio = self.seleccionarPrecio(peso)
        helado = Helado(peso, precio, sabores)
        self.__listaH.append(helado)

    def contarPedidos(self, cantS):
        aux = [0 for _ in range(cantS)]
        for vendido in self.__listaH:
            for sabor in vendido.getSaboresV():
                aux[sabor.get_id()-1] = aux[sabor.get_id()-1] + 1
        return aux    
                
    def masPedidos(self, cantS):
        top5 = []
        pedidos = self.contarPedidos(cantS)
        for i in range(5):
            max = 0
            pos = 0
            for j in range(len(pedidos)):
                if pedidos[j] > max:
                    max = pedidos[j]
                    pos = j
            pedidos[pos] = 0
            top5.append(pos)
        return top5
            
    def mostrarMasPedidos(self, MS):
        top5 = self.masPedidos(len(MS.getSabores()))
        sabores = MS.getSabores()
        print("Estos son los 5 sabores mas pedidos: ")
        for ID in top5:
            print(sabores[ID].getNombre())
            
    def gramosVendidos(self, MS):
        MS.mostrar_sabores()
        id = int(input('Ingrese el ID del helado a mostrar los gramos vendidos'))
        total_gramos = 0
        for venta in self.__listaH:
            sabores = venta.getSaboresV()
            for sabor in sabores:
                if sabor.get_id() == id:
                    total_gramos = total_gramos + (venta.get_gramos() / len(sabores))
        print('El total de gramos vendidos del sabor con ID {} es de {}g'.format(id, total_gramos))
        
    def contarVendidosTamaño(self, tamano, cantS):
        aux = [0 for _ in range(cantS)]
        for helado in self.__listaH:
            if helado.get_gramos() == tamano:
                for sabor in helado.getSaboresV():
                    aux[sabor.get_id()-1] = aux[sabor.get_id()-1] + 1
        return aux
                    
    def vendidosTamaño(self,  MS):
        #tamano = float(input('Ingrese el tamaño del helado'))
        tamano = self.seleccionarPeso()
        sabores = MS.getSabores()
        pedidos = self.contarVendidosTamaño(tamano, len(sabores))
        print('Estos son los sabores vendidos en el tamaño de {}g'.format(tamano))
        for i in range(len(sabores)):
            if pedidos[i] > 0:
                print('-' + sabores[i].getNombre())
            
    def calcularRecaudado(self):
        total = [0.0 for _ in range(5)]
        for venta in self.__listaH:
            tipo = venta.get_gramos()
            if tipo == 100:
                total[0] += venta.get_precio()
            if tipo == 150:
                total[1] += venta.get_precio()
            if tipo == 250:
                total[2] += venta.get_precio()
            if tipo == 500:
                total[3] += venta.get_precio()
            if tipo == 1000:
                total[4] += venta.get_precio()
        return total
    
    def mostrarRecaudado(self):
        print('Los tipos de helado son los siguientes:')
        self.mostrarTipo()
        vendido = self.calcularRecaudado()
        for i in range(5):
            print('Recaudado por los helados tipo {} : ${}'.format(i+1, vendido[i]))
        print('')