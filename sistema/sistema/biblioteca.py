from modelos.libro import Libro

class Biblioteca:
def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            print("\n No hay libros registrados.\n")
            return

        for libro in self.libros:
            print(libro.mostrar())

    def buscar_por_id(self, id_libro):
        for libro in self.libros:
            if libro.id == id_libro:
                return libro
        return None

    def buscar_por_titulo(self, titulo):
        resultados = []

        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                resultados.append(libro)

        return resultados
    def editar_libro(self, id_libro, **datos):
        libro = self.buscar_por_id(id_libro)

        if libro is None:
            return False

        if "titulo" in datos:
            libro.titulo = datos["titulo"]

        if "autor" in datos:
            libro.autor = datos["autor"]

        if "anio" in datos:
            libro.anio = datos["anio"]

        if "genero" in datos:
            libro.genero = datos["genero"]

        if "paginas" in datos:
            libro.paginas = datos["paginas"]

        if "estado" in datos:
            libro.estado = datos["estado"]

        return True