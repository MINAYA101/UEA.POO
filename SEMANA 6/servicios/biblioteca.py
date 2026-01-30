def imprimir_detalles_recurso(recurso):
    """
    Polimorfismo: No importa si el objeto es de la clase 'Recurso' o 'Libro',
    ambos responden al método 'mostrar_info' pero con implementaciones distintas.
    """
    print(recurso.mostrar_info())
    print(f"¿Disponible?: {recurso.esta_disponible()}")