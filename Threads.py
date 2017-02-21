import time ##Hora de la computadora
from threading import Thread ##Thread (hilo), para evitar el error threading.Thread
import threading ##Hilos


##Metodo encargado de imprimir la cantidad de hilos que se estan ejecutando
def imprimirAdios():
    ##Sentencia que se va repetir durante toda la ejecucion del programa
    while True:
        print ("Adios\n")
        ##Duerme el metodo 1 segundos
        time.sleep(5)

def imprimirHola():
    ##Sentencia que se va repetir durante toda la ejecucion del programa
    while True:
        print ("Hola\n")
        ##Duerme el metodo 1 segundos
        time.sleep(1)




##Crea un hilo y lo inicializa
##nombre de la variable = Thread(target=funcion que desea invocar, args=(argumentos que recibe dicha funcion))
a = Thread(target=imprimirAdios, args=())
a.start()

b = Thread(target=imprimirHola, args=())
b.start()
