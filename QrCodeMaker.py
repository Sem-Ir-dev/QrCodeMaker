import qrcode
from tkinter import *

blue = '#8398E3'
white = '#fff'
black = '#000'


def qcode():
    text = tx_poly.get('1.0', 'end')
    name = name_poly.get()
    image = qrcode.make(text)
    image.save(str(name) + '.png')


window = Tk()
window.title('QrCodeMaker')
window.geometry('350x330+480+200')
window.iconbitmap('scanner.ico')
window.resizable(False, False)
window['bg'] = white

lb0 = Label(window, text='Enter the text to encrypt:', fg=black, bg=white, font=('Arial', 12))
lb0.pack()

tx_poly = Text(window, width=30, bd=1, height=10, fg=black, font='Arial', bg=white, wrap=WORD)
tx_poly.pack()

lb1 = Label(window, text='Enter file name:', fg=black, bg=white, font=('Arial', 12))
lb1.pack()

name_poly = Entry(window, width=30, bd=1, fg=black, font='Arial', bg=white)
name_poly.pack()

but = Button(window, text='Encrypt', bd=0, fg=white, width=12, height=2, bg=blue, command=qcode)
but.place(x=132, y=270)

window.mainloop()
