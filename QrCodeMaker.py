import qrcode
from tkinter import *

bg_input = '#D3DEA4'
bg_button = '#CBDE77'
bg_back = '#E1E6E2'
fg_color = '#2D2D2F'


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
window['bg'] = bg_back

lb0 = Label(window, text='Enter the text to encrypt:', fg=fg_color, bg=bg_back, font=('Arial', 12))
lb0.pack()

tx_poly = Text(window, width=30, bd=1, height=10, fg=fg_color, font='Arial', bg=bg_input, wrap=WORD)
tx_poly.pack()

lb1 = Label(window, text='Enter file name:', fg=fg_color, bg=bg_back, font=('Arial', 12))
lb1.pack()

name_poly = Entry(window, width=30, bd=1, fg=fg_color, font='Arial', bg=bg_input)
name_poly.pack()

but = Button(window, text='Encrypt', bd=1, fg=fg_color, width=12, height=2, bg=bg_button, command=qcode)
but.place(x=132, y=270)

window.mainloop()
