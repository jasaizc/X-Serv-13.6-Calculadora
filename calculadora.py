"""
Script que nos crea una calculadora

Para ejecutarlo, desde la shell:
 $ python calculadora.py funcion operador1 operador2

"""
import os
import random
import sys

funciones = ['suma','resta','multiplicacion','division']
i = 0;

def suma(parametro1, parametro2):
    print (parametro1 + parametro2)
def resta(parametro1, parametro2):
    print (parametro1 - parametro2)
def multi(parametro1, parametro2):
    print (parametro1 * parametro2)
def div(parametro1, parametro2):
    try:
        print (float(parametro1) / float(parametro2)) 
    except ZeroDivisionError as e: 
        print "No se puede dividir entre 0"

if len(sys.argv) != 4:
    print sys.argv
    sys.exit("Usage: $ python calculadora.py funcion operador1 operador2")

for funcion in funciones:
    if(funcion == sys.argv[1]):
        print sys.argv[1] + ' de ' + sys.argv[2] + ' y ' +  sys.argv[3]
        if (i == 0):
            suma(int(sys.argv[2]), int(sys.argv[3]))
        elif (i == 1):
            resta(int(sys.argv[2]), int(sys.argv[3]))
        elif (i == 2):
            multi(int(sys.argv[2]), int(sys.argv[3]))
        elif (i == 3):
            div(int(sys.argv[2]), int(sys.argv[3]))
    else:
        i = i + 1

if (i > 3):
    sys.exit("Las Operaciones Validas son: suma, resta, multiplicacion, division")

    
