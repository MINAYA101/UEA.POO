"""
Programa: Calculadora de Índice de Masa Corporal (IMC)
Descripción: Calcula el Índice de Masa Corporal basado en el peso y altura del usuario,
clasifica el resultado según categorías médicas estándar y determina si el valor es saludable.
"""

def calcular_indice_masa_corporal(peso_kg: float, altura_m: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC) usando la fórmula: IMC = peso / altura^2
    
    Args:
        peso_kg (float): Peso del usuario en kilogramos
        altura_m (float): Altura del usuario en metros
        
    Returns:
        float: Valor del IMC calculado
    """
    # Fórmula del IMC: peso dividido por la altura al cuadrado
    indice_imc = peso_kg / (altura_m ** 2)
    return indice_imc


def clasificar_imc(valor_imc: float) -> tuple[str, bool]:
    """
    Clasifica el IMC en categorías estándar y determina si es saludable
    
    Args:
        valor_imc (float): Valor del IMC calculado
        
    Returns:
        tuple: (categoria (str), es_saludable (bool))
    """
    # Rangos de IMC según la Organización Mundial de la Salud
    if valor_imc < 18.5:
        categoria = "Bajo peso"
        es_saludable = False
    elif 18.5 <= valor_imc < 25.0:
        categoria = "Peso normal"
        es_saludable = True
    elif 25.0 <= valor_imc < 30.0:
        categoria = "Sobrepeso"
        es_saludable = False
    else:  # valor_imc >= 30.0
        categoria = "Obesidad"
        es_saludable = False
        
    return categoria, es_saludable


def obtener_datos_usuario() -> tuple[float, float, str]:
    """
    Solicita y valida los datos del usuario
    
    Returns:
        tuple: (peso (float), altura (float), nombre (str))
    """
    # Datos del tipo string (nombre del usuario)
    nombre_usuario = input("Ingrese su nombre: ").strip()
    
    # Datos numéricos: enteros (edad) y flotantes (peso, altura)
    print("\n" + "="*40)
    print("DATOS PERSONALES")
    print("="*40)
    
    # Usamos int para la edad (número entero)
    while True:
        try:
            edad = int(input("Ingrese su edad (años completos): "))
            if edad <= 0 or edad > 120:
                print("Por favor, ingrese una edad válida (1-120 años)")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido")
    
    # Usamos float para peso y altura (números decimales)
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos (ej: 68.5): "))
            if peso <= 0 or peso > 300:
                print("Por favor, ingrese un peso válido (0-300 kg)")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    while True:
        try:
            altura = float(input("Ingrese su altura en metros (ej: 1.75): "))
            if altura <= 0 or altura > 2.5:
                print("Por favor, ingrese una altura válida (0-2.5 m)")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    return peso, altura, nombre_usuario, edad


def mostrar_resultados(nombre: str, edad: int, imc: float, categoria: str, es_saludable: bool):
    """
    Muestra los resultados del cálculo de manera formateada
    
    Args:
        nombre (str): Nombre del usuario
        edad (int): Edad del usuario
        imc (float): Valor del IMC calculado
        categoria (str): Categoría del IMC
        es_saludable (bool): Indica si el IMC está en rango saludable
    """
    print("\n" + "="*50)
    print("RESULTADOS DEL CÁLCULO DE IMC")
    print("="*50)
    
    # Mostrar información básica
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    
    # Mostrar IMC con 2 decimales
    print(f"\nIMC calculado: {imc:.2f}")
    
    # Mostrar categoría
    print(f"Categoría: {categoria}")
    
    # Usar booleano para mostrar mensaje personalizado
    if es_saludable:
        print("Estado: Rango saludable")
    else:
        print("Estado: Fuera del rango saludable")
        print("Recomendación: Consulte con un profesional de la salud")
    
    print("="*50)


def main():
    """
    Función principal que orquesta el programa completo
    """
    print("="*60)
    print("CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC)")
    print("="*60)
    print("Este programa calcula su IMC y lo clasifica según estándares médicos.")
    
    try:
        # Obtener datos del usuario
        peso_usuario, altura_usuario, nombre_usuario, edad_usuario = obtener_datos_usuario()
        
        # Calcular IMC (float)
        imc_calculado = calcular_indice_masa_corporal(peso_usuario, altura_usuario)
        
        # Clasificar IMC (devuelve string y boolean)
        categoria_imc, es_saludable = clasificar_imc(imc_calculado)
        
        # Mostrar resultados
        mostrar_resultados(nombre_usuario, edad_usuario, imc_calculado, 
                          categoria_imc, es_saludable)
        
        # Preguntar si desea calcular otro IMC
        print("\n¿Desea calcular otro IMC?")
        calcular_otro = input("Ingrese 'si' para continuar o cualquier tecla para salir: ").lower()
        
        # Control de flujo con booleano
        continuar = calcular_otro == 'si'
        
        if continuar:
            print("\n" + "-"*40)
            main()  # Llamada recursiva para nuevo cálculo
        else:
            print("\n¡Gracias por usar la calculadora de IMC!")
            
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()