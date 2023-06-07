from manejaHelados import ManejaHelados
from manejaSabores import ManejaSabores
from menu import Menu

if __name__ == '__main__':
    MH = ManejaHelados()
    MS = ManejaSabores()
    MS.cargar_sabores()
    MS.mostrarCarga()
    print("\n")
    menu = Menu()
    menu.opciones(MS, MH)