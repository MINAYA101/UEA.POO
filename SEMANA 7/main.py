import time
from servicios.gestion_sistema import GestionSistema

def demostracion_ciclo_vida():
    """
    Función para demostrar cómo se crean y destruyen los objetos.
    """
    print("--- INICIO DE LA DEMOSTRACIÓN ---")
    
    # 1. Creación del objeto (Se ejecuta __init__)
    print("\n1. Instanciando el servicio...")
    sistema = GestionSistema()
    
    # 2. Uso del objeto
    print("\n2. Ejecutando lógica de negocio...")
    sistema.procesar_transaccion("Juan Perez", 1500.50)
    sistema.procesar_transaccion("Maria Lopez", 2300.00)
    
    # 3. Demostración de destrucción controlada
    print("\n3. Forzando la liberación de recursos internos...")
    sistema.finalizar_operaciones()
    
    print("\n4. El objeto 'sistema' sigue existiendo en este scope, pero sus recursos internos ya fueron liberados.")
    time.sleep(1) # Pausa para visualizar los mensajes en consola

    print("\n--- FIN DE LA FUNCIÓN (El objeto 'sistema' saldrá de alcance) ---")

if __name__ == "__main__":
    # Ejecutamos la demostración
    demostracion_ciclo_vida()
    
    # Al terminar la función, el recolector de basura de Python destruirá el objeto 'sistema'
    # y se ejecutará su método __del__.
    print("\n[MAIN] El programa principal ha terminado su ejecución.")
