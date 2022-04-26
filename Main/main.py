from tkinter import *
import sys
import os


def encrypt_btn_clicked():
    window.destroy()
    os.system('python encrypt.py')
    print("Button Clicked")

def decrypt_btn_clicked():
    window.destroy()
    os.system('python decrypt.py')
    print("Button Clicked")

window = Tk()

window.title="Cryptography"
window.geometry("640x406")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 406,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Main/background.png")
background = canvas.create_image(
    320.0, 203.0,
    image=background_img)

img0 = PhotoImage(file = f"Main/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = encrypt_btn_clicked,
    relief = "flat")

b0.place(
    x = 122, y = 319,
    width = 127,
    height = 36)

img1 = PhotoImage(file = f"Main/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = decrypt_btn_clicked,
    relief = "flat")

b1.place(
    x = 390, y = 319,
    width = 127,
    height = 36)

window.resizable(False, False)
window.mainloop()
