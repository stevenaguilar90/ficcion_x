import json
import os
from modelos.libro import Libro


class JSONManager:

    def __init__(self, ruta="datos/libros.json"):
        self.ruta = ruta

        def guardar(self, libros):
            datos = [libro.convertir_diccionario() for libro in libros]

            with open(self.ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

                def cargar(self):
                    if not os.path.exists(self.ruta):
                        return []
                    
                    try:
                        with open(self.ruta, "r", encoding="utf-8") as archivo:
                            datos = json.load(archivo)

                            return [Libro.desde_diccionario(libro) for libro in datos]
                        
                    except (json.JSONDecodeError, FileNotFoundError):
                        return []
                       
                def crear_archivo(self):
                    if not os.path.exists(self.ruta):
                        with open(self.ruta, "w", encoding="utf-8") as archivo:
                            json.dump([], archivo, indent=4)

                            def respaldo(self):
                                if os.path.exists(self.ruta):

                                    with open(self.ruta, "r", encoding="utf-8") as original:
                                        datos = json.load(original)

                                        with open("datos/respaldo_libros.json", "w", encoding="utf-8") as respaldo:
                                            json.dump(datos, respaldo, indent=4, ensure_ascii=False)
                                            