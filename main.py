import random
import math

def obtener_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        datos = []
        for i in file.readlines():
            i = i.strip()
            i = float(i)
            datos.append(i)
    return datos

def desviacion_estandar(data_list):
    var = 0
    for i in data_list:
        var += float(i)
    promedio = var/len(data_list)

    var = 0
    for i in data_list:
        var += (promedio - float(i)) ** 2
    var = var/(len(data_list) - 1)

    desviacion_estandar = round(math.sqrt(var), 4)

    error_estandar = round(desviacion_estandar/(math.sqrt(len(data_list) - 1)), 4)

    return f'La desviacion estandar es: {desviacion_estandar}\nEl error estandar es: {error_estandar}'

def calcular_desv_para(data_list, n):
    var = []
    for i in range(n):
        var.append(data_list[random.randint(0, len(datos) - 1)])
    
    return desviacion_estandar(var)

if __name__ == '__main__':

    '''
    datos = obtener_datos('toma_muestras.txt')
    
    print(f'Para n = 2:\n{calcular_desv_para(datos, 2)}\n------------------------')
    print(f'Para n = 2:\n{calcular_desv_para(datos, 4)}\n------------------------')
    print(f'Para n = 2:\n{calcular_desv_para(datos, 6)}\n------------------------')
    '''

    datos = obtener_datos('muestra_arroces.txt')
    
    print(desviacion_estandar(datos))
