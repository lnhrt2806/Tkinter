##Se llaman las bibliotecas necesarias para el funcionamiento del programa
from tkinter import * ##Interfaz
from tkinter import messagebox
import time ##Hora de la computadora
from threading import Thread ##Thread (hilo), para evitar threading.Thread
import random ##Metodos para generar numeros aleatorios
import threading ##Hilos
import os ##Funciones del sistema operativo

       
##Variable global
flag_cuadro=True

##Metodo para cargar imagenes
def cargarImagen(nombre):
    ruta = os.path.join('Imagenes',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen


##Creamos la ventana principal
##Solo la ventana principal o inicial es de tipo Tk()
ventana_principal = Tk()
ventana_principal.title("Taller tKinter")##Escribe el titulo de la ventana en la parte superior
ventana_principal.minsize(800,700)##Tamaño mínimo
ventana_principal.resizable(width=NO,height=NO)##Indica que la ventana no puede tener modificaciones en su tamaño.


#Crear canvas
#canvas = Canvas(WidgetContenedor, Ancho, Alto, bg=colorDeFondo)
contenedor_principal = Canvas(ventana_principal , width= 800, height = 700, bg = "#000000")
contenedor_principal.place(x=0,y=0)##Coloca el contenedor en las coordenadas indicadas dentro de la ventana principal

##Fondo de la pantalla
imagenFondo = cargarImagen("Fondo.gif")#Le asigna a la variable la imagen
LabelFondo=Label(contenedor_principal, image=imagenFondo, bg = "#FFFFFF")#La imagen siempre debe ir en otro contenedor
LabelFondo.place (x=0, y=0)

#crea el entry
#entrada = Entry(widgetContenedor, width)
entrada = Entry(contenedor_principal, width=30, bg = "#FFFFFF")
entrada.place(x=103,y=500)


##Metodo para el boton imprimir
def mostrar():
    messagebox.showinfo("Mensaje leido en el entry",str(entrada.get()))#Muestra un texto en una ventana emergente
    print ("Mensaje leido:"+entrada.get())#Muestra lo solicitado en consola


#Boton imprimir
#botonImprimir = Button(widgetContenedor, text=contenido, command=funcionLlamada, bg = colorDeFondo, fg = colorDeLetra)
botonImprimir = Button(contenedor_principal, text="Imprimir",command=mostrar, bg = "#BBBBFF", fg = "#000000")
botonImprimir.place(x=160,y=550)

def VentanaMondrian(): 
    ##Se desvanece la ventana principal, pero no se destruye
    ventana_principal.withdraw()
    ##Creamos otra ventana
    ventanaMondrian = Toplevel()#Todas las nuevas ventanas que se generen despues de la principal, serán tipo TopLevel
    ventanaMondrian.title("Taller tKinter")
    ventanaMondrian.minsize(600,600)
    ventanaMondrian.resizable(width=NO,height=NO)

    ##Se coloca un contenedor
    fondo = Canvas(ventanaMondrian , width=600,height=600, bg = "#000000")
    fondo.place(x=0,y=0)

    ##Metodo que retorna el valor hexadecimal de un color ramdom
    def color():
        lista_colores=["#42f456","#41f4cd","#b541f4","#f441b5","#88912a","#e4f902"]
        return lista_colores[random.randrange(0,5)]

    ##Metodo que genera la animacion del cuadro moviendose
    def cuadro():
        ##Coordenadas en cada movimiento del cuadro
        x_cuadro=0
        y_cuadro=0
        cuadro = Canvas(fondo, width=random.randrange(20, 30), height=random.randrange(20, 30), bg=color())
        ##Se hace referencia a la bandera flag_cuadro
        while flag_cuadro:#variable que permite el funcionamiento del thread
            try:
                ##Mueve el cuadro en cada iteracion
                cuadro.place(x=x_cuadro,y=y_cuadro)
                if(x_cuadro==600):
                    x_cuadro=0
                    y_cuadro+=30
                elif(y_cuadro==540):
                    y_cuadro=0
                else:
                    x_cuadro+=30
                time.sleep(0.05)
            except Exception as errtxt:
                print ("Error en hilo")

    ##Metodo del boton botonIniciarHilo
    def ver_cuadro():
        global flag_cuadro
        flag_cuadro=True
        ##Crea un hilo
        a = Thread(target=cuadro, args=())
       
        a.start()

    ##Metodo que destruye a los hilos
    def kill_cuadro():
        global flag_cuadro
        flag_cuadro=False

    ##Metodo para el boton regresar
    def regresar():
        kill_cuadro()
        ventanaMondrian.destroy()
        ##Reaparece la ventana principal
        ventana_principal.deiconify()
       
    botonIniciarHilo = Button(fondo, text="Cuadro",command=ver_cuadro, fg = "#000000", bg = "#0fa0aa")
    botonIniciarHilo.place(x=100,y=575)

    botonDetenerHilos = Button(fondo, text="Quitar Cuadro",command=kill_cuadro, fg = "#000000", bg = "#0fa0aa")
    botonDetenerHilos.place(x=200,y=575)

    botonVolver = Button(fondo, text="Regresar",command=regresar, fg = "#000000", bg = "#0fa0aa")
    botonVolver.place(x=540,y=575)

    ventanaMondrian.mainloop()
    
##Fondo de boton Movimiento
imagenMondrianEfect = cargarImagen("Boton.gif")

#Boton Ventana Hilos
#botonVentanaHilos = Button(widgetContenedor, text=contenido, command=funcionLlamada, bg = colorDeFondo, fg = colorDeLetra)
botonVentanaMondrian = Button(contenedor_principal, image=imagenMondrianEfect ,command=VentanaMondrian, bg = "#000000", fg = "#ffffff", width=300, height=300)
botonVentanaMondrian.place(x=45,y=45)

##Hace visibles los elementos
ventana_principal.mainloop()
