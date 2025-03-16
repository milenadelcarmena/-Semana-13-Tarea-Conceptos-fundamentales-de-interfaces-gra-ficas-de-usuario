import tkinter as tk
from tkinter import ttk


class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuarios")
        self.root.geometry("400x300")
        self.datos = []

        # Componentes de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Etiquetas y campos de texto
        tk.Label(self.root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre = tk.Entry(self.root)
        self.nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Correo:").grid(row=1, column=0, padx=5, pady=5)
        self.correo = tk.Entry(self.root)
        self.correo.grid(row=1, column=1, padx=5, pady=5)

        # Botones de acción
        frame_botones = tk.Frame(self.root)
        tk.Button(frame_botones, text="Agregar", command=self.agregar_registro).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar).pack(side=tk.LEFT, padx=5)
        frame_botones.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista de registros
        self.lista = tk.Listbox(self.root, width=50)
        self.lista.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def agregar_registro(self):
        """Agrega un nuevo registro a la lista"""
        nombre = self.nombre.get()
        correo = self.correo.get()

        if nombre and correo:
            registro = f"{nombre} - {correo}"
            self.datos.append(registro)
            self.lista.insert(tk.END, registro)
            self.nombre.delete(0, tk.END)
            self.correo.delete(0, tk.END)

    def limpiar(self):
        """Borra todos los registros y campos de texto"""
        self.datos.clear()
        self.lista.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.correo.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
