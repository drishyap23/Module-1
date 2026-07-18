from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


window = Tk()
window.title("My Photo Album")
window.geometry("450x500")
window.config(bg="lavender")


title_label = Label(
    window,
    text="My Photo Album",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="purple",
    width=25
)
title_label.pack(pady=15)