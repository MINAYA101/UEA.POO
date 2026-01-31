class ConexionBaseDatos:
    """
    Clase que representa una conexión simulada a una base de datos.
    Demuestra el uso de __init__ para establecer conexiones y __del__ para cerrarlas.
    """

    def __init__(self, servidor, base_datos):
        """
        Constructor: Inicializa los datos de conexión.
        - Define el estado inicial del objeto con los parámetros obligatorios.
        - Simula el establecimiento de una conexión de red.
        """
        self.servidor = servidor
        self.base_datos = base_datos
        self.conectado = True
        print(f"[CONSTRUCTOR] Conexión establecida con {self.servidor}/{self.base_datos}.")

    def ejecutar_consulta(self, query):
        """Simula la ejecución de una consulta SQL."""
        if self.conectado:
            print(f"[DB] Ejecutando: {query}")
        else:
            print("[ERROR] No hay conexión activa.")

    def __del__(self):
        """
        Destructor: Cierra la conexión simulada.
        - Se ejecuta automáticamente cuando ya no hay referencias al objeto.
        - Garantiza que la conexión no quede 'colgada' en el servidor.
        """
        self.conectado = False
        print(f"[DESTRUCTOR] Conexión con {self.servidor} cerrada correctamente.")
