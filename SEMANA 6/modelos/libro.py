# Clase Base: Representa un recurso general
class Recurso:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        # Encapsulación: Atributo privado (no accesible directamente desde fuera)
        self.__disponible = True 

    def mostrar_info(self):
        return f"Título: {self.titulo} | Autor: {self.autor}"

    # Método para acceder al atributo encapsulado
    def esta_disponible(self):
        return "Sí" if self.__disponible else "No"

# Clase Derivada (Herencia): Libro hereda de Recurso
class Libro(Recurso):
    def __init__(self, titulo, autor, num_paginas):
        # Llamada al constructor de la clase base
        super().__init__(titulo, autor)
        self.num_paginas = num_paginas

    # Polimorfismo: Sobrescribimos el método mostrar_info
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} | Páginas: {self.num_paginas} (Tipo: Libro)"