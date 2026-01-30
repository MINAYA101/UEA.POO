
from modelos.libro import Recurso, Libro
from servicios.biblioteca import imprimir_detalles_recurso

def ejecutar():
    # Crear instancias (Demostración)
    recurso_general = Recurso("Revista Científica", "Varios Autores")
    mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 496)

    print("--- DEMOSTRACIÓN DE POO ---")
    
    print("\n1. Objeto de Clase Base:")
    imprimir_detalles_recurso(recurso_general)

    print("\n2. Objeto de Clase Derivada (Herencia):")
    imprimir_detalles_recurso(mi_libro)

if __name__ == "__main__":
    ejecutar()