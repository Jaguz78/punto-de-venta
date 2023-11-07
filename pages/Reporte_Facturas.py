import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import filedialog
from fpdf import FPDF
from controllers.clientes import getClientes
from controllers.productos import getProductos
from controllers.facturas import getFacturas, getDetalle_Factura, getProductos_Factura

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
            nombres_clientes.append(c[2])
        return nombres_clientes
    
    def fillProductos(self):
        productos = getProductos()
        nombres_productos = []
        for p in productos:
            nombres_productos.append(p[1])
        return nombres_productos

    def crear_vista(self):
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self.frame1, text="Filtrar:").grid(row=0, column=0, sticky="e", pady=10)
        tk.OptionMenu(self.frame1, self.filtrar, "Cliente", "Producto", "Fecha").grid(row=0, column=1, padx=(10,20), pady=10)

        tk.Button(self.frame1, text="Filtrar", command=self.filtro).grid(row=0, column=2, pady=10)

        tk.Label(self.frame1, text=" ", height=1).grid(row=1)

    def filtro(self):
        self.frame1.destroy()
        self.frame2 = tk.Frame(self)
        self.frame2.grid(row=1, column=0, padx=10, pady=10)
        if self.filtrar.get() == 'Cliente':
            tk.Label(self.frame2, text="Cliente:").grid(row=2, column=0, sticky="e")
            tk.OptionMenu(self.frame2, self.cliente, *self.clientes).grid(row=2, column=1)
        elif self.filtrar.get() == 'Producto':
            tk.Label(self.frame2, text="Producto:").grid(row=2, column=0, sticky="e")
            tk.OptionMenu(self.frame2, self.producto, *self.productos).grid(row=2, column=1)
        elif self.filtrar.get() == 'Fecha':
            tk.Label(self.frame2, text="Fecha:").grid(row=2, column=0, sticky="e")
            DateEntry(self.frame2, textvariable=self.primera, date_pattern="dd/mm/y").grid(row=2, column=1)
            tk.Label(self.frame2, text="Fecha:").grid(row=2, column=2, sticky="e")
            DateEntry(self.frame2, textvariable=self.segunda, date_pattern="dd/mm/y").grid(row=2, column=3)
        
        tk.Label(self.frame2, text=" ", height=1).grid(row=3)

        tk.Button(self.frame2, text="Reporte", command=self.reporte).grid(row=4, column=0)
        tk.Button(self.frame2, text="PDF", command=self.pdf).grid(row=4, column=1)
        tk.Button(self.frame2, text="Limpiar", command=self.limpiar).grid(row=4, column=2)

        tk.Label(self.frame2, text=" ", height=1).grid(row=5)

        self.tabla = ttk.Treeview(self.frame2, columns=("ID Factura", "Fecha", "Cliente", "Usuario", "Total"), show="headings")
        self.tabla.heading("#1", text="Id Factura")
        self.tabla.heading("#2", text="Fecha")
        self.tabla.heading("#3", text="Cliente")
        self.tabla.heading("#4", text="Usuario")
        self.tabla.heading("#5", text="Total")
        self.tabla.column("#1", width=80, anchor="center")
        self.tabla.column("#2", width=80, anchor="center")
        self.tabla.column("#3", width=80, anchor="center")
        self.tabla.column("#4", width=80, anchor="center")
        self.tabla.column("#5", width=80, anchor="center")
        self.tabla.grid(row=6, columnspan=5)

    def reporte(self):
        facturas = getFacturas()
        detalle_facturas = getDetalle_Factura()
        if self.filtrar.get() == 'Cliente':
            cliente = self.cliente.get()
            for f in facturas:
                if f[2] == cliente:
                    row = (f[0], f[1], f[2], f[3], f[4])
                    self.tabla.insert("", "end", values=row)
        elif self.filtrar.get() == 'Producto':
            producto = self.producto.get()
            for f in detalle_facturas:
                if f[5] == producto:
                    row = (f[0], f[1], f[2], f[3], f[4])
                    self.tabla.insert("", "end", values=row)
        elif self.filtrar.get() == 'Fecha':
            primera = datetime.strptime(self.primera.get(), "%d/%m/%Y").date()
            segunda = datetime.strptime(self.segunda.get(), "%d/%m/%Y").date()
            for f in facturas:
                if f[1] > primera and f[1] < segunda:
                    row = (f[0], f[1], f[2], f[3], f[4])
                    self.tabla.insert("", "end", values=row)

    def pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            pdf = FPDF()
            facturas = getFacturas()
            detalle_facturas = getDetalle_Factura()
            if self.filtrar.get() == 'Cliente':
                cliente = self.cliente.get()
                for f in facturas:
                    if f[2] == cliente:
                        self.generar_pdf(pdf, f)
            elif self.filtrar.get() == 'Producto':
                producto = self.producto.get()
                for f in detalle_facturas:
                    if f[5] == producto:
                        self.generar_pdf(pdf, f)
            elif self.filtrar.get() == 'Fecha':
                primera = datetime.strptime(self.primera.get(), "%d/%m/%Y").date()
                segunda = datetime.strptime(self.segunda.get(), "%d/%m/%Y").date()
                for f in facturas:
                    if f[1] > primera and f[1] < segunda:
                        self.generar_pdf(pdf, f)
        
        pdf.output(file_path)
        messagebox.showinfo("Success", "Reporte PDF generado")
        self.limpiar()

    def generar_pdf(self, pdf, f):
        productos = getProductos_Factura(f[0])
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Reporte de Factura", 0, 1, "L")
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Id Factura: "+str(f[0]), 0, 1, "L")
        pdf.cell(0, 10, "Fecha: "+str(f[1]), 0, 1, "L")
        pdf.cell(0, 10, "Cliente: "+str(f[2]), 0, 1, "L")
        pdf.cell(0, 10, "Usuario: "+str(f[3]), 0, 1, "L")
        pdf.ln(5)

        col_width = pdf.w / 3.5
        row_height = pdf.font_size * 2
        pdf.set_x((pdf.w - col_width * 2) / 2)
        pdf.cell(col_width, row_height, "Producto", border=1)
        pdf.cell(col_width, row_height, "Cantidad", border=1, ln=True)

        for p in productos:
            pdf.set_x((pdf.w - col_width * 2) / 2)
            pdf.cell(col_width, row_height, str(p[0]), border=1)
            pdf.cell(col_width, row_height, str(p[1]), border=1, ln=True)

        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Total: Q"+str(f[4]), 0, 0, "L")

    def limpiar(self):
        self.frame2.destroy()
        self.filtrar.set("")
        self.crear_vista()
        