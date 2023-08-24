import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import filedialog
from fpdf import FPDF
from controllers.clientes import getClientes
from controllers.productos import getProductos
from controllers.facturas import getFacturas

class ReporteFacturasForm(tk.Frame):
    def __init__(self, master, userSession):
        super().__init__(master)
        self.master = master
        self.userSession = userSession
        self.master.title("Reporte de Facturas")

        self.clientes = self.fillClientes()
        self.productos = self.fillProductos()
        self.cliente = tk.StringVar()
        self.producto = tk.StringVar()
        self.filtrar = tk.StringVar()
        self.primera = tk.StringVar()
        self.segunda = tk.StringVar()

        self.crear_vista()

    def fillClientes(self):
        clientes = getClientes()
        nombres_clientes = []
        for c in clientes:
            nombres_clientes.append(c['nombres'])
        return nombres_clientes
    
    def fillProductos(self):
        productos = getProductos()
        nombres_productos = []
        for p in productos:
            nombres_productos.append(p['nombre'])
        return nombres_productos

    def crear_vista(self):
        tk.Label(self, text="Filtrar:").grid(row=0, column=0, sticky="e")
        tk.OptionMenu(self, self.filtrar, "Cliente", "Producto", "Fecha").grid(row=0, column=1)

        tk.Button(self, text="Filtrar", command=self.filtro).grid(row=0, column=2)

    def filtro(self):
        tk.Label(self, text=" ", height=1).grid(row=1)

        if self.filtrar.get() == 'Cliente':
            tk.Label(self, text="Cliente:").grid(row=2, column=0, sticky="e")
            tk.OptionMenu(self, self.cliente, *self.clientes).grid(row=2, column=1)
            tk.Label(self, text=" ", height=1).grid(row=3)
        elif self.filtrar.get() == 'Producto':
            tk.Label(self, text="Producto:").grid(row=2, column=0, sticky="e")
            tk.OptionMenu(self, self.producto, *self.productos).grid(row=2, column=1)
            tk.Label(self, text=" ", height=1).grid(row=3)
        elif self.filtrar.get() == 'Fecha':
            tk.Label(self, text="Fecha:").grid(row=2, column=0, sticky="e")
            DateEntry(self, textvariable=self.primera, date_pattern="dd/mm/y").grid(row=2, column=1)
            tk.Label(self, text="Fecha:").grid(row=2, column=2, sticky="e")
            DateEntry(self, textvariable=self.segunda, date_pattern="dd/mm/y").grid(row=2, column=3)
            tk.Label(self, text=" ", height=1).grid(row=3)

        tk.Button(self, text="Reporte", command=self.reporte).grid(row=4, column=0)
        tk.Button(self, text="PDF", command=self.pdf).grid(row=4, column=1)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=4, column=2)

        tk.Label(self, text=" ", height=1).grid(row=5)

        self.tabla = ttk.Treeview(self, columns=("ID Factura", "Fecha", "Cliente", "Total"), show="headings")
        self.tabla.heading("#1", text="Id Factura")
        self.tabla.heading("#2", text="Fecha")
        self.tabla.heading("#3", text="Cliente")
        self.tabla.heading("#4", text="Total")
        self.tabla.column("#1", width=80, anchor="center")
        self.tabla.column("#2", width=80, anchor="center")
        self.tabla.column("#3", width=80, anchor="center")
        self.tabla.column("#4", width=80, anchor="center")
        self.tabla.grid(row=6, columnspan=5)

    def reporte(self):
        facturas = getFacturas()
        for f in facturas:
            if self.filtrar.get() == 'Cliente':
                cliente = self.cliente.get()
                if f['cliente'] == cliente:
                    row = (f['id'], f['fecha'], f['cliente'], f['total'])
                    self.tabla.insert("", "end", values=row)
            elif self.filtrar.get() == 'Producto':
                producto = self.producto.get()
                for p in f['productos']:
                    if p[0] == producto:
                        row = (f['id'], f['fecha'], f['cliente'], f['total'])
                        self.tabla.insert("", "end", values=row)
            elif self.filtrar.get() == 'Fecha':
                primera = datetime.strptime(self.primera.get(), "%d/%m/%Y").date()
                segunda = datetime.strptime(self.segunda.get(), "%d/%m/%Y").date()
                if datetime.strptime(f['fecha'], "%d/%m/%Y").date() > primera and datetime.strptime(f['fecha'], "%d/%m/%Y").date() < segunda:
                    row = (f['id'], f['fecha'], f['cliente'], f['total'])
                    self.tabla.insert("", "end", values=row)

    def pdf(self):
        facturas = getFacturas()
        for f in facturas:
            if self.filtrar.get() == 'Cliente':
                cliente = self.cliente.get()
                if f['cliente'] == cliente:
                    self.generar_pdf(f)
            elif self.filtrar.get() == 'Producto':
                producto = self.producto.get()
                for p in f['productos']:
                    if p[0] == producto:
                        self.generar_pdf(f)
            elif self.filtrar.get() == 'Fecha':
                primera = datetime.strptime(self.primera.get(), "%d/%m/%Y").date()
                segunda = datetime.strptime(self.segunda.get(), "%d/%m/%Y").date()
                if datetime.strptime(f['fecha'], "%d/%m/%Y").date() > primera and datetime.strptime(f['fecha'], "%d/%m/%Y").date() < segunda:
                    self.generar_pdf(f)

    def generar_pdf(self, f):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Reporte de Factura", 0, 1, "L")
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Id Factura: "+str(f['id']), 0, 1, "L")
        pdf.cell(0, 10, "Fecha: "+f['fecha'], 0, 1, "L")
        pdf.cell(0, 10, "Cliente: "+f['cliente'], 0, 1, "L")
        pdf.ln(5)

        col_width = pdf.w / 3.5
        row_height = pdf.font_size * 2
        pdf.set_x((pdf.w - col_width * 2) / 2)
        pdf.cell(col_width, row_height, "Producto", border=1)
        pdf.cell(col_width, row_height, "Cantidad", border=1, ln=True)

        for p in f['productos']:
            pdf.set_x((pdf.w - col_width * 2) / 2)
            pdf.cell(col_width, row_height, p[0], border=1)
            pdf.cell(col_width, row_height, p[1], border=1, ln=True)

        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Total: Q"+str(f['total']), 0, 0, "L")

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            pdf.output(file_path)

    def limpiar(self):
        self.cliente.set("")
        self.producto.set("")
        self.filtrar.set("")
        self.primera.set("")
        self.segunda.set("")
        self.tabla.delete(*self.tabla.get_children())
        