#Essa é uma implentação do algoritimo que Soma os Elementos em um array de numeros (atividade passada).
#Tetamos mostrar o passo a passo da execução de cada thread, onde cada uma vai ficar com uma parte do array para ser somado.

import threading
from time import sleep

def funcao_helper(array, inicio, fim, id_thread, resultado):#
    print(f"Thread {id_thread} iniciada. Somando elementos de {inicio} a {fim - 1}.")
    sleep(3)
    soma_parcial = sum(array[inicio:fim])
    print(f"Thread {id_thread}: soma parcial = {soma_parcial}")
    resultado.append(soma_parcial)
    print(f"Thread {id_thread} finalizada.")
    sleep(3)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = []

#Divisão do array em partes para cada thread
num_threads = int(input("Digite o número de threads: "))#
print(f"Array de números: {numeros}\n")

tamanho_parte = len(numeros) // num_threads
threads = [] #

#Criando e iniciando as threads
for i in range(num_threads):
    inicio = i * tamanho_parte
    fim = (i + 1) * tamanho_parte if i != num_threads - 1 else len(numeros)
    #if(i!=num_threads-1):
        #fim = (i+1) * tamanho_parte
    #else:
        #fim = len(numeros) 
    print(f"Criando a Thread {i + 1} para somar os elementos na posição de {inicio} a {fim - 1}.")
    thread = threading.Thread(target=funcao_helper, args=(numeros, inicio, fim, i + 1, resultado))
    threads.append(thread)
    thread.start()
print()

#Garantindo que todas as threads terminem antes de finalizar o main
for thread in threads:
    thread.join()

# Calculando a soma total após as threads concluírem
soma_total = sum(resultado)
print()

print(f"Soma total dos elementos do array: {soma_total}")
print("Finalizando o método main.")
