import tkinter as tk

ventana = tk.Tk()
ventana.title("Cola de impresión")
ventana.geometry("800x600")
ventana.attributes("-alpha",1)

frame1=tk.Frame(ventana)
frame1.configure(width=200, height=300,bg="linen",bd=5)
frame1.place(x=100,y=80)

etiqueta=tk.Label(frame1,text="Nombre del documento:",font=("arial",10))
etiqueta.grid(row=0, column=0)

entrada1=tk.Entry(ventana)
entrada1.configure(fg="black",bg="white",font=("arial",10))
entrada1.place(x= 300, y =80)

etiqueta2=tk.Label(frame1,text="Numero de páginas:",font=("arial",10))
etiqueta2.grid(row=1, column=0)

entrada2=tk.Entry(ventana)
entrada2.configure(fg="black",bg="white",font=("arial",10))
entrada2.place(x= 300, y =105)

etiqueta3=tk.Label(frame1,text="Tiempo por página (seg):",font=("arial",10))
etiqueta3.grid(row=2, column=0)

entrada3=tk.Entry(ventana)
entrada3.configure(fg="black",bg="white",font=("arial",10))
entrada3.place(x= 300, y =130)

boton=tk.Button(frame1,text="AGREGAR A LA COLA")
boton.grid(row=3, column=1)

frame2=tk.Frame(ventana)
frame2.configure(width=700, height=100,bg="black",bd=5)
frame2.place(x=50,y=200)

etiqueta=tk.Label(frame1,text="COLA DE IMPRESIÓN",font=("arial",15))
etiqueta.grid(row=4, column=0)


etiqueta=tk.Label(frame1,text="ESTADO DE IMPRESIÓN",font=("arial",15))
etiqueta.grid(row=10, column=0)

frame4=tk.Frame(ventana)
frame4.configure(width=650, height=70,bg="black",bd=5)
frame4.place(x=50,y=350)

ventana.mainloop()