import threading
from time import sleep


class MeuThread(threading.Thread):
    def __init__(self, nome, idThread):
        threading.Thread.__init__(self)
        self.nome = nome
        self.idThread = idThread
    
    def run(self):
        sleep(3)
        for i in range(self.idThread):
            print(f"{self.nome}: {self.idThread}")    
            sleep(self.idThread)
            

num_threads = input()
threads = []

# Criando e iniciando as threads
for i in range(int(num_threads)):
    thread = MeuThread(f"Thread: {i+1}", i+1)
    status = thread
    if(not status): #Caso n seja criado a thread o programa da erro e encerra
        print("erro")
        exit(0)
    threads.append(thread)
    print(f"Criando a Thread: {i+1}")

for thread in threads:
    thread.start()

# Garantindo que todas as threads terminem antes de finalizar o main

for thread in threads:
    thread.join()

print("Finalizando o método main")
