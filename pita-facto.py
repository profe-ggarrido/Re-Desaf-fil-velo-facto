#CONTROL DE TERMINAL LIMPIA
import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_consola()

# ESTE DESAFIO LO CONSTRUÍ POR LA GUIA O PROCESO QUE HIZO EL PROFE
# ENTENDÍ BIEN EL ALGORITMO PERO NO SE ME OCURRIÒ OTRA FORMA

def pitatoria(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

def factorial(numero):
    #print(type(numero))
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = numero * factorial(numero-1)
        return resultado
    
def calcular(**kwargs):
    #print(kwargs) --- Chequeando typo de KWARGS
    for k,v in kwargs.items():
        if type(v) is int:

            fact = factorial(v)
            print(f"El factorial de {v} es {factorial(v)}")
        else:
            print(f"La productoria de {v} es {pitatoria(v)}")

#PROBANDO FACTORIAL Y PRODUCTORIA
# clave y valor o sea cualquier texto seguido de un valor
calcular(act = 5, prod_1 = [4, 6, 7, 4, 3] , act_2 = 6, fact_3 = 15, prod_2 = [22, 16, 57, 64, 83]) 
#calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3] , fact_2 = 6, fact_3 = 15, prod_2 = [22, 16, 57, 64, 83]) 
print("")