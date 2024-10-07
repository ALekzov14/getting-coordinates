from pynput import mouse
import tkinter as tk
from tkinter import scrolledtext

def add_text(x, y, button, pressed):
    if button == mouse.Button.left or mouse.Button.right and pressed:
        txt.insert(tk.END, f"X:{x} Y:{y}" + "\n")

listener = mouse.Listener(on_click=add_text)

try:
    from tkinter import*
except:
    from tkinter import*

window = Tk()
window.iconbitmap("icon.ico")
window.title("test")
window.geometry("390x240")

# Создание scrolledtext
txt = scrolledtext.ScrolledText(window, width=40, height=14)
txt.pack()

listener.start()
window.attributes("-topmost",True)

window.mainloop()