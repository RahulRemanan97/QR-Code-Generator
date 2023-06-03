#importing modules..
import qrcode, PIL 
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk,messagebox,filedialog

#functions for qrcode
def createQR(*args):
    data = entry.get()
    if data:
        im = qrcode.make(data)
        img = ImageTk.PhotoImage(im)
        qr_canvas.delete("all")
        qr_canvas.create_image(0,0,anchor=tk.NW,image=img)
        qr_canvas.image = img
    else:
        messagebox.showerror("Error","Enter any data first!")

def saveQR(*args):
    data = entry.get()
    if data:
        img = qrcode.make(data)
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            img.save(path)
            messagebox.showinfo("Success","QR code is saved.")
    else:
        messagebox.showerror("Error","Enter any data first!")


# code for GUI
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("320x400")
root.config(bg="whitesmoke")

frame1 = tk.Frame(root,bd=2,relief=tk.RAISED,width=300,height=290)
frame1.place(x=10,y=0)
frame2 = tk.Frame(root,bd=2,relief=tk.FLAT,width=300,height=100)
frame2.place(x=10,y=300)

cover_img = ImageTk.PhotoImage(Image.open("qr-img-3.png"))

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW,image=cover_img)
qr_canvas.bind("<Double-1>",saveQR)
qr_canvas.pack(fill=tk.BOTH)

entry = ttk.Entry(frame2,width=35,font=("arial",11),justify=tk.CENTER)
entry.place(x=5,y=5)
entry.bind("<Return>",createQR)

but1 = ttk.Button(frame2,text="Create",width=10,command=createQR)
but1.place(x=15,y=50)
but2 = ttk.Button(frame2,text="Save",width=10,command=saveQR)
but2.place(x=100,y=50)
but3 = ttk.Button(frame2,text="Exit",width=10,command=root.quit)
but3.place(x=180,y=50)

root.mainloop()