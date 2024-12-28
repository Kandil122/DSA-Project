"""
Sorting Algorithms Visualization with CSV Export Functionality.
"""

# Importing required libraries and modules
from tkinter import *
from tkinter import ttk
import random
import csv
import time  # Ensure the `time` module is imported

# Importing sorting algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.quickSort import quick_sort
from algorithms.mergeSort import merge_sort

# Importing colors
from colors import *

# Create tkinter window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg=WHITE)

# Initialize variables
algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []  # List to store array data

# Draw data as vertical bars on canvas
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# Generate random array
def generate():
    global data
    data = [random.randint(1, 150) for _ in range(100)]  # Generate random numbers
    drawData(data, [BLUE for x in range(len(data))])

# Set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

# Save sorting results to CSV file
def save_to_csv(algorithm, elapsed_time):
    filename = f"{algorithm}_results.csv"
    try:
        with open(filename, mode='a', newline='') as file:  # Append mode
            writer = csv.writer(file)
            # Add headers if file is empty
            file.seek(0)
            if file.read(1) == "":
                writer.writerow(["Algorithm", "Array Size", "Elapsed Time (seconds)"])
            writer.writerow([algorithm, len(data), f"{elapsed_time:.5f}"])
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"Error saving to file {filename}: {e}")

# Perform sorting and visualize
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        start_time = time.time()  # Start time tracking
        bubble_sort(data, drawData, timeTick)
        elapsed_time = time.time() - start_time
        save_to_csv("Bubble Sort", elapsed_time)

    elif algo_menu.get() == 'Selection Sort':
        start_time = time.time()
        selection_sort(data, 0, len(data) - 1, drawData, timeTick)
        elapsed_time = time.time() - start_time
        save_to_csv("Selection Sort", elapsed_time)

    elif algo_menu.get() == 'Insertion Sort':
        start_time = time.time()
        insertion_sort(data, 0, len(data) - 1, drawData, timeTick)
        elapsed_time = time.time() - start_time
        save_to_csv("Insertion Sort", elapsed_time)

    elif algo_menu.get() == 'Quick Sort':
        start_time = time.time()
        quick_sort(data, 0, len(data) - 1, drawData, timeTick)
        elapsed_time = time.time() - start_time
        save_to_csv("Quick Sort", elapsed_time)

    elif algo_menu.get() == 'Merge Sort':
        start_time = time.time()
        merge_sort(data, 0, len(data) - 1, drawData, timeTick)
        elapsed_time = time.time() - start_time
        save_to_csv("Merge Sort", elapsed_time)

# UI frame
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Dropdown to select sorting algorithm
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# Dropdown to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# Buttons for actions
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# Canvas to draw array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

# Main loop
window.mainloop()
