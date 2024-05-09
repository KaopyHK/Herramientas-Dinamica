import random
import math


class Dynamics:
    def __init__(self, file_name: str):
        self._obtener_datos(file_name)

    def _obtener_datos(self, nombre_archivo):

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
                # datos[i] = ','.join(datos[i])
        # self._escribir_datos(datos)
        vel_text, frz_text = self._propio_lab2(datos)
        self._escribir_datos('Lab2\Velocidad', vel_text)
        self._escribir_datos('Lab2\Fuerza', frz_text)

    @staticmethod
    def _escribir_datos(nombre_archivo, datos):
        with open(nombre_archivo + '_procesado.csv', 'wt', encoding='UTF8') as file:
            for linea in datos:

                file.write(linea + '\n')

    @staticmethod
    def _propio_lab2(datos):

        fuerza_index, velocidad_index = (0, 0)
        for i in range(len(datos[0])):
            if fuerza_index and velocidad_index:
                break
            if '(N)' in datos[0][i]:
                fuerza_index = i
            elif '(m/s)' in datos[0][i]:
                velocidad_index = i

        fuerza_texto = []
        velocidad_texto = []
        for linea in datos:
            var = [linea[0]]
            for i in range(fuerza_index, len(linea) + 1, 8):
                var.append(linea[i])
            fuerza_texto.append(var)

        for linea in datos:
            var = [linea[0]]
            for i in range(velocidad_index, len(linea) + 1, 8):
                var.append(linea[i])
            velocidad_texto.append(var)

        for i in range(len(velocidad_texto)):
            velocidad_texto[i] = ','.join(velocidad_texto[i])

        for i in range(len(fuerza_texto)):
            fuerza_texto[i] = ','.join(fuerza_texto[i])

        return velocidad_texto, fuerza_texto




if __name__ == '__main__':

    texto = Dynamics('Lab2\datos_subida')
