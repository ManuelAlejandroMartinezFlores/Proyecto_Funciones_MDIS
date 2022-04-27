'''
    Interfaz que interactua con el usuario.
    Manuel Alejandro Martínez Flores
'''

from funciones import *

# Se solicita la cardinalidad del dominio y contradominio (0 < ... < 9)
while True:
    try:
        print("Ingrese cardinalidad de dominio: (0 < X < 9)")
        X = int(input())
        assert 0 < X < 9
        print("Ingrese cardinalidad de contradominio: (0 < Y < 9)")
        Y = int(input())
        assert 0 < X < 9
        print("Desea imprimir las funciones? (0 - No / 1 - Si)")
        imprimir = int(input())
        assert -1 < imprimir < 2 
        break
    except:
        print("Ingrese valores válidos")

# Si ambos son 1, solo existe 1 de cada clase
if X == 1 and Y == 1:
    print("Sobreyectivas: ", 1)
    print("Inyectivas: ", 1)
# Si X es 1, a este elemento se le puede asignar cualqueira de Y
# entonces hay Y inyectivas
elif X == 1:
    print("Sobreyectivas: ", 0)
    print("Inyectivas: ", Y)
# Si Y es 1, todos los elementos de X tienen a ese elemento asignado
# entonces hay 1 sobreyectiva
elif Y == 1:
    print("Sobreyectivas: ", 1)
    print("Inyectivas: ", 0)
# En caso contrario, se evalua
else:   
    cnt_iny, cnt_sob = eval(X, Y, imprimir)
    print("Sobreyectivas: ", cnt_sob)
    print("Inyectivas: ", cnt_iny)
    