from tkinter import *
from tkinter import ttk
import random
from quicksort import quick_sort

root = Tk()
root.title('Quick Sort Visualized')

root.maxsize(900, 600)
root.config(bg='black')

select_alg = StringVar()
data = []


def generate():
    global data

    minval = int(minEntry.get())
    maxval = int(maxEntry.get())
    sizeval = int(sizeEntry.get())

    data = []
    for _ in range(sizeval):
        data.append(random.randrange(minval, maxval + 1))
    draw_d(data, ['red' for x in range(len(data))])


def draw_d(data, colorlist):
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width / (len(data) + 1)
    offset = 30
    spacing = 10

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        # 0, 0 = top left
        x0 = i * x_width + offset + spacing
        y0 = can_height - height * 340

        # bottom right
        x1 = ((i + 1) * x_width) + offset
        y1 = can_height

        canvas.create_rectangle(x0, y0, x1, y1, fill = colorlist[i])
        canvas.create_text(x0 + 2, y0, anchor = SE, text = str(data[i]))
    root.update_idletasks()

def start_algorithm():
    global data
    if not data:
        return
    
    if(algmenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data) - 1, draw_d, speedbar.get())
        draw_d(data, ['green' for x in range(len(data))])

Mainframe = Frame(root, width = 600, height = 200, bg = "grey")
Mainframe.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = Canvas(root, width = 600, height = 380, bg = "grey")
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

Label(Mainframe, text = "Sorting Algorithm", bg = 'grey').grid(
    row = 0, column = 0, padx = 5, pady = 5, sticky = W)
 
algmenu = ttk.Combobox(Mainframe, textvariable = select_alg,
                       values = ['Quick Sort'])
algmenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algmenu.current(0)

Button(Mainframe, text = "Begin", bg = "blue",
       command = start_algorithm).grid(row = 1,
                                       column = 3,
                                       padx = 5, 
                                       pady = 5)

speedbar = Scale(Mainframe, from_ = 0.10,
                 to = 2.0, length = 100, digits = 2,
                 resolution = 0.2, orient = HORIZONTAL,
                 label = "Select Speed")
speedbar.grid(row = 0, column = 2, padx = 5, pady = 5)

sizeEntry = Scale(Mainframe, from_ = 3,
                  to = 60, resolution = 1,
                  orient = HORIZONTAL,
                  label = "Size")
sizeEntry.grid(row = 1, column = 0, padx = 5, pady = 5)


minEntry = Scale(Mainframe, from_ = 0,
                 to = 10, resolution = 1,
                 orient = HORIZONTAL,
                 label = "Min Value")
minEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

maxEntry = Scale(Mainframe, from_ = 10,
                 to = 100, resolution = 1,
                 orient = HORIZONTAL,
                 label = "Max Value")
maxEntry.grid(row = 1, column = 2, padx = 5, pady = 5)

Button(Mainframe, text="Generate", bg= "red",
       command = generate).grid(row = 0, column = 3,
                                padx= 5, pady = 5)

root.mainloop()
