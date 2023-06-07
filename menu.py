
class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, MS, MH):
        indice = True
        while indice:
            print ("Opcion 1: Registrar un helado vendido.")
            print ("Opcion 2: Mostrar el nombre de los 5 sabores de helado más pedidos.")
            print ("Opcion 3: Ingresar un número de sabor y estimar el total de gramos vendidos.")
            print ("Opcion 4: Ingresar un tipo de helado y mostrar los sabores vendidos en ese tamaño.")
            print ("Opcion 5: Determinar el importe total recaudado por la Heladería, por cada tipo de helado.")
            print ("Opcion 6: Salir ")
            print("\n")
            self.__opcion = int(input("Seleccione una opcion: "))
            if self.__opcion == 1:
                MH.registrarVenta(MS)
            elif self.__opcion == 2:
                MH.mostrarMasPedidos(MS)
            elif self.__opcion == 3:
                MH.gramosVendidos(MS)
            elif self.__opcion == 4:
                MH.vendidosTamaño(MS)
            elif self.__opcion == 5:
                MH.mostrarRecaudado()
            elif self.__opcion == 6:
                print("Finalizando la ejecución del programa...")
                indice = False
            else:
                print("La opción ingresada no es válida.")
            
            print("\n")

