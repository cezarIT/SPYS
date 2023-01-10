import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
def show(array):
    def Gauss_dist(data, x):
        std = np.sqrt(np.var(data))
        return (1 / (std * np.sqrt(2 * np.pi))) * np.e**(-1/2 * ((x - np.mean(data)) / std)**2)
    fig, ax = plt.subplots()
    ax.plot(np.linspace(-5, 15, 100), Gauss_dist(array, np.linspace(-5, 15, 100)))
    ax.set_xlabel('x')
    ax.set_ylabel('Gauss Distribution')
    ax.set_title('Gauss Distribution of Numbers')
    plt.show()
# Create main window
window = tk.Tk()
window.title('Gauss Distribution Calculator')
window.geometry('200x100')
window.iconbitmap('C:/program1/app_ico.ico')
# Create input fields for data and x values
data_label = tk.Label(window, text="Enter data values (comma-separated):")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()
# Create button to trigger Gauss_dist() function
def calculate_button_clicked():
    data_str = data_entry.get()
    data = [int(x) for x in data_str.split(",")]  # Convert data string to list of integers
    x = 0
    show(data)
calculate_button = tk.Button(window, text="Calculate", command=calculate_button_clicked)
calculate_button.pack()
# Run main loop
window.mainloop()