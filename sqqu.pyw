import math
import er_win

from tkinter import *
def fsqm(a, b, c): #полное квадратное уровнение a b c - кф.
	D = b**2 - 4 * a * c
	if D < 0:
		out_D_label.config({'text':'D = '+str(D)})
	elif D == 0:
		x = - b + math.sqrt(D)/2*a
		out_x1_label.config({'text':'X1 = '+str(x)})
		out_D_label.config({'text':'D = '+str(D)})
	elif D > 0:
		x = - b + math.sqrt(D)/2*a
		xx = - b - math.sqrt(D)/2*a
		out_x1_label.config({'text':'X1 = '+str(x)})
		out_x2_label.config({'text':'X2 = '+str(xx)})
		out_D_label.config({'text':'D = '+str(D)})
#
def nfsqm(a, b, c, mod):  #не полное кв.у mod - 1 если ax^2 + bx = 0; 2 если ax^2 + c = 0 в ненужном кф. ставить 0
	if mod == 1:
		D = b**2 - 4 * a * 0
		if D < 0:
			out_D_label.config({'text':'D = '+str(D)})
		elif D == 0:
			x = - b + math.sqrt(D)/2*a
			out_x1_label.config({'text':'X1 = '+str(x)})
			out_D_label.config({'text':'D = '+str(D)})
		elif D > 0:
			x = - b + math.sqrt(D)/2*a
			xx = - b - math.sqrt(D)/2*a
			out_x1_label.config({'text':'X1 = '+str(x)})
			out_x2_label.config({'text':'X2 = '+str(xx)})
			out_D_label.config({'text':'D = '+str(D)})
	if mod == 2:
		D = 0**2 - 4 * a * c
		if D < 0:
			out_D_label.config({'text':'D = '+str(D)})
		elif D == 0:
			x = - b + math.sqrt(D)/2*a
			out_x1_label.config({'text':'X1 = '+str(x)})
			out_D_label.config({'text':'D = '+str(D)})
		elif D > 0:
			x = - b + math.sqrt(D)/2*a
			xx = - b - math.sqrt(D)/2*a
			out_x1_label.config({'text':'X1 = '+str(x)})
			out_x2_label.config({'text':'X2 = '+str(xx)})
			out_D_label.config({'text':'D = '+str(D)})

def show_selected_mode(option):
	print(option)

def but_calc_clicked():
	try:
		A = float(in_ent_a.get())
		B = float(in_ent_b.get())
		C = float(in_ent_c.get())
	except:
		er_win.err('No data', 104)
	mode = selected_mode.get()
	if mode == 'ax^2 + bx +c = 0':
		fsqm(A,B,C)
	elif mode == 'ax^2 + bx = 0':
		nfsqm(A, B, 0, 1)
	elif mode == 'ax^2 + c = 0':
		nfsqm(A, 0, C, 2)
	else:
		er_win.err('Equation type non selected', 103)

window = Tk()
window.title('SPYS: square equations solver')
window.geometry('550x200')
window.iconbitmap('C:/program1/app_ico.ico')
selected_mode = StringVar()
# Containers

interface = Frame(window)
interface.grid(row=1, column=0, sticky='nw')

butCon = Frame(window)
butCon.grid(row = 2, column= 0, sticky= 'nw')

view = Frame(window)
view.grid(row = 0, column= 0, sticky= 'nw')
# Labels

out_x1_label = Label(view, text='X1 = ')
out_x1_label.grid(row=0, column=0, sticky='nw', padx = 10, pady = 10)

out_x2_label = Label(view, text='X2 = ')
out_x2_label.grid(row=0, column=1, sticky='nw', padx = 10, pady = 10)

out_D_label = Label(view, text='D = ')
out_D_label.grid(row=0, column=2, sticky='nw', padx = 10, pady = 10)
# Entry

lab_a = Label(interface, text='a = ')
lab_a.grid(row=1, column=0, sticky='nw', padx = 5, pady = 10)
in_ent_a = Entry(interface)
in_ent_a.grid(row=1, column=1, sticky='nw', padx = 0, pady = 10)

lab_b = Label(interface, text='b = ')
lab_b.grid(row=1, column=2, sticky='nw', padx = 5, pady = 10)
in_ent_b = Entry(interface)
in_ent_b.grid(row=1, column=3, sticky='nw', padx = 0, pady = 10)

lab_c = Label(interface, text='c = ')
lab_c.grid(row=1, column=4, sticky='nw', padx = 5, pady = 10)
in_ent_c = Entry(interface)
in_ent_c.grid(row=1, column=5, sticky='nw', padx = 0, pady = 10)

# butt

but_calc = Button(butCon, text='calculate', command= but_calc_clicked)
but_calc.grid(row=0, column=1, sticky='nw', padx=10, pady=10, )

mode_menu = OptionMenu(butCon, selected_mode, 'ax^2 + bx = 0', 'ax^2 + bx +c = 0', 'ax^2 + c = 0', command= show_selected_mode, )
mode_menu.grid(row=0, column=0, sticky='nw', padx=10, pady=10, )

window.mainloop()
