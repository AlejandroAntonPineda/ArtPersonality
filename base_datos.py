import tkinter as tk
import sqlite3


def guardar_palabras():
    palabras = [entrada1.get(), entrada2.get(), entrada3.get(), entrada4.get(), entrada5.get()]

    # Conexión a la base de datos
    conexion = sqlite3.connect('basedatos.db')
    cursor = conexion.cursor()

    # Crear la tabla "palabras" si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS palabras
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       palabra TEXT)''')

    # Eliminar las palabras anteriores en la tabla
    cursor.execute("DELETE FROM palabras")

    # Insertar las últimas 5 palabras en la tabla "palabras"
    for palabra in palabras:
        cursor.execute("INSERT INTO palabras (palabra) VALUES (?)", (palabra,))

    # Guardar cambios y cerrar conexión
    conexion.commit()
    conexion.close()
    ventana.destroy()

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
boton = tk.Button(ventana, text="Aceptar", command=guardar_palabras)
boton.pack()
ventana.mainloop()


def mostrar_ventana1():
    ventana1 = tk.Toplevel()
    ventana1.title("Tus palabras")
    etiqueta1 = tk.Label(ventana1, text="Estas son tus palabras:")
    etiqueta1.pack()

    # Conexión a la base de datos
    conexion = sqlite3.connect('basedatos.db')
    cursor = conexion.cursor()

    # Consulta para recuperar las palabras
    cursor.execute("SELECT palabra FROM palabras")
    palabras = cursor.fetchall()

    for palabra in palabras:
        etiqueta = tk.Label(ventana1, text=palabra[0])
        etiqueta.pack()

    # Cerrar conexión
    conexion.close()


def mostrar_ventana2():
    ventana2 = tk.Toplevel()
    ventana2.title("Palabras nuevas")
    frase_inicio = "Si fueras 5 palabras, cuáles serías?:"
    etiqueta_frase = tk.Label(ventana2, text=frase_inicio)
    etiqueta_frase.pack()

    entrada1 = tk.Entry(ventana2)
    entrada1.pack()
    entrada2 = tk.Entry(ventana2)
    entrada2.pack()
    entrada3 = tk.Entry(ventana2)
    entrada3.pack()
    entrada4 = tk.Entry(ventana2)
    entrada4.pack()
    entrada5 = tk.Entry(ventana2)
    entrada5.pack()

    def guardar_palabras_nuevas():
        palabras = [entrada1.get(), entrada2.get(), entrada3.get(), entrada4.get(), entrada5.get()]

        # Conexión a la base de datos
        conexion = sqlite3.connect('basedatos.db')
        cursor = conexion.cursor()

        # Crear la tabla "palabras" si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS palabras
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             palabra TEXT)''')

        # Eliminar las palabras anteriores en la tabla
        cursor.execute("DELETE FROM palabras")

        # Insertar las últimas 5 palabras en la tabla "palabras"
        for palabra in palabras:
            cursor.execute("INSERT INTO palabras (palabra) VALUES (?)", (palabra,))

        # Guardar cambios y cerrar conexión
        conexion.commit()
        conexion.close()


    boton = tk.Button(ventana2, text="Aceptar", command=guardar_palabras_nuevas)
    boton.pack()



ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")

boton_ventana1 = tk.Button(ventana_principal, text="Tus palabras", command=mostrar_ventana1)
boton_ventana1.pack()

boton_ventana2 = tk.Button(ventana_principal, text="Palabras nuevas", command=mostrar_ventana2)
boton_ventana2.pack()

ventana_principal.mainloop()