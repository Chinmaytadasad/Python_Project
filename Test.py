import qrcode
import resize
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

app = Tk()

app.title("QR Code Generator")
app.geometry("500x500")

obj = resize.Resize(app)
obj.pack(fill=BOTH, expand=YES)




def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(app, text='File Saved!', bg='Blue', fg='black', font=('Arial Black', 8)).pack()
    messagebox.showinfo("Done", "Your QrCode Generated Successfully!")


def show():
    img = qrcode.make(msg.get())
    type(img)
    img.show()


Label(app, text='Enter the Text or URL : ', font=('Arial Black', 16),
      bg='White').place(x=50, y=80)
msg = Entry(app,width=35,font=('Arial 15'))
msg.place(x=50, y=140)


Label(app, text='File Name(Save As) : ', font=('Arial Black', 16),
      bg='White').place(x=50, y=240)

save_name = Entry(app,width=35,font=('Arial 15'))
save_name.place(x=50, y=300)

btn = Button(app, text='Save QR code', command=generate, bd='5', width=20,font=('Arial 15'))
btn.place(x=50, y=380)

# Create an infinite loop for
# displaying app on screen
app.mainloop()
