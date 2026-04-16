# Convertidor unitario en Python
# Autor: Asistente
# Descripción: Convierte entre diferentes unidades de longitud, masa, temperatura, volumen y tiempo.

import sys

# ==================== FUNCIONES DE CONVERSIÓN ====================

def convertir_longitud(valor, desde, hasta):
    """
    Convierte unidades de longitud usando el metro como unidad base.
    """
    # Factores de conversión a metros
    a_metros = {
        'metros': 1,
        'kilometros': 1000,
        'centimetros': 0.01,
        'milimetros': 0.001,
        'millas': 1609.34,
        'pies': 0.3048,
        'pulgadas': 0.0254,
        'yardas': 0.9144
    }
    
    if desde not in a_metros or hasta not in a_metros:
        return None
    # Convertir a metros y luego a la unidad deseada
    en_metros = valor * a_metros[desde]
    resultado = en_metros / a_metros[hasta]
    return resultado

def convertir_masa(valor, desde, hasta):
    """
    Convierte unidades de masa usando el gramo como unidad base.
    """
    a_gramos = {
        'gramos': 1,
        'kilogramos': 1000,
        'libras': 453.592,
        'onzas': 28.3495
    }
    
    if desde not in a_gramos or hasta not in a_gramos:
        return None
    en_gramos = valor * a_gramos[desde]
    resultado = en_gramos / a_gramos[hasta]
    return resultado

def convertir_temperatura(valor, desde, hasta):
    """
    Convierte entre Celsius, Fahrenheit y Kelvin usando fórmulas directas.
    """
    # Primero convertir a Celsius como base
    if desde == 'celsius':
        celsius = valor
    elif desde == 'fahrenheit':
        celsius = (valor - 32) * 5/9
    elif desde == 'kelvin':
        celsius = valor - 273.15
    else:
        return None
    
    # Luego convertir desde Celsius a la unidad final
    if hasta == 'celsius':
        return celsius
    elif hasta == 'fahrenheit':
        return celsius * 9/5 + 32
    elif hasta == 'kelvin':
        return celsius + 273.15
    else:
        return None

def convertir_volumen(valor, desde, hasta):
    """
    Convierte unidades de volumen usando el litro como unidad base.
    """
    a_litros = {
        'litros': 1,
        'mililitros': 0.001,
        'galones': 3.78541,
        'pies_cubicos': 28.3168
    }
    
    if desde not in a_litros or hasta not in a_litros:
        return None
    en_litros = valor * a_litros[desde]
    resultado = en_litros / a_litros[hasta]
    return resultado

def convertir_tiempo(valor, desde, hasta):
    """
    Convierte unidades de tiempo usando el segundo como unidad base.
    """
    a_segundos = {
        'segundos': 1,
        'minutos': 60,
        'horas': 3600,
        'dias': 86400
    }
    
    if desde not in a_segundos or hasta not in a_segundos:
        return None
    en_segundos = valor * a_segundos[desde]
    resultado = en_segundos / a_segundos[hasta]
    return resultado

# ==================== INTERFAZ DE USUARIO ====================

def mostrar_menu():
    print("\n" + "="*50)
    print("      CONVERTIDOR UNITARIO")
    print("="*50)
    print("1. Longitud")
    print("2. Masa")
    print("3. Temperatura")
    print("4. Volumen")
    print("5. Tiempo")
    print("0. Salir")
    print("-"*50)

def obtener_unidades(categoria):
    """
    Devuelve un diccionario con las unidades disponibles para cada categoría.
    """
    unidades = {
        1: ['metros', 'kilometros', 'centimetros', 'milimetros', 'millas', 'pies', 'pulgadas', 'yardas'],
        2: ['gramos', 'kilogramos', 'libras', 'onzas'],
        3: ['celsius', 'fahrenheit', 'kelvin'],
        4: ['litros', 'mililitros', 'galones', 'pies_cubicos'],
        5: ['segundos', 'minutos', 'horas', 'dias']
    }
    return unidades.get(categoria, [])

def pedir_unidad(lista_unidades, mensaje):
    """
    Pide al usuario que elija una unidad de la lista dada.
    """
    print(mensaje)
    for i, unidad in enumerate(lista_unidades, 1):
        print(f"  {i}. {unidad.capitalize()}")
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= len(lista_unidades):
                return lista_unidades[opcion-1]
            else:
                print(f"Opción inválida. Elija entre 1 y {len(lista_unidades)}.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una categoría (0-5): ").strip()
        
        if opcion == '0':
            print("¡Gracias por usar el convertidor! Hasta luego.")
            sys.exit()
        
        if opcion not in ['1', '2', '3', '4', '5']:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        categoria = int(opcion)
        unidades_disponibles = obtener_unidades(categoria)
        
        # Mostrar unidades disponibles y pedir la unidad de origen
        print("\n--- Conversión de", ['Longitud','Masa','Temperatura','Volumen','Tiempo'][categoria-1], "---")
        unidad_origen = pedir_unidad(unidades_disponibles, "Unidad de ORIGEN:")
        unidad_destino = pedir_unidad(unidades_disponibles, "Unidad de DESTINO:")
        
        # Pedir valor a convertir
        while True:
            try:
                valor = float(input(f"\nIngrese el valor en {unidad_origen.capitalize()}: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        # Realizar la conversión según la categoría
        if categoria == 1:
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
        elif categoria == 2:
            resultado = convertir_masa(valor, unidad_origen, unidad_destino)
        elif categoria == 3:
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
        elif categoria == 4:
            resultado = convertir_volumen(valor, unidad_origen, unidad_destino)
        elif categoria == 5:
            resultado = convertir_tiempo(valor, unidad_origen, unidad_destino)
        
        if resultado is None:
            print("Error: unidades no reconocidas. Intente de nuevo.")
        else:
            print(f"\n✅ {valor} {unidad_origen.capitalize()} = {resultado:.6f} {unidad_destino.capitalize()}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()