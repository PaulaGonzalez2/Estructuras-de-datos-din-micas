import tkinter as tk
from collections import deque
from Documento import Documento


# ---------------------------------------
# VARIABLES DEL PROGRAMA
# ---------------------------------------

cola_impresion = deque()

documento_actual = None
imprimiendo = False

TIEMPO_POR_PAGINA = 1000   # 1000 milisegundos = 1 segundo


# ---------------------------------------
# FUNCIONES
# ---------------------------------------

def escribir_registro(mensaje):
    registro.insert(tk.END, mensaje + "\n")
    registro.see(tk.END)


def mostrar_cola():
    lista_cola.delete(0, tk.END)

    if documento_actual is not None:
        texto = "Imprimiendo: " + documento_actual.nombre
        texto += " - Página " + str(documento_actual.pagina_actual)
        texto += " de " + str(documento_actual.numero_paginas)
        lista_cola.insert(tk.END, texto)

    contador = 1

    for documento in cola_impresion:
        texto = str(contador) + ". "
        texto += documento.nombre
        texto += " - " + str(documento.numero_paginas) + " páginas"

        lista_cola.insert(tk.END, texto)
        contador += 1


def agregar_documento():
    nombre = nombre_var.get()
    paginas = paginas_var.get()

    if nombre == "" or paginas == "":
        estado_var.set("Debe escribir el nombre y el número de páginas")
        return

    if not paginas.isdigit():
        estado_var.set("El número de páginas debe ser un número entero")
        return

    paginas = int(paginas)

    if paginas <= 0:
        estado_var.set("El número de páginas debe ser mayor que cero")
        return

    nuevo_documento = Documento(nombre, paginas)

    # append agrega al final de la cola.
    cola_impresion.append(nuevo_documento)

    escribir_registro(
        "Se agregó el documento: " + nombre +
        " con " + str(paginas) + " páginas."
    )

    nombre_var.set("")
    paginas_var.set("")

    mostrar_cola()

    if not imprimiendo:
        estado_var.set(
            "Documento agregado. Hay " +
            str(len(cola_impresion)) +
            " documento(s) en cola."
        )


def iniciar_impresion():
    global imprimiendo

    if imprimiendo:
        estado_var.set("La impresora ya está funcionando")
        return

    if documento_actual is None and len(cola_impresion) == 0:
        estado_var.set("No hay documentos en la cola")
        escribir_registro("No hay documentos para imprimir.")
        return

    imprimiendo = True
    escribir_registro("La impresión fue iniciada.")
    imprimir_siguiente_pagina()


def detener_impresion():
    global imprimiendo

    if imprimiendo:
        imprimiendo = False
        estado_var.set("Impresión detenida")
        escribir_registro("La impresión fue detenida.")
    else:
        estado_var.set("No hay impresión activa")


def imprimir_siguiente_pagina():
    global documento_actual
    global imprimiendo

    if not imprimiendo:
        return

    # Si no hay documento imprimiéndose, se saca el primero de la cola.
    if documento_actual is None:

        if len(cola_impresion) == 0:
            imprimiendo = False
            estado_var.set("No hay más documentos en cola")
            escribir_registro("Todos los documentos fueron impresos.")
            mostrar_cola()
            return

        # popleft saca el primer documento de la cola: FIFO.
        documento_actual = cola_impresion.popleft()

        escribir_registro(
            "Comenzó la impresión de: " +
            documento_actual.nombre
        )

    # Se imprime una página.
    documento_actual.pagina_actual += 1

    estado_var.set(
        "Imprimiendo " + documento_actual.nombre +
        " - Página " + str(documento_actual.pagina_actual) +
        " de " + str(documento_actual.numero_paginas)
    )

    escribir_registro(
        documento_actual.nombre +
        ": página " + str(documento_actual.pagina_actual) +
        " de " + str(documento_actual.numero_paginas)
    )

    mostrar_cola()

    # Si ya se imprimieron todas las páginas, el documento termina.
    if documento_actual.pagina_actual == documento_actual.numero_paginas:

        escribir_registro(
            "Documento terminado: " +
            documento_actual.nombre
        )

        documento_actual = None

    # after espera un segundo sin congelar la ventana.
    ventana.after(TIEMPO_POR_PAGINA, imprimir_siguiente_pagina)


# ---------------------------------------
# VENTANA PRINCIPAL
# ---------------------------------------

ventana = tk.Tk()
ventana.title("Cola de impresión")
ventana.geometry("800x650")


# Variables para las cajas de texto
nombre_var = tk.StringVar()
paginas_var = tk.StringVar()
estado_var = tk.StringVar()

estado_var.set("No hay documentos en cola")


# ---------------------------------------
# MARCO 1: INGRESAR DOCUMENTO
# ---------------------------------------

frame1 = tk.Frame(ventana, bg="lemon chiffon", bd=5)
frame1.place(x=5, y=5, width=790, height=175)

etiqueta0 = tk.Label(frame1, text="SIMULADOR DE IMPRESORA", font=("Arial", 15, "bold"), bg="lemon chiffon")
etiqueta0.place(x=220, y=5)

etiqueta1 = tk.Label(frame1, text="Nombre del documento:",font=("Arial", 10),bg="lemon chiffon")
etiqueta1.place(x=40, y=45)

entrada1 = tk.Entry(frame1, textvariable=nombre_var,font=("Arial", 10),width=30)
entrada1.place(x=220, y=45)

etiqueta2 = tk.Label(frame1,text="Número de páginas:",font=("Arial", 10),bg="lemon chiffon")
etiqueta2.place(x=40, y=80)

entrada2 = tk.Entry(frame1, textvariable=paginas_var,font=("Arial", 10),width=30)
entrada2.place(x=220, y=80)

etiqueta3 = tk.Label(frame1,text="Tiempo por página: 1 segundo",font=("Arial", 10),bg="lemon chiffon")
etiqueta3.place(x=40, y=115)

boton1 = tk.Button(frame1,text="AGREGAR A LA COLA", command=agregar_documento)
boton1.place(x=500, y=75)


# ---------------------------------------
# MARCO 2: COLA
# ---------------------------------------

frame2 = tk.Frame(ventana, bg="bisque", bd=5)
frame2.place(x=5, y=185, width=790, height=150)

etiqueta4 = tk.Label(frame2,text="COLA DE IMPRESIÓN",font=("Arial", 15, "bold"),bg="bisque")
etiqueta4.place(x=260, y=5)

lista_cola = tk.Listbox(frame2,font=("Arial", 10))
lista_cola.place(x=30, y=40, width=720, height=90)


# ---------------------------------------
# MARCO 3: ESTADO Y BOTONES
# ---------------------------------------

frame3 = tk.Frame(ventana, bg="old lace", bd=5)
frame3.place(x=5, y=345, width=790, height=120)

etiqueta5 = tk.Label(frame3,text="ESTADO DE IMPRESIÓN",font=("Arial", 15, "bold"),bg="old lace")
etiqueta5.place(x=250, y=5)

estado = tk.Label(frame3,textvariable=estado_var,font=("Arial", 11),bg="old lace",fg="blue")
estado.place(x=230, y=40)

boton2 = tk.Button(frame3,text="INICIAR IMPRESIÓN",command=iniciar_impresion)
boton2.place(x=180, y=75)

boton3 = tk.Button(frame3,text="DETENER IMPRESIÓN", command=detener_impresion)
boton3.place(x=390, y=75)


# ---------------------------------------
# MARCO 4: REGISTRO
# ---------------------------------------

frame4 = tk.Frame(ventana, bg="navajo white", bd=5)
frame4.place(x=5, y=475, width=790, height=165)

etiqueta6 = tk.Label(frame4,text="REGISTRO DE EVENTOS",font=("Arial", 15, "bold"),bg="navajo white")
etiqueta6.place(x=245, y=5)

registro = tk.Text(frame4,font=("Arial", 10))
registro.place(x=15, y=35, width=750, height=110)


ventana.mainloop()