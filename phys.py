import tkinter as tk
import math

g = 9.80665

def get_g():
    global g
    return g

def set_g():
    global g
    def setg():
        global g
        var = entry.get()
        if var == 'default':
            g = 9.80665
            label.config({'text':'g = 9.80665'})
            window.destroy()
        else:
            g = float(var)
            label.config({'text':'g = '+str(g)})
            window.destroy()

    window = tk.Tk()
    window.title('Set g')
    window.geometry('150x70')

    label = tk.Label(window, text='Enter a value:')
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text='Set g', command=setg)
    button.pack()

    window.mainloop()

def vertically(speed, height, time):
    global g
    return height + speed * time * g * time ** 2 / 2

def horizontally_Y(height, time):
    global g
    return height - g * time ** 2 / 2

def horizontally_X(speed, time):
    return speed * time

def angle_Y(speed, angle, time):
    global g
    n = speed * math.sin(angle)
    return n * time - g * time ** 2 / 2

def angle_X(speed, angle, time):
    n = speed * math.cos(angle)
    return n * time

# Speeds

def speed_angle_Y(speed,angle, time):
    global g
    return speed * math.sin(angle) - g * time

def speed_angle_X(speed,angle):
    return speed * math.sin(angle)


def speed_horizontally_Y(time):
    global g
    return -g * time

def speed_horizontally_X(speed):
    return speed


def speed_vertically_X(speed):
    return 0

def speed_vertically_Y(speed, time):
    global g
    return speed -g * time