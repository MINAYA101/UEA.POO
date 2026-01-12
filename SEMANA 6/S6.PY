"""
Sistema de Gestión de Vehículos
Este programa demuestra conceptos de Programación Orientada a Objetos:
1. Definición de Clase y Objeto
2. Herencia
3. Encapsulación
4. Polimorfismo
"""


# ============================================
# CLASE BASE: DEMOSTRACIÓN DE ENCAPSULAMIENTO
# ============================================
class Vehiculo:
    """
    Clase base que representa un vehículo genérico.
    Demuestra encapsulación mediante atributos privados.
    """
    
    def __init__(self, marca, modelo, año):
        """
        Constructor de la clase Vehiculo.
        
        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo
            año (int): Año de fabricación
        """
        # Atributos privados (encapsulación) - solo accesibles desde la clase
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self.__año = año  # Atributo privado (doble guion bajo)
        self.__kilometraje = 0  # Atributo privado inicializado en 0
    
    # ========== MÉTODOS GETTER Y SETTER (ENCAPSULAMIENTO) ==========
    
    def get_marca(self):
        """Getter para obtener la marca del vehículo"""
        return self._marca
    
    def set_marca(self, nueva_marca):
        """Setter para modificar la marca del vehículo"""
        self._marca = nueva_marca
    
    def get_modelo(self):
        """Getter para obtener el modelo del vehículo"""
        return self._modelo
    
    def set_modelo(self, nuevo_modelo):
        """Setter para modificar el modelo del vehículo"""
        self._modelo = nuevo_modelo
    
    def get_año(self):
        """Getter para obtener el año del vehículo"""
        return self.__año
    
    def get_kilometraje(self):
        """Getter para obtener el kilometraje del vehículo"""
        return self.__kilometraje
    
    def aumentar_kilometraje(self, kilometros):
        """
        Método para aumentar el kilometraje del vehículo.
        
        Args:
            kilometros (float): Kilómetros a añadir al kilometraje actual
            
        Returns:
            bool: True si se pudo aumentar, False si los kilómetros son negativos
        """
        if kilometros >= 0:
            self.__kilometraje += kilometros
            return True
        else:
            print("Error: Los kilómetros no pueden ser negativos")
            return False
    
    # ========== MÉTODO POLIMÓRFICO (será sobrescrito) ==========
    
    def mostrar_info(self):
        """
        Método que muestra información básica del vehículo.
        Este método será sobrescrito en las clases derivadas (polimorfismo).
        
        Returns:
            str: Información del vehículo
        """
        return f"{self._marca} {self._modelo} ({self.__año}) - {self.__kilometraje} km"
    
    def arrancar(self):
        """
        Método para arrancar el vehículo.
        
        Returns:
            str: Mensaje de arranque
        """
        return "Vehículo arrancado"
    
    def calcular_antiguedad(self, año_actual):
        """
        Método para calcular la antigüedad del vehículo.
        
        Args:
            año_actual (int): Año actual para el cálculo
            
        Returns:
            int: Años de antigüedad del vehículo
        """
        return año_actual - self.__año


# ============================================
# CLASE DERIVADA 1: HERENCIA Y POLIMORFISMO
# ============================================
class Automovil(Vehiculo):
    """
    Clase derivada de Vehiculo que representa un automóvil.
    Demuestra herencia y polimorfismo (sobrescritura de métodos).
    """
    
    def __init__(self, marca, modelo, año, tipo_combustible, num_puertas):
        """
        Constructor de la clase Automovil.
        
        Args:
            marca (str): Marca del automóvil
            modelo (str): Modelo del automóvil
            año (int): Año de fabricación
            tipo_combustible (str): Tipo de combustible (gasolina, diesel, eléctrico)
            num_puertas (int): Número de puertas
        """
        # Llamada al constructor de la clase base (herencia)
        super().__init__(marca, modelo, año)
        
        # Atributos específicos de Automovil
        self.tipo_combustible = tipo_combustible
        self.num_puertas = num_puertas
        self.__nivel_combustible = 100  # Atributo privado específico
    
    # ========== MÉTODOS ESPECÍFICOS DE AUTOMOVIL ==========
    
    def get_nivel_combustible(self):
        """Getter para obtener el nivel de combustible"""
        return self.__nivel_combustible
    
    def repostar(self, cantidad):
        """
        Método para repostar combustible.
        
        Args:
            cantidad (float): Cantidad de combustible a añadir
            
        Returns:
            float: Nuevo nivel de combustible
        """
        if cantidad > 0:
            self.__nivel_combustible = min(100, self.__nivel_combustible + cantidad)
            return self.__nivel_combustible
        else:
            print("Error: La cantidad debe ser positiva")
            return self.__nivel_combustible
    
    def consumir_combustible(self, cantidad):
        """
        Método para consumir combustible.
        
        Args:
            cantidad (float): Cantidad de combustible a consumir
            
        Returns:
            float: Nuevo nivel de combustible
        """
        if cantidad > 0:
            self.__nivel_combustible = max(0, self.__nivel_combustible - cantidad)
            return self.__nivel_combustible
        else:
            print("Error: La cantidad debe ser positiva")
            return self.__nivel_combustible
    
    # ========== SOBRESCRITURA DE MÉTODOS (POLIMORFISMO) ==========
    
    def mostrar_info(self):
        """
        Sobrescritura del método mostrar_info de la clase base.
        Demuestra polimorfismo al modificar el comportamiento del método.
        
        Returns:
            str: Información detallada del automóvil
        """
        info_base = super().mostrar_info()
        return (f"{info_base}\n"
                f"  Tipo: Automóvil\n"
                f"  Combustible: {self.tipo_combustible}\n"
                f"  Puertas: {self.num_puertas}\n"
                f"  Combustible: {self.__nivel_combustible}%")
    
    def arrancar(self):
        """
        Sobrescritura del método arrancar de la clase base.
        
        Returns:
            str: Mensaje de arranque específico para automóvil
        """
        if self.__nivel_combustible > 0:
            return f"Automóvil {self.get_marca()} {self.get_modelo()} arrancado. Nivel de combustible: {self.__nivel_combustible}%"
        else:
            return f"¡Advertencia! Nivel de combustible bajo: {self.__nivel_combustible}%"


# ============================================
# CLASE DERIVADA 2: HERENCIA Y POLIMORFISMO
# ============================================
class Motocicleta(Vehiculo):
    """
    Clase derivada de Vehiculo que representa una motocicleta.
    Demuestra herencia y polimorfismo (sobrescritura de métodos).
    """
    
    def __init__(self, marca, modelo, año, tipo_moto, cilindrada):
        """
        Constructor de la clase Motocicleta.
        
        Args:
            marca (str): Marca de la motocicleta
            modelo (str): Modelo de la motocicleta
            año (int): Año de fabricación
            tipo_moto (str): Tipo de motocicleta (deportiva, cruiser, etc.)
            cilindrada (int): Cilindrada en cc
        """
        # Llamada al constructor de la clase base (herencia)
        super().__init__(marca, modelo, año)
        
        # Atributos específicos de Motocicleta
        self.tipo_moto = tipo_moto
        self.cilindrada = cilindrada
        self.__casco_guardado = True  # Atributo privado específico
    
    # ========== MÉTODOS ESPECÍFICOS DE MOTOCICLETA ==========
    
    def get_casco_guardado(self):
        """Getter para verificar si el casco está guardado"""
        return self.__casco_guardado
    
    def guardar_casco(self):
        """Método para guardar el casco"""
        self.__casco_guardado = True
        return "Casco guardado correctamente"
    
    def sacar_casco(self):
        """Método para sacar el casco"""
        self.__casco_guardado = False
        return "Casco sacado correctamente"
    
    # ========== SOBRESCRITURA DE MÉTODOS (POLIMORFISMO) ==========
    
    def mostrar_info(self):
        """
        Sobrescritura del método mostrar_info de la clase base.
        Demuestra polimorfismo al modificar el comportamiento del método.
        
        Returns:
            str: Información detallada de la motocicleta
        """
        info_base = super().mostrar_info()
        return (f"{info_base}\n"
                f"  Tipo: Motocicleta\n"
                f"  Categoría: {self.tipo_moto}\n"
                f"  Cilindrada: {self.cilindrada}cc\n"
                f"  Casco guardado: {'Sí' if self.__casco_guardado else 'No'}")
    
    def arrancar(self):
        """
        Sobrescritura del método arrancar de la clase base.
        
        Returns:
            str: Mensaje de arranque específico para motocicleta
        """
        if self.__casco_guardado:
            return f"Motocicleta {self.get_marca()} {self.get_modelo()} arrancada. ¡Recuerda usar casco!"
        else:
            return f"Motocicleta {self.get_marca()} {self.get_modelo()} arrancada. Casco disponible."


# ============================================
# FUNCIÓN QUE DEMUESTRA POLIMORFISMO
# ============================================
def probar_vehiculos(lista_vehiculos):
    """
    Función que demuestra polimorfismo al trabajar con diferentes tipos de vehículos.
    
    Args:
        lista_vehiculos (list): Lista de objetos Vehiculo o sus derivados
    """
    print("\n" + "="*60)
    print("DEMOSTRACIÓN DE POLIMORFISMO")
    print("="*60)
    
    for i, vehiculo in enumerate(lista_vehiculos, 1):
        print(f"\n--- Vehículo {i} ---")
        # Polimorfismo: el mismo método se comporta diferente según el tipo de vehículo
        print(vehiculo.mostrar_info())
        print(vehiculo.arrancar())
        
        # Demostrar métodos específicos según el tipo
        if isinstance(vehiculo, Automovil):
            print(f"Nivel de combustible: {vehiculo.get_nivel_combustible()}%")
            vehiculo.consumir_combustible(20)
            print(f"Después de conducir: {vehiculo.get_nivel_combustible()}%")
        elif isinstance(vehiculo, Motocicleta):
            estado_casco = "guardado" if vehiculo.get_casco_guardado() else "sacado"
            print(f"Estado del casco: {estado_casco}")


# ============================================
# FUNCIÓN PRINCIPAL DEL PROGRAMA
# ============================================
def main():
    """
    Función principal del programa que demuestra todos los conceptos de POO.
    """
    print("="*60)
    print("SISTEMA DE GESTIÓN DE VEHÍCULOS - DEMOSTRACIÓN DE POO")
    print("="*60)
    
    # ========== CREACIÓN DE INSTANCIAS (OBJETOS) ==========
    
    print("\n1. CREACIÓN DE VEHÍCULOS (INSTANCIACIÓN DE OBJETOS)")
    print("-"*50)
    
    # Crear un automóvil (instancia de Automovil)
    mi_auto = Automovil("Toyota", "Corolla", 2022, "Híbrido", 4)
    print(f"Automóvil creado: {mi_auto.get_marca()} {mi_auto.get_modelo()}")
    
    # Crear una motocicleta (instancia de Motocicleta)
    mi_moto = Motocicleta("Harley-Davidson", "Sportster", 2023, "Cruiser", 1200)
    print(f"Motocicleta creada: {mi_moto.get_marca()} {mi_moto.get_modelo()}")
    
    # Crear otro vehículo para demostración
    otro_auto = Automovil("Tesla", "Model 3", 2024, "Eléctrico", 4)
    print(f"Otro automóvil creado: {otro_auto.get_marca()} {otro_auto.get_modelo()}")
    
    # ========== DEMOSTRACIÓN DE ENCAPSULAMIENTO ==========
    
    print("\n\n2. DEMOSTRACIÓN DE ENCAPSULAMIENTO")
    print("-"*50)
    
    # Acceder a atributos mediante getters (encapsulación)
    print(f"Marca del auto (getter): {mi_auto.get_marca()}")
    print(f"Año del auto (getter): {mi_auto.get_año()}")
    print(f"Kilometraje inicial: {mi_auto.get_kilometraje()} km")
    
    # Modificar atributos mediante setters (encapsulación)
    mi_auto.set_marca("Toyota Modificado")
    print(f"Nueva marca del auto (setter): {mi_auto.get_marca()}")
    
    # Aumentar kilometraje usando método controlado
    mi_auto.aumentar_kilometraje(150.5)
    print(f"Kilometraje después de viaje: {mi_auto.get_kilometraje()} km")
    
    # Intentar aumentar con valor negativo (será rechazado)
    print("Intentando aumentar kilometraje con valor negativo...")
    mi_auto.aumentar_kilometraje(-50)
    print(f"Kilometraje después del intento: {mi_auto.get_kilometraje()} km")
    
    # ========== DEMOSTRACIÓN DE HERENCIA ==========
    
    print("\n\n3. DEMOSTRACIÓN DE HERENCIA")
    print("-"*50)
    
    # Mostrar que Motocicleta hereda de Vehiculo
    print(f"¿mi_moto es instancia de Vehiculo? {isinstance(mi_moto, Vehiculo)}")
    print(f"¿mi_moto es instancia de Motocicleta? {isinstance(mi_moto, Motocicleta)}")
    
    # Acceder a método heredado de la clase base
    antiguedad = mi_moto.calcular_antiguedad(2025)
    print(f"Antigüedad de la motocicleta (método heredado): {antiguedad} años")
    
    # ========== DEMOSTRACIÓN DE POLIMORFISMO ==========
    
    # Crear lista de vehículos de diferentes tipos
    vehiculos = [mi_auto, mi_moto, otro_auto]
    
    # Llamar a función polimórfica
    probar_vehiculos(vehiculos)
    
    # ========== DEMOSTRACIÓN ADICIONAL ==========
    
    print("\n\n4. OPERACIONES ESPECÍFICAS POR TIPO DE VEHÍCULO")
    print("-"*50)
    
    # Operaciones específicas para Automovil
    print("\n--- Operaciones con Automóvil ---")
    print(f"Nivel de combustible inicial: {mi_auto.get_nivel_combustible()}%")
    mi_auto.consumir_combustible(30)
    print(f"Después de consumir 30%: {mi_auto.get_nivel_combustible()}%")
    mi_auto.repostar(25)
    print(f"Después de repostar 25%: {mi_auto.get_nivel_combustible()}%")
    
    # Operaciones específicas para Motocicleta
    print("\n--- Operaciones con Motocicleta ---")
    print(f"¿Casco guardado? {mi_moto.get_casco_guardado()}")
    print(mi_moto.sacar_casco())
    print(f"¿Casco guardado ahora? {mi_moto.get_casco_guardado()}")
    print(mi_moto.guardar_casco())
    print(f"¿Casco guardado finalmente? {mi_moto.get_casco_guardado()}")
    
    print("\n" + "="*60)
    print("DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("="*60)


# ============================================
# EJECUCIÓN DEL PROGRAMA
# ============================================
if __name__ == "__main__":
    main()