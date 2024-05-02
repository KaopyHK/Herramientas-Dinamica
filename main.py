import random
import math


class Dynamics:
    def __init__(self, file_name: str):
        self._obtener_datos(file_name)

    @staticmethod
    def _obtener_datos(nombre_archivo):

        with open(nombre_archivo + '.csv', 'rt', encoding='UTF8') as file:
            datos = file.readlines()
            for i in range(len(datos)):
                datos[i] = datos[i].strip()
                datos[i] = datos[i].split(';')
                if i == 0:
                    for j in range(len(datos[i])):
                        datos[i][j] = datos[i][j].strip()
                else:
                    for j in range(len(datos[i])):
                        datos[i][j] = datos[i][j].replace(',', '.')
                        if not datos[i][j]:
                            datos[i][j] = '-'
                datos[i] = ','.join(datos[i])

        with open(nombre_archivo + '_procesado.csv', 'wt', encoding='UTF8') as file:
            for linea in datos:

                file.write(linea + '\n')


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

    texto = Dynamics('Lab2\datos_bajada')
