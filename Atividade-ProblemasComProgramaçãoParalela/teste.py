import threading

resultado = 0
def somaN(lista, i, f, nome):
    global resultado

    print(f"{nome}! resultado: {resultado}") # Primeira Volta

    resultado = sum(lista[i:f])
    
    print(f"{nome}! resultado: {resultado}") #Terceira Volta


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
meio = len(lista) // 2

th1 = threading.Thread(target=somaN, args=(lista,0, meio, "Thread 1"))
th2 = threading.Thread(target=somaN, args=(lista,meio, len(lista), "Thread 2"))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Soma Total : {resultado}")

'''
Resultado Certo
0
15
15
40
Soma : 55
'''

'''
Exemplo de Erro
0
0
15 
40 
A soma dos valores da lista é 80
'''

#Explicação do Erro
'''
def somaN(lista, i, f):
    global resultado
    global soma
    print(f"{resultado}")
    resultado = sum(lista[i:f])
    print(f"{resultado}")
    soma += resultado

    thread 1 está no controle e altera resultado para 15, em seguida chega a thread 2, 
    assume o controle e altera resultado para 40. O controle volta para a thread 1 que 
    por sua vez
'''

