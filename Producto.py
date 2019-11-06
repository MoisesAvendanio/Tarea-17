# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np

def Producto(arreglo):
    return np.prod(arreglo)  #Operación Básica

def ProductoDos(arreglo):
    valor=1
    for i in range (len(arreglo)):
        valor=valor*arreglo[i]  #Operación Básica
    return valor

a=[4,5,6,7,8,9]
print(Producto(a))
print(ProductoDos(a))
