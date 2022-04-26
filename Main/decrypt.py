from tkinter import *
from tkinter import filedialog
import sys
import os
import Caesar_Cipher as cs
import steg as stg
from PIL import Image,ImageTk


fgColour = 'white'
yourImage = ''
ct1=''

def back_btn_clicked():
    window.destroy()
    os.system('python main.py')
    #print("Button Clicked")

def btn_clicked():
    print("Hi")

def selectImg():
    global yourImage
    yourImage=filedialog.askopenfilename(title = "Select your image",filetypes = [("Image Files","*.png"),("Image Files","*.jpg")])
    entry0.insert(END,yourImage)
    global my_image
    img = Image.open(yourImage)
    img = img.resize((267,147), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(img)
    entry2.image_create(END, image=my_image)    

def seg_dec():
    global ct1
    ct1 = stg.decode(yourImage)
    print(ct1)
    entry1.insert(END,"\nMessage Extracted from the Image : "+ yourImage+"\n\n----------\nEncrypted Message:\n"+ct1)

def cc_dec():
    outputFileName="Output/"+ entry3.get()
    key=int(entry5.get())
    loop=int(entry4.get())
    global ct1
    #entry6.insert(END,ct1)
    for i in range(loop) :
        ct = cs.cs_decrypt(ct1,key)
        ct1 = ct
        print(ct1)

    global cipherText 
    cipherText = ct1
    f = open(outputFileName, "a")
    f.write(cipherText)
    f.close()
    entry6.insert(END,"\nPlain Text :\n"+cipherText)

window = Tk()

window.title="Decryption"
window.geometry("1326x779")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 779,
    width = 1326,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Decrypt/background.png")
background = canvas.create_image(
    695.5, 396.0,
    image=background_img)

entry0_img = PhotoImage(file = f"Decrypt/img_textBox0.png")
entry0_bg = canvas.create_image(
    257.0, 112.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

entry0.place(
    x = 39, y = 94,
    width = 436,
    height = 34)

entry1_img = PhotoImage(file = f"Decrypt/img_textBox1.png")
entry1_bg = canvas.create_image(
    329.0, 542.0,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

entry1.place(
    x = 39, y = 335,
    width = 580,
    height = 412)

entry2_img = PhotoImage(file = f"Decrypt/img_textBox2.png")
entry2_bg = canvas.create_image(
    485.5, 225.5,
    image = entry2_img)

entry2 = Text(
    bd = 0,
    bg = "#040404",
    highlightthickness = 0)

entry2.place(
    x = 352, y = 151,
    width = 267,
    height = 147)

img0 = PhotoImage(file = f"Decrypt/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = selectImg,
    relief = "flat")

b0.place(
    x = 492, y = 94,
    width = 127,
    height = 36)

img1 = PhotoImage(file = f"Decrypt/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = seg_dec,
    relief = "flat")

b1.place(
    x = 130, y = 262,
    width = 127,
    height = 36)

img2 = PhotoImage(file = f"Decrypt/img2.png")
back_btn = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = back_btn_clicked,
    relief = "flat")

back_btn.place(
    x = 1182, y = 4,
    width = 127,
    height = 36)

entry3_img = PhotoImage(file = f"Decrypt/img_textBox3.png")
entry3_bg = canvas.create_image(
    998.0, 112.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

entry3.place(
    x = 708, y = 94,
    width = 580,
    height = 34)

entry4_img = PhotoImage(file = f"Decrypt/img_textBox4.png")
entry4_bg = canvas.create_image(
    842.0, 200.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    show="*",
    highlightthickness = 0)

entry4.place(
    x = 708, y = 182,
    width = 268,
    height = 34)

entry5_img = PhotoImage(file = f"Decrypt/img_textBox5.png")
entry5_bg = canvas.create_image(
    1156.5, 197.0,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#040404",
    show="*",
    fg = fgColour,
    highlightthickness = 0)

entry5.place(
    x = 1025, y = 179,
    width = 263,
    height = 34)

entry6_img = PhotoImage(file = f"Decrypt/img_textBox6.png")
entry6_bg = canvas.create_image(
    999.0, 546.0,
    image = entry6_img)

entry6 = Text(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

entry6.place(
    x = 709, y = 339,
    width = 580,
    height = 412)

img3 = PhotoImage(file = f"Decrypt/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = cc_dec,
    relief = "flat")

b3.place(
    x = 936, y = 262,
    width = 127,
    height = 36)

window.resizable(False, False)
window.mainloop()
