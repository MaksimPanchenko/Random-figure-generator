import tkinter as tk
import random

def create_shape():
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    shape = random.choice(['square', 'circle', 'triangle'])

    if shape == 'square':
        size = random.randint(10, 100)

        x1 = random.randint(0, canvas_width - size)
        y1 = random.randint(0, canvas_height - size)
        x2 = x1 + size
        y2 = y1 + size

        canvas.create_rectangle(x1, y1, x2, y2, fill='red')

    elif shape == 'circle':
        size = random.randint(10, 100)

        x1 = random.randint(0, canvas_width - size)
        y1 = random.randint(0, canvas_height - size)
        x2 = x1 + size
        y2 = y1 + size

        canvas.create_oval(x1, y1, x2, y2, fill='green')

    elif shape == 'triangle':
        size = random.randint(10, 100)

        x1 = random.randint(0, canvas_width - size)
        y1 = random.randint(0, canvas_height - size)
        x2 = x1 + size
        y2 = y1 + size
        x3 = x1 + size/2
        y3 = y1 - size/2

        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='blue')

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
button = tk.Button(root, text='Создать форму', command=create_shape)
button.pack()
root.mainloop()
