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