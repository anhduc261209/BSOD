
# importing tkinter for gui
from tkinter import *
from PIL import ImageTk, Image
import os, sys, webbrowser, time
from tkinter.messagebox import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def open():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(5)
    choice = askyesno("Blue Screen Of Fu*k", "Do you want to escape or not:)?")
    if choice:
        showinfo("Blue Screen Of Fu*k", "Ya-Yamete kudasai\nOK, I will let you die:)")
    else:
        showinfo("Blue Screen Of Fu*k", "ara ara~\nOK, time to escape")
        sys.exit()

time_left = 30

# creating window
window = Tk()
 
# setting attribute
window.attributes('-fullscreen', True)
window.title("Blue Screen Of Death")
window.configure(bg='#0723DB')
window.iconbitmap(os.path.join(resource_path(""), "smile.ico"))

lbl1 = Label(window, text = "\n   :))))", font = ("Segoe UI", 70), fg = "white", bg = "#0723DB", anchor = "nw")
lbl1.pack(fill='both')

lbl2 = Label(window, text = "     Your computer has been fucked by Anh Duc", font = ("Segoe UI", 30), fg = "white", bg = "#0723DB", anchor = "nw")
lbl2.pack(fill='both')

lbl3 = Label(window, text = "     You can't yamete kudasai this window", font = ("Segoe UI", 30), fg = "white", bg = "#0723DB", anchor = "nw")
lbl3.pack(fill='both')

troubleshoot_frame = Frame(window, bg='#0723DB')
troubleshoot_frame.pack(fill='both')

qr_code_img = ImageTk.PhotoImage(Image.open(os.path.join(resource_path(""), "qr_code.png")).resize((150, 175), Image.ANTIALIAS))
qr_code_lbl = Label(troubleshoot_frame, image = qr_code_img, anchor = 'nw', bg = "#0723DB")
qr_code_lbl.grid(row = 0, column = 0, rowspan = 2, padx = 40)

lbl4 = Label(troubleshoot_frame, text="For more information about this, please visit our website: https://dontopenthiswebsite.glitch.me", font = ("Segoe UI", 10), fg = "white", bg = "#0723DB", anchor = "nw")
lbl4.grid(row = 0, column = 1, padx = 0, pady = 0)

btn = Button(window, text="Click here to fix the issue", fg = "white", bg = "green", anchor = "nw", font = ("Segoe UI", 15), command = open)
btn.pack()

window.mainloop()
