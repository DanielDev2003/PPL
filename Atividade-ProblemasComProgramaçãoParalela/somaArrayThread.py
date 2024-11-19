#Soma de Elementos em um array de numeros

import threading
import time
def soma_parcial(lista, inicio, fim, resultado, delay):
    time.sleep(delay)#delay usado para simular os erros
    parcial = sum(lista[inicio:fim])
    resultado.append(parcial)  

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = []

fim = len(numeros)
meio = fim // 2

thread1 = threading.Thread(target=soma_parcial, args=(numeros, 0, meio, resultado, 0))

thread2 = threading.Thread(target=soma_parcial, args=(numeros, meio, fim, resultado, 0))

thread1.start()
thread2.start()

print(numeros[0:meio])
print(numeros[meio:fim])
print(resultado)
soma_total = sum(resultado)

print(soma_total)

#Erros
# 1 - O array resultado pode conter apenas um valor parcial, levando a uma soma incorreta.
# 2 - O array resultado pode estar vazio