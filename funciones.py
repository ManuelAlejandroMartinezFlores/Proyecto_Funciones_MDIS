'''
    Implementaciones de funciones utiles para el proyecto
    Manuel Alejandro Martínez Flores
'''

import numpy as np


def gen_fun(n, X, Y):
    '''
        Genera un string donde cada posición corresponde a un elemento del dominio
        y el número en esa posición a uno del contradominio
    '''
    s = np.base_repr(n, base=Y)
    return "0" * (X - len(s)) + s


def eval_mat(fun, X, Y):
    '''
        Genera una matriz a partir de la función para evaluar si es inyectiva y/o sobreyectiva
    '''
    m = np.zeros((X, Y))
    for i, j in enumerate([int(x) for x in fun]):
        m[i, j] = 1
    m = m.sum(axis=0)
    # Si algún elemento del contradominio se repite, no es inyectiva
    iny = m.max() == 1
    # Si algún elemento del contradominio no aparece, no es sobreyectiva
    sob = m.min() == 1
    return (iny, sob)


def eval_dict(fun, X, Y):
    '''
        Evalua si la función es sobreyectiva y/o inyectiva utilizando un diccionario
    '''
    d = {}
    iny = True
    total_y = Y
    
    for y in fun:
        # Si algún elemento del contradominio se repite, no es inyectiva
        if y in d:
            # Si hay mas elementos en el contradominio que en el dominio, no puede ser sobre
            if Y > X :  
                return (False, False)
            iny = False
        else:
            d[y] = 0
            total_y = total_y - 1

            
    return (iny, total_y == 0)



def eval(X, Y, imprimir, eval_fun = eval_dict):
    '''
        Cuenta las funciones sobreyectivas y/o inyectivas para dominio X y contradominio Y
    '''
    cnt_iny = 0
    cnt_sob = 0

    for n in range(Y**X):
        fun = gen_fun(n, X, Y) 
        iny, sob = eval_fun(fun, X, Y)
        cnt_iny += iny
        cnt_sob += sob
        if imprimir :
            if sob or iny:
                txt = ""
                if sob : txt += "- sobreyectiva "
                if iny : txt += "- inyectiva "
                print(fun, txt)
            
    if imprimir : print("*Nota: las funciones están representadas como una cadena donde la posición" +
                        " representa un elemento del dominio y el número en ella un elemento del contradominio*")
    return cnt_iny, cnt_sob