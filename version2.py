import tkinter as tk
from tkinter import messagebox


class ProductoInvalidoException(Exception):
    pass

class PrecioInvalidoException(Exception):
    pass

class CantidadInvalidaException(Exception):
    pass

# Clase Producto
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

# Lista para almacenar los productos
productos = []

# Función para agregar un producto
def agregar_producto():
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        producto = Producto(nombre, precio, cantidad)
        productos.append(producto)  # Agrega el producto a la lista
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
    except ProductoInvalidoException as e:
        messagebox.showerror("Error", str(e))
    except PrecioInvalidoException as e:
        messagebox.showerror("Error", str(e))
    except CantidadInvalidaException as e:
        messagebox.showerror("Error", str(e))
    except ValueError:
        messagebox.showerror("Error", "Precio y cantidad deben ser valores numéricos.")

# Función para mostrar todos los productos
def mostrar_todos_los_productos():
    if not productos:
        messagebox.showinfo("Productos", "No hay productos registrados.")
    else:
        detalles = "\n\n".join([p.mostrar_detalles() for p in productos])
        messagebox.showinfo("Todos los Productos", detalles)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Productos")
ventana.geometry("300x250")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre del Producto:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Precio:").pack(pady=5)
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Label(ventana, text="Cantidad:").pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

# Botones para agregar producto y mostrar todos los productos
btn_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
btn_agregar.pack(pady=5)

btn_mostrar_todos = tk.Button(ventana, text="Mostrar Todos los Productos", command=mostrar_todos_los_productos)
btn_mostrar_todos.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
