from datetime import datetime



class Libro:
    def __init__(self,id_libro,titulo,autor,anio,genero,paginas,
            estado="Disponible"):
        
        self.id = id_libro
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.anio = anio
        self.genero = genero.strip()
        self.paginas = paginas
        self.estado = estado
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y/ %H:%M:%S")
    
    def mostrar(self):
        return(
        f"\n{'=' * 45}\n" 
        f"ID:{self.id}\n"
        f"Titulo:{self.titulo}\n"
        f"Autor:{self.autor}\n"
        f"Año:{self.anio}\n"
        f"Género: {self.genero}\n"
        f"Páginas: {self.paginas}\n"
        f"estado:{self.estado}\n"
        f"fecha de registro:{self.fecha_registro}\n"
                f"{'=' * 45}"
            )
    def convert_diccionario(self):
            return{
                "id":self.id,
                "titulo":self.titulo,
                "autor":self.autor,
                "anio":self.anio,
                "genero": self.genero,
                "paginas":
    self.paginas,
            "estado":self.estado,
            "fecha_registro":
    self.fecha_registro
        }
    @classmethod
    def desde_diccionario(cls, datos):
            libro=cls(
                datos["id"],
                datos["titulo"],
                datos["autor"],
                datos["anio"],
                datos["genero"],
                datos["paginas"],
                datos["estado"]
                )
            libro.fecha_registro=datos.get(
                "fecha_registro",
                
        datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            )
            return libro

        