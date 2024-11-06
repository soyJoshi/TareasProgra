import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicacion es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        divicion = num1 / num2
        messagebox.showinfo("Resultado", f"La divición es: {divicion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "División entre cero.")
        

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x300")
 
label_num1 = tk.Label(ventana, text="Número 1:",bg="lightblue",fg="black",font=("Fantasy",12,"bold"),relief="solid")
label_num1.grid(row=0,column=0)
entry_num1 = tk.Entry(ventana,bg="orange",relief="groove")
entry_num1.grid(row=0,column=1)
 
label_num2 = tk.Label(ventana, text="Número 2:",bg="lightblue",fg="black",font=("Arial",12,"italic"),relief="solid")
label_num2.grid(row=0,column=3)
entry_num2 = tk.Entry(ventana,bg="orange",relief="groove")
entry_num2.grid(row=0,column=4)
 
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar, bg="black",fg="white",font=("Arial",12))
boton_sumar.grid(row=2,column=1)
boton_restar = tk.Button(ventana, text="Restar", command=restar,bg="black",fg="white",font=("Arial",12))
boton_restar.grid(row=2,column=2)
boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar,bg="black",fg="white",font=("Arial",12))
boton_multiplicar.grid(row=2,column=3)
boton_dividir = tk.Button(ventana, text="Divición", command=dividir,bg="black",fg="white",font=("Arial",12))
boton_dividir.grid(row=2,column=4)
 
ventana.mainloop()