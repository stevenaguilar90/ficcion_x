from modelos.libro import Libro


class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            print("\nNo hay libros registrados.\n")
            return

        for libro in self.libros:
            print(libro.mostrar())

    def buscar_por_id(self, id_libro):
        for libro in self.libros:
            if str(libro.id) == str(id_libro):
                return libro

        return None

    def buscar_libro(self, titulo):
        resultados = []

        for libro in self.libros:
            if titulo.lower().strip() in libro.titulo.lower():
                resultados.append(libro)

        if resultados:
            print("\n--- LIBROS ENCONTRADOS ---")

            for libro in resultados:
                print(libro.mostrar())

            return True

        print("\nNo se encontró ningún libro.")
        return False

    def buscar_por_titulo(self, titulo):
        resultados = []

        for libro in self.libros:
            if titulo.lower().strip() in libro.titulo.lower():
                resultados.append(libro)

        return resultados

    def editar_libro(self, id_libro, **datos):
        libro = self.buscar_por_id(id_libro)

        if libro is None:
            return False

        if "titulo" in datos:
            libro.titulo = datos["titulo"].strip()

        if "autor" in datos:
            libro.autor = datos["autor"].strip()

        if "anio" in datos:
            libro.anio = datos["anio"]

        if "genero" in datos:
            libro.genero = datos["genero"].strip()

        if "paginas" in datos:
            libro.paginas = datos["paginas"]

        if "estado" in datos:
            libro.estado = datos["estado"]

        return True

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower().strip() == titulo.lower().strip():
                self.libros.remove(libro)
                print("\nLibro eliminado correctamente.")
                return True

        print("\nNo se encontró el libro.")
        return False