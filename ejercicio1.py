import tkinter as tk

ventana = tk.Tk()
ventana.title("Cola de impresión")
ventana.geometry("800x600")
ventana.attributes("-alpha",1)

### Marco 1
frame1=tk.Frame(ventana)
frame1.configure(width=790, height=175,bg="lemon chiffon",bd=5)
frame1.place(x=5,y=0)
etiqueta0=tk.Label(frame1,text="SIMULADOR DE IMPRESORA",font=("arial",15))
etiqueta0.place(x= 200, y =0)

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


###Marco 2

frame3=tk.Frame(ventana)
frame3.configure(width=790, height=150,bg="bisque",bd=5)
frame3.place(x=5,y=175)

etiqueta4=tk.Label(frame3,text="COLA DE IMPRESIÓN",font=("arial",15))
etiqueta4.place(x= 0, y =0)

frame4=tk.Frame(frame3)
frame4.configure(width=650, height=100,bg="white",bd=5)
frame4.place(x=5,y=35)


### Marco 3
frame5=tk.Frame(ventana)
frame5.configure(width=790, height=100,bg="old lace",bd=5)
frame5.place(x=5,y=325)

etiqueta5=tk.Label(frame5,text="ESTADO DE IMPRESIÓN",font=("arial",15))
etiqueta5.place(x= 0, y =0)

boton2=tk.Button(frame5,text="INICIAR IMPRESION")
boton2.place(x= 50, y =60)
boton3=tk.Button(frame5,text="DETENER IMPRESION")
boton3.place(x= 200, y =60)

##MARCO 4
frame6=tk.Frame(ventana)
frame6.configure(width=790, height=175,bg="navajo white",bd=5)
frame6.place(x=5,y=425)

etiqueta6=tk.Label(frame6,text="REGISTRO DE EVENTOS",font=("arial",15))
etiqueta6.place(x= 0, y =0)

frame7=tk.Frame(frame6)
frame7.configure(width=765, height=120,bg="white",bd=5)
frame7.place(x=10,y=30)
ventana.mainloop()