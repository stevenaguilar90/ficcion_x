import os 
from sistema.biblioteca import Biblioteca
from archivos.json_manager import JSONManager
from modelos.libro import Libro

# Manejo seguro de colorama por si no está instalado
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = GREEN = YELLOW = CYAN = ""
    class Style:
        RESET_ALL = ""


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input(f"\n{Fore.YELLOW}Presiona ENTER para continuar...{Style.RESET_ALL}")


def mostrar_titulo():
    limpiar_pantalla()
    print(Fore.CYAN + "=" * 50)
    print(" 📚          SISTEMA DE BIBLIOTECA")
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


def main():
    biblioteca = Biblioteca()
    json_manager = JSONManager("datos/libros.json")

    # Cargar datos iniciales
    try:
        libros = json_manager.cargar()
        for datos in libros:
            libro = Libro(
                datos["titulo"],
                datos["autor"],
                datos["anio"],
                datos["isbn"]
            )
            biblioteca.agregar_libro(libro)
    except Exception:
        pass

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Agregar libro ---")
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, anio, isbn)
            biblioteca.agregar_libro(libro)

            print(Fore.GREEN + "\nLibro agregado correctamente.")
            pausar()

        elif opcion == "2":
            print("\n--- Lista de libros ---")
            biblioteca.mostrar_libros()
            pausar()

        elif opcion == "3":
            titulo = input("\nIngrese el título a buscar: ")
            biblioteca.buscar_libro(titulo)
            pausar()

        elif opcion == "4":
            titulo = input("\nIngrese el título a eliminar: ")
            biblioteca.eliminar_libro(titulo)
            pausar()

        elif opcion == "5":
            json_manager.guardar(biblioteca.libros)
            print(Fore.GREEN + "\nDatos guardados correctamente.")
            pausar()

        elif opcion == "6":
            biblioteca.libros = []
            libros = json_manager.cargar()

            for datos in libros:
                libro = Libro(
                    datos["titulo"],
                    datos["autor"],
                    datos["anio"],
                    datos["isbn"]
                )
                biblioteca.agregar_libro(libro)

            print(Fore.GREEN + "\nDatos cargados correctamente.")
            pausar()

        elif opcion == "7":
            json_manager.guardar(biblioteca.libros)
            print(Fore.CYAN + "\n¡Hasta luego!")
            break

        else:
            print(Fore.RED + "\nOpción inválida.")
            pausar()


if __name__ == "__main__":
    main()