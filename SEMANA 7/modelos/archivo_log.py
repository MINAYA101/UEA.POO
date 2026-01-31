class ArchivoLog:
    """
    Clase que representa un archivo de registro (log).
    Demuestra el uso de __init__ para abrir recursos y __del__ para liberarlos.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor: Inicializa el estado del objeto.
        - Se ejecuta al crear una instancia de la clase.
        - Abre un archivo en modo 'append' para simular un log persistente.
        - Inicializa atributos obligatorios como el nombre del archivo.
        """
        self.nombre_archivo = nombre_archivo
        try:
            # Simulamos la apertura de un recurso (archivo)
            self.archivo = open(self.nombre_archivo, "a", encoding="utf-8")
            print(f"[CONSTRUCTOR] Recurso '{self.nombre_archivo}' abierto exitosamente.")
        except Exception as e:
            print(f"[ERROR] No se pudo abrir el archivo: {e}")
            self.archivo = None

    def registrar_evento(self, mensaje):
        """Método para escribir en el recurso abierto."""
        if self.archivo:
            self.archivo.write(f"EVENTO: {mensaje}\n")
            print(f"[LOG] Mensaje registrado: {mensaje}")

    def __del__(self):
        """
        Destructor: Realiza la limpieza de recursos.
        - Se ejecuta cuando el objeto es destruido por el recolector de basura (GC).
        - Situaciones comunes: el objeto sale de alcance, se usa 'del' o el programa termina.
        - Aquí cerramos el archivo para asegurar que los datos se guarden y liberar memoria.
        """
        if hasattr(self, 'archivo') and self.archivo:
            self.archivo.close()
            print(f"[DESTRUCTOR] Recurso '{self.nombre_archivo}' cerrado y liberado.")
        else:
            print(f"[DESTRUCTOR] El objeto '{self.nombre_archivo}' dejó de existir (sin recursos abiertos).")
