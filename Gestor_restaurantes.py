from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador += numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comidas[x].set('0')
        x += 1

    y = 0
    for c in cuadros_bebidas:
        if variables_bebida[y].get() == 1:
            cuadros_bebidas[y].config(state=NORMAL)
            if cuadros_bebidas[y].get() == '0':
                cuadros_bebidas[y].delete(0, END)
            cuadros_bebidas[y].focus()
        else:
            cuadros_bebidas[y].config(state=DISABLED)
            texto_bebidas[y].set('0')
        y += 1

    z = 0
    for c in cuadros_postres:
        if variables_postre[z].get() == 1:
            cuadros_postres[z].config(state=NORMAL)
            if cuadros_postres[z].get() == '0':
                cuadros_postres[z].delete(0, END)
            cuadros_postres[z].focus()
        else:
            cuadros_postres[z].config(state=DISABLED)
            texto_postres[z].set('0')
        z += 1

def total():
    subtotal_comida = 0
    subtotal_bebidas = 0
    subtotal_postres = 0
    p = 0
    for cantidad in texto_comidas:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    p = 0
    for cantidad in texto_bebidas:
        subtotal_bebidas = subtotal_bebidas + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    p = 0
    for cantidad in texto_postres:
        subtotal_postres = subtotal_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
    subtotal = subtotal_postres + subtotal_bebidas + subtotal_comida
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    var_costo_comida.set(f'$ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'$ {round(subtotal_bebidas, 2)}')
    var_costo_postre.set(f'$ {round(subtotal_postres, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo():
    texto_recibos.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibos.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibos.insert(END, f'*'*55+'\n')
    texto_recibos.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibos.insert(END, f'-'*66+'\n')

    x=0
    for comida in texto_comidas:
        if comida.get() != '0':
            texto_recibos.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get()) * precios_comida[x]}\n')
        x += 1
    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibos.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibos.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t${int(postre.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibos.insert(END, f'-' * 66 + '\n')
    texto_recibos.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibos.insert(END, f'Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibos.insert(END, f'Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibos.insert(END, f'-' * 66 + '\n')
    texto_recibos.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibos.insert(END, f'impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibos.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibos.insert(END, f'-' * 66 + '\n')
    texto_recibos.insert(END, 'Lo esperamos Pronto!')

def guardar():
    info_recibo = texto_recibos.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

def resetear():
    texto_recibos.delete(0.1, END)
    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for variable in variables_comida:
        variable.set('0')
    for variable in variables_bebida:
        variable.set('0')
    for variable in variables_postre:
        variable.set('0')

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_total.set('')
    var_impuesto.set('')


# iniciar tkinter
apliacion = Tk()

# Tamano app
apliacion.geometry("1120x630+0+0")

# Evitar Maximizar
apliacion.resizable(0, 0)

# Titulo de la ventana
apliacion.title("Mi Restaurante - Sistema de facturacion")

# Color de la ventana
apliacion.config(bg="burlywood")

# Panel superior
panel_superior = Frame(apliacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='black',
                        font=('Dosis', 50), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0, sticky=E)

# Panel izquierdo
panel_izquierdo = Frame(apliacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg= 'azure4', padx=55)
panel_costos.pack(side=BOTTOM)

# Panel comida
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(apliacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel recibos
panel_recibos = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibos.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# Generar items comida
variables_comida =[]
cuadros_comida=[]
texto_comidas=[]
contador = 0
for comida in lista_comidas:

    # Crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_comida[contador], command= revisar_check)
    comida.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comidas.append('')
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_comidas[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

# Generar items bebida
variables_bebida=[]
cuadros_bebidas=[]
texto_bebidas=[]
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_bebida[contador], command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador, column=1)
    contador += 1

# Generar items postres
variables_postre =[]
cuadros_postres=[]
texto_postres=[]
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_postre[contador], command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)
    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_costo_comida= Label(panel_costos, text='Costo comida', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida =Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida= Label(panel_costos, text='Costo bebidas', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida =Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre= Label(panel_costos, text='Costo postres', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre =Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_costo_subtotal= Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
etiqueta_costo_subtotal.grid(row=0,column=4)

texto_costo_subtotal =Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_costo_subtotal.grid(row=0, column=3, padx=41)

etiqueta_costo_impuestos= Label(panel_costos, text='Impuestos', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
etiqueta_costo_impuestos.grid(row=1,column=4)

texto_costo_impuestos =Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_impuesto)
texto_costo_impuestos.grid(row=1, column=3, padx=41)

etiqueta_costo_total= Label(panel_costos, text='Total', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
etiqueta_costo_total.grid(row=2,column=4)

texto_costo_total =Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
texto_costo_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['total', 'recibos', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis', 16, 'bold'), fg='white', bg='azure4', bd=1,width=8)
    boton.grid(row=0,column=columnas)
    botones_creados.append(boton)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Area de recibos
texto_recibos = Text(panel_recibos, font=('Dosis', 12, 'bold'), bd=1, width=49, height=10)
texto_recibos.grid(row=0,column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), bd=1, width=37)
visor_calculadora.grid(row=0,column=0,columnspan=4)
botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','R','B','0','/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(),font=('Dosis', 16, 'bold'),fg='white',bg='azure4',bd=1,width=8)
    boton.grid(row=fila, column=columna)

    botones_guardados.append(boton)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))


# Evitar que la pantalla se cierre
apliacion.mainloop()
