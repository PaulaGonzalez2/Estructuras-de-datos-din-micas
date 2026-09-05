import tkinter as tk

ventana = tk.Tk()
ventana.title("Cola de impresión")
ventana.geometry("800x600")
ventana.attributes("-alpha",1)

### Marco 1
frame1=tk.Frame(ventana)
frame1.configure(width=790, height=175,bg="lemon chiffon",bd=5)
frame1.place(x=5,y=0)

frame2=tk.Frame(frame1)
frame2.configure(width=500, height=175,bg="white",bd=5)
frame2.place(x=5,y=30)

etiqueta=tk.Label(frame2,text="Nombre del documento:",font=("arial",10))
etiqueta.place(x= 0, y =0)
entrada1=tk.Entry(frame2)
entrada1.configure(fg="black",bg="white",font=("arial",10))
entrada1.place(x= 200, y =0)

etiqueta2=tk.Label(frame2,text="Numero de páginas:",font=("arial",10))
etiqueta2.place(x= 0, y =35)
entrada2=tk.Entry(frame2)
entrada2.configure(fg="black",bg="white",font=("arial",10))
entrada2.place(x= 200, y =35)

etiqueta3=tk.Label(frame2,text="Tiempo por página (seg):",font=("arial",10))
etiqueta3.place(x= 0, y =75)
entrada3=tk.Entry(frame2)
entrada3.configure(fg="black",bg="white",font=("arial",10))
entrada3.place(x= 200, y =75)

boton=tk.Button(frame2,text="AGREGAR A LA COLA")
boton.place(x= 200, y =100)


"""













"""
###Marco 2

frame2=tk.Frame(ventana)
frame2.configure(width=790, height=150,bg="bisque",bd=5)
frame2.place(x=5,y=175)
"""
etiqueta=tk.Label(frame2,text="COLA DE IMPRESIÓN",font=("arial",15))
etiqueta.grid(row=0, column=0)
frame4=tk.Frame(frame2)
frame4.configure(width=650, height=100,bg="white",bd=5)
frame4.place(x=50,y=220)

"""
### Marco 3
frame3=tk.Frame(ventana)
frame3.configure(width=790, height=100,bg="old lace",bd=5)
frame3.place(x=5,y=325)
"""
etiqueta=tk.Label(frame3,text="ESTADO DE IMPRESIÓN",font=("arial",15))
etiqueta.grid(row=10, column=0)

boton2=tk.Button(frame3,text="INICIAR IMPRESION")
boton2.grid(row=11, column=0)
boton3=tk.Button(frame3,text="DETENER IMPRESION")
boton3.grid(row=11, column=1)
"""
frame5=tk.Frame(ventana)
frame5.configure(width=790, height=175,bg="navajo white",bd=5)
frame5.place(x=5,y=425)

ventana.mainloop()