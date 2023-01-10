""" Import libreles """

from phys import *
import er_win
import help
import slog

import subprocess
from tkinter import *
from tkinter import ttk

""" Main code """
slog.clear()
slog.add('Session start', 1)
#functions

def open_gaus():
    slog.add('Gauss Distribution Calculator opening', 10)
    subprocess.run(['python', 'gaus_dist.pyw'], creationflags=subprocess.CREATE_NO_WINDOW)

def g_set():
    set_g()

def win_calc():
    slog.add('Open Windows Calc', 2)
    subprocess.call('"C:\Windows\System32\calc.exe"')

def help_page():
    slog.add('Open help page', 3)
    help.help()
def about_page():
    slog.add('Open about page', 4)
    help.about()

def open_sqqu():
    slog.add('square equations solver opening', 5)
    subprocess.run(['python', 'sqqu.pyw'], creationflags=subprocess.CREATE_NO_WINDOW)

def button_speed_clicked():
    slog.add('Button_speed clicked!', 6)
    opt = selected_option.get()
    axis = selected_axis.get()
    
    try:
        if opt == 'Body thrown vertically upwards':
            if axis == 'Axis X':
                out_label_speed.config({'text' : 'Speed = ' + str(speed_vertically_X(float(in_entry_speed.get())))})
            elif axis == 'Axis Y':
                out_label_speed.config({'text' : 'Speed = ' + str(speed_vertically_Y(float(in_entry_speed.get()),float(in_entry_time.get())))})
        elif opt == 'Body thrown horizontally':
            if axis == 'Axis X':
                out_label_speed.config({'text':'Speed = ' + str(speed_horizontally_X(float(in_entry_speed.get())))})
            elif axis == 'Axis Y':
                out_label_speed.config({'text':'Speed = ' + str(speed_horizontally_Y(float(in_entry_time.get())))})
        elif opt == 'The body is thrown at an angle to the horizon':
            if axis == 'Axis X':
                out_label_speed.config({'text' : 'speed = ' + str(speed_angle_X(float(in_entry_speed.get()), float(in_entry_angle.get())))})
            elif axis == 'Axis Y':
                out_label_speed.config({'text' : 'speed = ' + str(speed_angle_Y(float(in_entry_speed.get()), float(in_entry_angle.get()), float(in_entry_time.get())))})
        else:
            slog.add('No situation selected', 102 )
            er_win.err('No situation selected', 102)
    except:
        slog.add('No data', 104)
        er_win.err('No data', 104)

def button_calculate_clicked():
    slog.add('Button_calculate clicked!', 7)
    opt = selected_option.get()
    axis = selected_axis.get()

    try:
        if opt == 'Body thrown vertically upwards':
            out_label_height.config({'text':'Height =  ' +  str(vertically(float(in_entry_speed.get()), float(in_entry_height.get()), float(in_entry_time.get())))})
        elif opt == 'The body is thrown at an angle to the horizon':
            if axis == 'Axis X':
                out_label_height.config({'text':'Height = ' + str(angle_X(float(in_entry_speed.get()),float(in_entry_angle.get()) ,float(in_entry_time.get())))})
            elif axis == 'Axis Y':
                out_label_height.config({'text':'Height = ' + str(angle_Y(float(in_entry_speed.get()),float(in_entry_angle.get()) ,float(in_entry_time.get())))})
            else:
                slog.add('No axis selected', 101)
                er_win.err('No axis selected - Select X or Y axis', 101)
        elif opt == 'Body thrown horizontally':
            if axis == 'Axis X':
                out_label_height.config({'text':'Height = ' + str(horizontally_X(float(in_entry_speed.get()),float(in_entry_time.get())))})
            elif axis == 'Axis Y':
                out_label_height.config({'text':'Height = ' + str(horizontally_Y(float(in_entry_height.get()),float(in_entry_time.get())))})
            else:
                slog.add('No axis selected', 101)
                er_win.err('No axis selected - Select X or Y axis', 101)
        else:
            slog.add('No situation selected', 102)
            er_win.err('No situation selected', 102)
    except:
        slog.add('No data', 104)
        er_win.err('No data', 104)

def show_selected_option(option):
    slog.add(f'Selected option: {option}', 8)

def show_selected_axis(option):
    slog.add(f'Selected axis: {option}', 9)

''' Create the main window '''

window = Tk()
window.title('SPYS')
window.geometry('500x300')
window.iconbitmap('C:/program1/app_ico.ico')

selected_option = StringVar()
selected_axis = StringVar()

''' Create menu bar '''

# Create a Menu widget

menu_bar = Menu(window)

# Create a File menu with some options

#file_menu = Menu(menu_bar, tearoff=0)
#file_menu.add_command(label='New', command=lambda: print('New selected'))
#file_menu.add_command(label='Open', command=lambda: print('Open selected'))
#file_menu.add_separator()
#file_menu.add_command(label='Exit', command=window.quit)
#menu_bar.add_cascade(label='File', menu=file_menu)

# Create a Settings menu with some options

settings_menu = Menu(menu_bar, tearoff=0)
#settings_menu.add_command(label='Language', command=lambda: print('Language selected'))
#settings_menu.add_command(label='Theme', command=lambda: print('Theme selected') )
settings_menu.add_command(label='Set g', command= g_set)
menu_bar.add_cascade(label='Settings', menu= settings_menu)

# Create a Help menu with some options

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command= about_page )
help_menu.add_command(label='Help', command= help_page )
menu_bar.add_cascade(label='Help', menu=help_menu)

# Algebra menu

alg_menu = Menu(menu_bar, tearoff=0)
alg_menu.add_command(label='Gauss Distribution Calculator', command= open_gaus)
alg_menu.add_command(label='square equations solver', command= open_sqqu)
alg_menu.add_command(label='Windows standart calc', command= win_calc)
menu_bar.add_cascade(label='Algebra', menu=alg_menu)

# Add the Menu widget to the window

window.config(menu=menu_bar)

''' Create a container widget '''

but_cont = Frame(window)
but_cont.grid(row=1, column=0, sticky='nw')

input_cont = Frame(window)
input_cont.grid(row=0, column=1, sticky='nw')

output_cont = Frame(window)
output_cont.grid(row=0, column=0, sticky='nw')

''' Add widgets '''

# Output

out_label_speed = Label(output_cont, text='Speed')
out_label_speed.grid(row=0, column=0, sticky='nw', padx = 10, pady = 10)

out_label_height = Label(output_cont, text= 'Height' )
out_label_height.grid(row=1, column=0, sticky='nw', padx = 10, pady = 10)

# Input

in_label_speed = Label(input_cont, text= 'Speed = ' )
in_label_speed.grid(row=0, column=0, sticky='nw', padx = 0, pady = 10)  
in_entry_speed = Entry(input_cont)
in_entry_speed.grid(row = 0, column = 1, sticky='nw', padx = 10, pady = 10)

in_label_height = Label(input_cont, text= 'Height = ' )
in_label_height.grid(row=1, column=0, sticky='nw', padx = 0, pady = 10)
in_entry_height = Entry(input_cont)
in_entry_height.grid(row = 1, column = 1, sticky='nw', padx = 10, pady = 10)

in_label_time = Label(input_cont, text= 'Time = ' )
in_label_time.grid(row=2, column=0, sticky='nw', padx = 0, pady = 10)
in_entry_time = Entry(input_cont)
in_entry_time.grid(row = 2, column = 1, sticky='nw', padx = 10, pady = 10)

in_label_angle = Label(input_cont, text= 'Angle = ' )
in_label_angle.grid(row=3, column=0, sticky='nw', padx = 0, pady = 10)
in_entry_angle = Entry(input_cont)
in_entry_angle.grid(row = 3, column = 1, sticky='nw', padx = 10, pady = 10)

# Buttoms

button_calculate = Button(but_cont, text='calculate', command=button_calculate_clicked)
button_calculate.grid(row=0, column=0, sticky='nw', padx=10, pady=10)

button_right = Button(but_cont, text='Get axis speed', command=button_speed_clicked)
button_right.grid(row=0, column=1, sticky='nw', padx=10, pady=10)

option_menu = OptionMenu(window, selected_option, 'Body thrown vertically upwards', 'Body thrown horizontally', 'The body is thrown at an angle to the horizon', command=show_selected_option, )
option_menu.grid(row=2, column=0, sticky='nw', padx=0, pady=10, )

axis_menu = OptionMenu(window, selected_axis, 'Axis X', 'Axis Y', command=show_selected_axis, )
axis_menu.grid(row=2, column=1, sticky='nw', padx=0, pady=10, )

# Run the Tkinter event loop

window.mainloop()
