import json
import os

from modelos.libro import Libro


class JSONManager:

    def __init__(self, ruta="datos/libros.json"):
        self.ruta = ruta

    def crear_archivo(self):
        carpeta = os.path.dirname(self.ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.ruta):
            with open(
                self.ruta,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump([], archivo, indent=4)

    def guardar(self, libros):
        self.crear_archivo()

        datos = []

        for libro in libros:
            datos.append(
                libro.convertir_diccionario()
            )

        with open(
            self.ruta,
            "w",
            encoding="utf-8"
        ) as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def cargar(self):
        self.crear_archivo()

        try:
            with open(
                self.ruta,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            libros = []

            for datos_libro in datos:
                libros.append(
                    Libro.desde_diccionario(datos_libro)
                )

            return libros

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def respaldo(self):
        self.crear_archivo()

        carpeta = os.path.dirname(self.ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        try:
            with open(
                self.ruta,
                "r",
                encoding="utf-8"
            ) as original:
                datos = json.load(original)

            with open(
                "datos/respaldo_libros.json",
                "w",
                encoding="utf-8"
            ) as respaldo:
                json.dump(
                    datos,
                    respaldo,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except (json.JSONDecodeError, FileNotFoundError):
            return False