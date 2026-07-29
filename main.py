from sistema.biblioteca import Biblioteca
from archivos.json_manager import JSONManager
from modelos.libro import Libro
import os 
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = GREEN = YELLOW = CYAN = ""
    class Style:
        RESET_ALL = ""
    def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
    def pausar():
    input("\nPresione ENTER para continuar...")
    def titulo():

    limpiar()

    print("=" * 50)
    print("📚      FICCIÓN X - GESTOR DE LIBROS")
    print("=" * 50)
    def menu():

    titulo()

    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Editar libro")
    print("5. Eliminar libro")
    print("6. Estadísticas")
    print("7. Salir")

    return input("\nSeleccione una opción: ")
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input(f"\n{Fore.YELLOW}Presiona ENTER para continuar...{Style.RESET_ALL}")


def mostrar_titulo():
    limpiar_pantalla()
    print(Fore.CYAN + "=" * 50)
    print("          SISTEMA DE BIBLIOTECA")
    print("=" * 50 + Style.RESET_ALL)


def mostrar_menu():
    mostrar_titulo()
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Guardar datos")
    print("6. Cargar datos")
    print("7. Salir")
    print()