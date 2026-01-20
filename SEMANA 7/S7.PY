"""
Programa que demuestra el uso de constructores y destructores en Python
Contiene varias clases con diferentes tipos de recursos que requieren
inicialización y limpieza adecuadas.
"""

import time
import os


class ArchivoLogger:
    """
    Clase que maneja un archivo de log. 
    El constructor abre el archivo y el destructor asegura su cierre.
    """
    
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase ArchivoLogger.
        Inicializa el archivo de log y escribe un mensaje de inicio.
        
        Parámetros:
        - nombre_archivo: str - nombre del archivo donde se guardarán los logs
        """
        print(f"[ArchivoLogger] Constructor llamado: creando log en {nombre_archivo}")
        
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'a', encoding='utf-8')
        self.contador = 0
        
        # Escribimos un mensaje inicial en el log
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.archivo.write(f"[{timestamp}] --- INICIO DE LOG ---\n")
        print(f"[ArchivoLogger] Archivo {nombre_archivo} abierto correctamente")
    
    def escribir_log(self, mensaje):
        """
        Escribe un mensaje en el archivo de log.
        
        Parámetros:
        - mensaje: str - mensaje a escribir en el log
        """
        self.contador += 1
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entrada = f"[{timestamp}] [{self.contador:03d}] {mensaje}\n"
        self.archivo.write(entrada)
        self.archivo.flush()  # Forzamos escritura inmediata
        print(f"[ArchivoLogger] Mensaje escrito en log: {mensaje}")
    
    def __del__(self):
        """
        Destructor de la clase ArchivoLogger.
        Asegura que el archivo se cierre correctamente y escribe un mensaje final.
        """
        # Verificamos si el archivo existe antes de intentar cerrarlo
        if hasattr(self, 'archivo') and not self.archivo.closed:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            self.archivo.write(f"[{timestamp}] --- FIN DE LOG ({self.contador} mensajes) ---\n")
            self.archivo.close()
            print(f"[ArchivoLogger] Destructor llamado: archivo {self.nombre_archivo} cerrado")
        else:
            print("[ArchivoLogger] Destructor llamado: archivo ya estaba cerrado o no existía")


class ConexionSimulada:
    """
    Clase que simula una conexión a un recurso externo (base de datos, API, etc.).
    El constructor establece la conexión y el destructor asegura su cierre.
    """
    
    def __init__(self, servidor, puerto):
        """
        Constructor de la clase ConexionSimulada.
        Simula la conexión a un servidor.
        
        Parámetros:
        - servidor: str - dirección del servidor
        - puerto: int - puerto de conexión
        """
        print(f"[ConexionSimulada] Constructor llamado: conectando a {servidor}:{puerto}")
        
        self.servidor = servidor
        self.puerto = puerto
        self.conectado = False
        self.id_conexion = None
        
        # Simulamos el proceso de conexión
        print(f"[ConexionSimulada] Estableciendo conexión con {servidor}...")
        time.sleep(0.5)  # Simulamos latencia
        
        # Generamos un ID único para la conexión (simulado)
        self.id_conexion = hash(f"{servidor}:{puerto}:{time.time()}") % 10000
        self.conectado = True
        
        print(f"[ConexionSimulada] Conexión establecida. ID: {self.id_conexion}")
    
    def enviar_datos(self, datos):
        """
        Envía datos a través de la conexión simulada.
        
        Parámetros:
        - datos: str - datos a enviar
        
        Retorna:
        - bool - True si los datos se enviaron correctamente
        """
        if self.conectado:
            print(f"[ConexionSimulada] Enviando datos: '{datos}' a {self.servidor}")
            return True
        else:
            print(f"[ConexionSimulada] Error: No hay conexión activa")
            return False
    
    def __del__(self):
        """
        Destructor de la clase ConexionSimulada.
        Asegura que la conexión se cierre correctamente.
        """
        if hasattr(self, 'conectado') and self.conectado:
            print(f"[ConexionSimulada] Destructor llamado: cerrando conexión {self.id_conexion}...")
            # Simulamos el cierre de conexión
            time.sleep(0.3)
            self.conectado = False
            print(f"[ConexionSimulada] Conexión {self.id_conexion} cerrada correctamente")
        else:
            print("[ConexionSimulada] Destructor llamado: no había conexión activa")


class SistemaSensor:
    """
    Clase que simula un sistema de sensores.
    El constructor inicializa los sensores y el destructor los apaga.
    """
    
    def __init__(self, nombre_sistema, num_sensores):
        """
        Constructor de la clase SistemaSensor.
        Inicializa el sistema de sensores.
        
        Parámetros:
        - nombre_sistema: str - nombre del sistema de sensores
        - num_sensores: int - número de sensores a inicializar
        """
        print(f"[SistemaSensor] Constructor llamado: inicializando {nombre_sistema}")
        
        self.nombre = nombre_sistema
        self.num_sensores = num_sensores
        self.sensores_activos = []
        self.activo = True
        
        # Inicializamos los sensores
        for i in range(num_sensores):
            sensor_id = f"SENSOR_{i+1:03d}"
            self.sensores_activos.append(sensor_id)
            print(f"[SistemaSensor] Sensor {sensor_id} inicializado")
        
        print(f"[SistemaSensor] Sistema '{nombre_sistema}' listo con {num_sensores} sensores")
    
    def leer_sensor(self, sensor_id):
        """
        Lee el valor de un sensor específico.
        
        Parámetros:
        - sensor_id: str - identificador del sensor a leer
        
        Retorna:
        - float - valor simulado del sensor
        """
        if sensor_id in self.sensores_activos and self.activo:
            # Simulamos una lectura aleatoria
            import random
            lectura = random.uniform(20.0, 30.0)
            print(f"[SistemaSensor] Lectura de {sensor_id}: {lectura:.2f}°C")
            return lectura
        else:
            print(f"[SistemaSensor] Error: Sensor {sensor_id} no disponible")
            return None
    
    def __del__(self):
        """
        Destructor de la clase SistemaSensor.
        Apaga todos los sensores de manera segura.
        """
        print(f"[SistemaSensor] Destructor llamado: apagando sistema '{self.nombre}'")
        
        if hasattr(self, 'activo') and self.activo:
            # Apagamos todos los sensores en orden inverso
            for sensor_id in reversed(self.sensores_activos):
                print(f"[SistemaSensor] Apagando sensor {sensor_id}...")
                time.sleep(0.1)  # Simulamos tiempo de apagado
            
            self.activo = False
            self.sensores_activos.clear()
            print(f"[SistemaSensor] Sistema '{self.nombre}' apagado correctamente")


def demostrar_ciclo_vida():
    """
    Función que demuestra el ciclo de vida de los objetos
    y cómo se llaman los constructores y destructores.
    """
    print("\n" + "="*60)
    print("DEMOSTRACIÓN DEL CICLO DE VIDA DE OBJETOS")
    print("="*60)
    
    # Creación de objetos - se llaman los constructores
    print("\n--- FASE 1: Creación de objetos ---")
    logger = ArchivoLogger("app.log")
    conexion = ConexionSimulada("servidor.db", 5432)
    sensores = SistemaSensor("Sistema Climático", 3)
    
    # Uso de los objetos
    print("\n--- FASE 2: Uso de los objetos ---")
    
    logger.escribir_log("Iniciando aplicación")
    
    if conexion.enviar_datos("SELECT * FROM temperaturas"):
        logger.escribir_log("Consulta a base de datos exitosa")
    
    temperatura = sensores.leer_sensor("SENSOR_002")
    if temperatura:
        logger.escribir_log(f"Temperatura leída: {temperatura:.2f}°C")
    
    logger.escribir_log("Operaciones completadas")
    
    # Los destructores se llamarán automáticamente cuando:
    # 1. Salgamos de esta función (objetos locales)
    # 2. Eliminemos explícitamente los objetos con 'del'
    # 3. Cuando el recolector de basura de Python los elimine
    print("\n--- FASE 3: Fin de la función - destructores se llamarán ---")
    
    # Nota: Los destructores se llamarán automáticamente al salir de la función
    # pero podemos forzar su llamada con 'del' para demostrarlo
    print("\n--- FASE 4: Llamada explícita a destructores ---")
    
    # Eliminamos explícitamente los objetos
    del conexion  # Se llamará al destructor de ConexionSimulada
    
    # Creamos y destruimos un objeto temporal
    print("\n--- Objeto temporal creado y destruido inmediatamente ---")
    temp_conexion = ConexionSimulada("temporal.db", 8080)
    temp_conexion.enviar_datos("DATOS_TEST")
    del temp_conexion  # Destructor llamado inmediatamente


def demostrar_contexto_anidado():
    """
    Demuestra cómo se comportan los destructores en contextos anidados.
    """
    print("\n" + "="*60)
    print("DEMOSTRACIÓN EN CONTEXTO ANIDADO")
    print("="*60)
    
    print("\nEntrando en contexto anidado...")
    
    # Objeto creado en un contexto externo
    logger_externo = ArchivoLogger("externo.log")
    logger_externo.escribir_log("Contexto externo iniciado")
    
    # Contexto interno
    with open("archivo_temporal.txt", "w") as f:
        f.write("Datos temporales\n")
        
        # Objeto creado en contexto interno
        logger_interno = ArchivoLogger("interno.log")
        logger_interno.escribir_log("Contexto interno iniciado")
        
        # Al salir del bloque 'with', logger_interno será destruido
        print("\nSaliendo del contexto interno...")
    
    print("\nVolviendo al contexto externo...")
    logger_externo.escribir_log("Contexto externo activo")
    
    # Al final de la función, logger_externo será destruido


def main():
    """
    Función principal que ejecuta las demostraciones.
    """
    print("PROGRAMA DEMOSTRATIVO: CONSTRUCTORES Y DESTRUCTORES EN PYTHON")
    print("="*60)
    
    # Demostración del ciclo de vida básico
    demostrar_ciclo_vida()
    
    # Pequeña pausa entre demostraciones
    time.sleep(1)
    
    # Demostración de contexto anidado
    demostrar_contexto_anidado()
    
    print("\n" + "="*60)
    print("PROGRAMA COMPLETADO")
    print("="*60)
    
    # Verificamos que los archivos de log se crearon
    print("\nVerificación de archivos creados:")
    for archivo in ["app.log", "externo.log", "interno.log"]:
        if os.path.exists(archivo):
            print(f"✓ {archivo} creado correctamente")
        else:
            print(f"✗ {archivo} no encontrado")


# Punto de entrada del programa
if __name__ == "__main__":
    main()