import csv
from datetime import datetime
from math import sqrt, pi, cos, log10



class Solution:
    
    def __init__(self, filename):
        # id,first_name,last_name,dateOfBirth,interests,latitude,longitude
        self.students = []
        with open(filename) as file:
            reader = csv.reader(file, delimiter=',', skipinitialspace=True)
            i = 0
            for line in reader:
                self.students.append(line[1:])
                # Se convierten los tipos de datos correspondientes
                self.students[i][2] = datetime.strptime(self.students[i][2], '%Y-%m-%d')
                self.students[i][3] = float(self.students[i][3])
                self.students[i][4] = float(self.students[i][4])
                for j in range(5, 11):
                    self.students[i][j] = bool(int(self.students[i][j]))

                i += 1

                

    # Distancia entre estudiantes
    def ejercicio1(self, id1, id2):
        # Escribe tu solucion aqui

        return #tu resultado


    # Compatibilidad entre estudiantes
    def ejercicio2(self, id1, id2):
        # Escribe tu solucion aqui

        return #tu resultado

    # Estudiantes mas cercanos
    def ejercicio3(self, id, n):
        # Escribe tu solucion aqui

        return #tu resultado


    # Estudiantes mas cercanos
    def ejercicio4(self, id, n):
        # Escribe tu solucion aqui

        return #tu resultado


    # Estudiantes mas compatibles
    def ejercicio5(self, id, n):
        # Escribe tu solucion aqui

        return #tu resultado


    # Estudiantes menos compatibles
    def ejercicio6(self, id, n):
        # Escribe tu solucion aqui

        return #tu resultado



