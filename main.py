import os

from sistema.biblioteca import Biblioteca
from archivos.json_manager import JSONManager
from modelos.libro import Libro


# Manejo de colores
try:
    from colorama import init, Fore, Style

    init(autoreset=True)

except ImportError:

    class Fore:
        RED = ""
        GREEN = ""
        YELLOW = ""
        CYAN = ""

    class Style:
        RESET_ALL = ""


def limpiar_pantalla():
    os.system(
        "cls" if os.name == "nt" else "clear"
    )


def pausar():
    input(
        f"\n{Fore.YELLOW}"
        "Presiona ENTER para continuar..."
        f"{Style.RESET_ALL}"
    )


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
def pedir_numero(mensaje, minimo=1, maximo=None):
    while True:
        valor = input(mensaje).strip()

        if not valor.isdigit():
            print(Fore.RED + "❌ Debe ingresar solamente números.")
            continue

        numero = int(valor)

        if numero < minimo:
            print(Fore.RED + f"❌ El valor debe ser como mínimo {minimo}.")
            continue

        if maximo is not None and numero > maximo:
            print(Fore.RED + f"❌ El valor no puede ser mayor que {maximo}.")
            continue

        return numero


def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()

        if not valor:
            print(Fore.RED + "❌ Este campo no puede quedar vacío.")
            continue

        return valor

def main():

    biblioteca = Biblioteca()
    json_manager = JSONManager()

    # Cargar libros existentes al iniciar
    biblioteca.libros = json_manager.cargar()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        # =================================
        # AGREGAR LIBRO
        # =================================

        if opcion == "1":

            print("\n--- AGREGAR LIBRO ---")

            id_libro = input(
                "ID del libro: "
            ).strip()

            titulo = input(
                "Título: "
            ).strip()

            autor = input(
                "Autor: "
            ).strip()

            anio = input(
                "Año: "
            ).strip()

            genero = input(
                "Género: "
            ).strip()

            paginas = input(
                "Cantidad de páginas: "
            ).strip()

            # Verificar ID repetido
            if biblioteca.buscar_por_id(id_libro):
                print(
                    Fore.RED
                    + "\nEse ID ya existe."
                )
                pausar()
                continue

            libro = Libro(
                id_libro,
                titulo,
                autor,
                anio,
                genero,
                paginas
            )

            biblioteca.agregar_libro(libro)

            print(
                Fore.GREEN
                + "\nLibro agregado correctamente."
            )

            pausar()

        # =================================
        # MOSTRAR LIBROS
        # =================================

        elif opcion == "2":

            print("\n--- LISTA DE LIBROS ---")

            biblioteca.mostrar_libros()

            pausar()

        # =================================
        # BUSCAR LIBRO
        # =================================

        elif opcion == "3":

            print("\n--- BUSCAR LIBRO ---")

            titulo = input(
                "Ingrese el título a buscar: "
            ).strip()

            biblioteca.buscar_libro(titulo)

            pausar()

        # =================================
        # ELIMINAR LIBRO
        # =================================

        elif opcion == "4":

            print("\n--- ELIMINAR LIBRO ---")

            titulo = input(
                "Ingrese el título a eliminar: "
            ).strip()

            eliminado = biblioteca.eliminar_libro(
                titulo
            )

            if eliminado:
                # Guardar automáticamente
                json_manager.guardar(
                    biblioteca.libros
                )

            pausar()

        # =================================
        # GUARDAR DATOS
        # =================================

        elif opcion == "5":

            try:

                json_manager.guardar(
                    biblioteca.libros
                )

                print(
                    Fore.GREEN
                    + "\nDatos guardados correctamente."
                )

            except Exception as error:

                print(
                    Fore.RED
                    + f"\nError al guardar: {error}"
                )

            pausar()

        # =================================
        # CARGAR DATOS
        # =================================

        elif opcion == "6":

            try:

                biblioteca.libros = (
                    json_manager.cargar()
                )

                print(
                    Fore.GREEN
                    + "\nDatos cargados correctamente."
                )

                print(
                    f"Libros cargados: "
                    f"{len(biblioteca.libros)}"
                )

            except Exception as error:

                print(
                    Fore.RED
                    + f"\nError al cargar: {error}"
                )

            pausar()

        # =================================
        # SALIR
        # =================================

        elif opcion == "7":

            # Guardar automáticamente antes de salir
            json_manager.guardar(
                biblioteca.libros
            )

            print(
                Fore.CYAN
                + "\nDatos guardados."
            )

            print(
                Fore.CYAN
                + "¡Hasta luego!"
            )

            break

        # =================================
        # OPCIÓN INCORRECTA
        # =================================

        else:

            print(
                Fore.RED
                + "\nOpción inválida."
            )

            pausar()


if __name__ == "__main__":
    main()