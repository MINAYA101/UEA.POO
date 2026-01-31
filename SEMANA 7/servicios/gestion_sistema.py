from modelos.archivo_log import ArchivoLog
from modelos.conexion_db import ConexionBaseDatos

class GestionSistema:
    """
    Capa de Servicios: Gestiona la lógica del sistema.
    Usa los modelos para realizar operaciones complejas.
    """

    def __init__(self):
        """
        Constructor del servicio.
        Inicializa los componentes necesarios para que el sistema funcione.
        """
        print("[SERVICIO] Iniciando el gestor del sistema...")
        self.logger = ArchivoLog("sistema_log.txt")
        self.db = ConexionBaseDatos("localhost", "mi_empresa_db")

    def procesar_transaccion(self, usuario, monto):
        """
        Lógica de negocio: Registra una transacción en la DB y en el Log.
        """
        print(f"[SERVICIO] Procesando transacción para {usuario}...")
        self.db.ejecutar_consulta(f"INSERT INTO transacciones (usuario, monto) VALUES ('{usuario}', {monto})")
        self.logger.registrar_evento(f"Transacción exitosa: {usuario} - ${monto}")

    def finalizar_operaciones(self):
        """
        Método para demostrar la destrucción manual o controlada.
        """
        print("[SERVICIO] Finalizando operaciones del sistema...")
        # Al eliminar estas referencias, se activarán sus destructores (__del__)
        del self.db
        del self.logger

    def __del__(self):
        """
        Destructor del servicio.
        Asegura que si el servicio se destruye, se notifique el cierre del sistema.
        """
        print("[SERVICIO] El Gestor del Sistema ha sido destruido.")
