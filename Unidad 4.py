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
        if cantidad <= 0:
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

def agregar_producto():
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        producto = Producto(nombre, precio, cantidad)
        detalles_producto = producto.mostrar_detalles()
        messagebox.showinfo("Detalles del Producto", detalles_producto)
    except ProductoInvalidoException as e:
        messagebox.showerror("Error", str(e))
    except PrecioInvalidoException as e:
        messagebox.showerror("Error", str(e))
    except CantidadInvalidaException as e:
        messagebox.showerror("Error", str(e))
    except ValueError:
        messagebox.showerror("Error", "Precio y cantidad deben ser valores numéricos.")


ventana = tk.Tk()
ventana.title("Gestión de Productos")
ventana.geometry("300x200")

tk.Label(ventana, text="Nombre del Producto:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Precio:").pack(pady=5)
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Label(ventana, text="Cantidad:").pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()


btn_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
btn_agregar.pack(pady=10)


ventana.mainloop()
