from tkinter import *
from tkinter import filedialog
import sys
import os
import Caesar_Cipher as cs
import steg as stg
from PIL import Image,ImageTk


def test():
    os.system('python hi.py')

plain_Text = " "
cipherText = ""

def cs_encrypt():
    #tb2 = out_name.get()
    kb6 = int(key_TF.get())
    tb7 = int(loop_TF.get())
    global plain_Text
    for i in range(tb7) :
        ct = cs.cs_encrypt(plain_Text,kb6)
        plain_Text = ct
        print(plain_Text)
        
        #preview.insert(END,"\n\nIteration 0"+k+"\n"+ct)

    #print(plain_Text,kb6,ct)
    global cipherText 
    cipherText = ct
    preview.insert(END,"\n\nCiphertext :\n"+cipherText)

def back_btn_clicked():
    window.destroy()
    os.system('python main.py')
    #print("Button Clicked")

def pt_src_btn_clicked():
    filename = filedialog.askopenfilename(
                                        title = "Select a File",
                                        filetypes = (("Text files",
                                                        "*.txt*"),
                                                    ("all files",
                                                        "*.*")))
        
    # Change label contents
    pt_textBox.insert(0,filename)
    f = open(filename, "r")
    global plain_Text 
    plain_Text = f.read()
    pt= "Plain Text :\n" + plain_Text
    #tb2 = out_name.get()
    #tb6 = key_TF.get()
    #tb7 = loop_TF.get()
    preview.insert(END,pt)
    #print(filename,"\nOut Name:",tb2,"\nKey:",tb6,"\nLoop Value:",tb7)


def img_src_btn_clicked():
    yourImage=filedialog.askopenfilename(title = "Select your image",filetypes = [("Image Files","*.png"),("Image Files","*.jpg")])
    img_textBox.insert(END,yourImage)
    global my_image
    img = Image.open(yourImage)
    img = img.resize((267,145), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(img)
    pr.image_create(END, image=my_image)

def stg_encrypt():
    img1 = img_textBox.get()
    out= "C:/Users/Sarvesh/Desktop/test 02/Testing multiple windows/Main/Output/"+out_name.get()
    #print(out)
    stg.encode(cipherText,img1,out)
    #preview2.insert(END,"\n\nCiphertext :\n"+cipherText)
    global my_image4
    img3 = Image.open(out)
    img3 = img3.resize((580,412), Image.ANTIALIAS)
    my_image4 = ImageTk.PhotoImage(img3)
    preview2.image_create(END, image=my_image4)

def btn_clicked():
    print("Button Clicked")

fgColour = "white"

window = Tk()

window.title("Encryption")
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

background_img = PhotoImage(file = f"Encrypt/background.png")
background = canvas.create_image(
    695.5, 396.0,
    image=background_img)

entry0_img = PhotoImage(file = f"Encrypt/img_textBox0.png")
entry0_bg = canvas.create_image(
    260.0, 112.0,
    image = entry0_img)

pt_textBox = Entry(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

pt_textBox.place(
    x = 42, y = 94,
    width = 436,
    height = 34)

entry1_img = PhotoImage(file = f"Encrypt/img_textBox1.png")
entry1_bg = canvas.create_image(
    919.0, 112.0,
    image = entry1_img)

img_textBox = Entry(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

img_textBox.place(
    x = 701, y = 94,
    width = 436,
    height = 34)

entry2_img = PhotoImage(file = f"Encrypt/img_textBox2.png")
entry2_bg = canvas.create_image(
    849.0, 199.0,
    image = entry2_img)

out_name = Entry(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

out_name.place(
    x = 702, y = 181,
    width = 294,
    height = 34)

entry3_img = PhotoImage(file = f"Encrypt/img_textBox3.png")
entry3_bg = canvas.create_image(
    333.0, 546.0,
    image = entry3_img)

preview = Text(
    wrap='word',
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

preview.place(
    x = 43, y = 339,
    width = 580,
    height = 412)

entry4_img = PhotoImage(file = f"Encrypt/img_textBox4.png")
entry4_bg = canvas.create_image(
    997.0, 542.0,
    image = entry4_img)

preview2 = Text(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

preview2.place(
    x = 707, y = 335,
    width = 580,
    height = 412)

entry5_img = PhotoImage(file = f"Encrypt/img_textBox5.png")
entry5_bg = canvas.create_image(
    1153.5, 224.5,
    image = entry5_img)

pr = Text(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

pr.place(
    x = 1020, y = 151,
    width = 267,
    height = 145)

entry6_img = PhotoImage(file = f"Encrypt/img_textBox6.png")
entry6_bg = canvas.create_image(
    176.0, 200.0,
    image = entry6_img)

key_TF = Entry(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

key_TF.place(
    x = 42, y = 182,
    width = 268,
    height = 34)

entry7_img = PhotoImage(file = f"Encrypt/img_textBox7.png")
entry7_bg = canvas.create_image(
    490.5, 197.0,
    image = entry7_img)

loop_TF = Entry(
    bd = 0,
    bg = "#040404",
    fg = fgColour,
    highlightthickness = 0)

loop_TF.place(
    x = 359, y = 179,
    width = 263,
    height = 34)

img0 = PhotoImage(file = f"Encrypt/img0.png")
pt_browse_btn = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = pt_src_btn_clicked,
    relief = "flat")

pt_browse_btn .place(
    x = 495, y = 94,
    width = 127,
    height = 36)

img1 = PhotoImage(file = f"Encrypt/img1.png")
img_browse_btn = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = img_src_btn_clicked,
    relief = "flat")

img_browse_btn.place(
    x = 1160, y = 94,
    width = 127,
    height = 36)

img2 = PhotoImage(file = f"Encrypt/img2.png")
encrypt1 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = cs_encrypt,
    relief = "flat")

encrypt1.place(
    x = 267, y = 262,
    width = 127,
    height = 36)

img3 = PhotoImage(file = f"Encrypt/img3.png")
encrypt2 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = stg_encrypt,
    relief = "flat")

encrypt2.place(
    x = 795, y = 262,
    width = 127,
    height = 36)

img4 = PhotoImage(file = f"Encrypt/img4.png")
back_btn = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = back_btn_clicked,
    relief = "flat")

back_btn.place(
    x = 1182, y = 4,
    width = 127,
    height = 36)

window.resizable(False, False)
window.mainloop()
