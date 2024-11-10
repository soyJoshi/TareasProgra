import tkinter as tk
from tkinter import messagebox

class ProductoInvalidoException(Exception):
    pass

class PrecioInvalidoException(Exception):
    pass

class CantidadInvalidaException(Exception):
    pass

class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not nombre or nombre.strip() == "":
            raise ProductoInvalidoException("El nombre del producto no puede estar vacío.")
        if precio <= 0:
            raise PrecioInvalidoException("El precio debe ser mayor a cero.")
        if cantidad < 0:
            raise CantidadInvalidaException("La cantidad no puede ser negativa.")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def mostrar_detalles(self):
        valor_total = self.calcular_valor_total()
        return (f"Nombre: {self.nombre}\n"
                f"Precio: ${self.precio:.2f}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Valor Total: ${valor_total:.2f}")

productos = []

def agregar_producto():
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        producto = Producto(nombre, precio, cantidad)
        productos.append(producto)  
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
    except ProductoInvalidoException as e:
        messagebox.showerror("Error", str(e))
    except PrecioInvalidoException as e:
        messagebox.showerror("Error", str(e))
    except CantidadInvalidaException as e:
        messagebox.showerror("Error", str(e))
    except ValueError:
        messagebox.showerror("Error", "Precio y cantidad deben ser valores numéricos.")

def mostrar_todos_los_productos():
    if not productos:
        messagebox.showinfo("Productos", "No hay productos registrados.")
    else:
        detalles = "\n\n".join([p.mostrar_detalles() for p in productos])
        messagebox.showinfo("Todos los Productos", detalles)


ventana = tk.Tk()
ventana.title("Gestión de Productos")
ventana.geometry("300x250")
ventana.configure(bg="black")

tk.Label(ventana, text="Nombre del Producto:", bg="lightblue", relief="ridge",font=("Arial",10,"italic")).pack(pady=5)
entry_nombre = tk.Entry(ventana, bg="cyan", relief="groove")
entry_nombre.pack()

tk.Label(ventana, text="Precio:", relief="ridge",font=("Arial",10,"italic"),bg="lightblue").pack(pady=5)
entry_precio = tk.Entry(ventana, bg="cyan", relief="groove")
entry_precio.pack()

tk.Label(ventana, text="Cantidad:", relief="ridge",font=("Arial",10,"italic"),bg="lightblue").pack(pady=5)
entry_cantidad = tk.Entry(ventana, bg="cyan",relief="groove")
entry_cantidad.pack()

btn_agregar = tk.Button(ventana, text="Agregar Producto",bg="blue",font=("Arial",10,"bold"),relief="sunken" ,command=agregar_producto)
btn_agregar.pack(pady=5)

btn_mostrar_todos = tk.Button(ventana, text="Mostrar Todos los Productos", bg="blue",font=("Arial",10,"bold"),relief="sunken",command=mostrar_todos_los_productos)
btn_mostrar_todos.pack(pady=5)

ventana.mainloop()
