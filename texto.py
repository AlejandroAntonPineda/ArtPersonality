import tkinter as tk


def obtener_palabras():
    primera_palabra = entrada1.get()
    segunda_palabra = entrada2.get()
    tercera_palabra = entrada3.get()
    cuarta_palabra = entrada4.get()
    quinta_palabra = entrada5.get()

    print("Palabras ingresadas:")
    print(primera_palabra)
    print(segunda_palabra)
    print(tercera_palabra)
    print(cuarta_palabra)
    print(quinta_palabra)


ventana = tk.Tk()
ventana.title("5 Palabras")
frase_inicio = "Si fueras 5 palabras, cuáles serías?:"
etiqueta_frase = tk.Label(ventana, text=frase_inicio)
etiqueta_frase.pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()
entrada3 = tk.Entry(ventana)
entrada3.pack()
entrada4 = tk.Entry(ventana)
entrada4.pack()
entrada5 = tk.Entry(ventana)
entrada5.pack()
boton = tk.Button(ventana, text="Aceptar", command=obtener_palabras)
boton.pack()
ventana.mainloop()





