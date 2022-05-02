'''
    Test de rendimiento de implementaciones
    Manuel Alejandro Martínez Flores
'''

import time
from funciones import *

def test_eval(eval_fun):
    '''
        Evalua el tiempo necesario para utilizar una implementación
    '''
    t = time.time()
    for X in range(2, 9):
        for Y in range(2, 9):
            eval(X, Y, False ,eval_fun)
    return time.time() - t

print("Mat")
print(test_eval(eval_mat))
print("Dict")
print(test_eval(eval_dict))