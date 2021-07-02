import csv
from datetime import datetime
from math import sqrt, pi, cos, log10

class Solution:
    
    def __init__(self, filename):
        # id,first_name,last_name,dateOfBirth,interests,latitude,longitude
        filename = "data.cvs"
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
    def Prob1(self, id1, id2):
      la = Solution().students[id1][3] * pi / 180
      lo = Solution().students[id1][4] * pi / 180
      d = 6371.009*sqrt(abs(la-lo)^2 + (abs(la-lo)*cos(sum(la-lo)/2))^2)
      return d

    # Compatibilidad entre estudiantes
    def ejercicio2(self, id1, id2):
        AgeD = abs(id1[4]-id2[4])
        if AgeD <=1 :
            return 1
        if AgeD >= 1:
            return (AgeD)^(-1)
        LID1 = list(id1[3])
        LID2 = list(id2[3])
        COIN = len(LID1 & LID2)
        CP = ((log10*"ejercicio1"))^(-1) + AgeD + COIN

        return CP


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