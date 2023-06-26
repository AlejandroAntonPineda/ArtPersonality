import tkinter as tk


def mostrar_ventana1():
    ventana1 = tk.Toplevel()
    ventana1.title("Ventana 1")
    etiqueta1 = tk.Label(ventana1, text="Esta es la ventana 1")
    etiqueta1.pack()

def mostrar_ventana2():
    ventana2 = tk.Toplevel()
    ventana2.title("Ventana 2")
    etiqueta2 = tk.Label(ventana2, text="Esta es la ventana 2")
    etiqueta2.pack()

ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")

boton_ventana1 = tk.Button(ventana_principal, text="Mostrar Ventana 1", command=mostrar_ventana1)
boton_ventana1.pack()

boton_ventana2 = tk.Button(ventana_principal, text="Mostrar Ventana 2", command=mostrar_ventana2)
boton_ventana2.pack()

ventana_principal.mainloop()