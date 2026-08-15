import os

from sistema.biblioteca import Biblioteca
from archivos.json_manager import JSONManager
from modelos.libro import Libro


# ==========================================
# MANEJO DE COLORES
# ==========================================

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


# ==========================================
# FUNCIONES DE PANTALLA
# ==========================================

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


# ==========================================
# VALIDAR NÚMEROS
# ==========================================

def pedir_numero(mensaje, minimo=1, maximo=None):

    while True:

        valor = input(mensaje).strip()

        # Comprobar que solamente sean números
        if not valor.isdigit():

            print(
                Fore.RED
                + "❌ Debe ingresar solamente números."
            )

            continue

        numero = int(valor)

        # Comprobar mínimo
        if numero < minimo:

            print(
                Fore.RED
                + f"❌ El valor debe ser como mínimo {minimo}."
            )

            continue

        # Comprobar máximo
        if maximo is not None and numero > maximo:

            print(
                Fore.RED
                + f"❌ El valor no puede ser mayor que {maximo}."
            )

            continue

        return numero


# ==========================================
# VALIDAR TEXTO
# ==========================================

def pedir_texto(mensaje):

    while True:

        valor = input(mensaje).strip()

        if not valor:

            print(
                Fore.RED
                + "❌ Este campo no puede quedar vacío."
            )

            continue

        return valor


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():

    biblioteca = Biblioteca()
    json_manager = JSONManager()

    # Cargar libros existentes
    biblioteca.libros = json_manager.cargar()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        # ==================================
        # 1. AGREGAR LIBRO
        # ==================================

        if opcion == "1":

            print("\n--- AGREGAR LIBRO ---")

            # ID solamente números
            id_libro = pedir_numero(
                "ID del libro: ",
                minimo=1
            )

            # Comprobar ID repetido
            if biblioteca.buscar_por_id(id_libro) is not None:

                print(
                    Fore.RED
                    + "\n❌ Ya existe un libro con ese ID."
                )

                pausar()
                continue

            # Título obligatorio
            titulo = pedir_texto(
                "Título: "
            )

            # Autor obligatorio
            autor = pedir_texto(
                "Autor: "
            )

            # Año entre 1 y 2026
            anio = pedir_numero(
                "Año: ",
                minimo=1,
                maximo=2026
            )

            # Género obligatorio
            genero = pedir_texto(
                "Género: "
            )

            # Páginas entre 1 y 1000
            paginas = pedir_numero(
                "Cantidad de páginas: ",
                minimo=1,
                maximo=1000
            )

            # Crear libro
            libro = Libro(
                id_libro,
                titulo,
                autor,
                anio,
                genero,
                paginas
            )

            # Agregar a la biblioteca
            biblioteca.agregar_libro(libro)

            print(
                Fore.GREEN
                + "\n✅ Libro agregado correctamente."
            )

            pausar()

        # ==================================
        # 2. MOSTRAR LIBROS
        # ==================================

        elif opcion == "2":

            print("\n--- LISTA DE LIBROS ---")

            biblioteca.mostrar_libros()

            pausar()

        # ==================================
        # 3. BUSCAR LIBRO
        # ==================================

        elif opcion == "3":

            print("\n--- BUSCAR LIBRO ---")

            titulo = pedir_texto(
                "Ingrese el título a buscar: "
            )

            biblioteca.buscar_libro(titulo)

            pausar()

        # ==================================
        # 4. ELIMINAR LIBRO
        # ==================================

        elif opcion == "4":

            print("\n--- ELIMINAR LIBRO ---")

            titulo = pedir_texto(
                "Ingrese el título a eliminar: "
            )

            eliminado = biblioteca.eliminar_libro(
                titulo
            )

            if eliminado:

                json_manager.guardar(
                    biblioteca.libros
                )

            pausar()

        # ==================================
        # 5. GUARDAR DATOS
        # ==================================

        elif opcion == "5":

            try:

                json_manager.guardar(
                    biblioteca.libros
                )

                print(
                    Fore.GREEN
                    + "\n✅ Datos guardados correctamente."
                )

            except Exception as error:

                print(
                    Fore.RED
                    + f"\n❌ Error al guardar: {error}"
                )

            pausar()

        # ==================================
        # 6. CARGAR DATOS
        # ==================================

        elif opcion == "6":

            try:

                biblioteca.libros = (
                    json_manager.cargar()
                )

                print(
                    Fore.GREEN
                    + "\n✅ Datos cargados correctamente."
                )

                print(
                    f"Libros cargados: "
                    f"{len(biblioteca.libros)}"
                )

            except Exception as error:

                print(
                    Fore.RED
                    + f"\n❌ Error al cargar: {error}"
                )

            pausar()

        # ==================================
        # 7. SALIR
        # ==================================

        elif opcion == "7":

            try:

                # Guardar automáticamente
                json_manager.guardar(
                    biblioteca.libros
                )

                print(
                    Fore.CYAN
                    + "\n✅ Datos guardados."
                )

            except Exception as error:

                print(
                    Fore.RED
                    + f"\n❌ Error al guardar: {error}"
                )

            print(
                Fore.CYAN
                + "¡Hasta luego!"
            )

            break

        # ==================================
        # OPCIÓN INVÁLIDA
        # ==================================

        else:

            print(
                Fore.RED
                + "\n❌ Opción inválida."
            )

            pausar()


# ==========================================
# INICIAR PROGRAMA
# ==========================================

if __name__ == "__main__":
    main()