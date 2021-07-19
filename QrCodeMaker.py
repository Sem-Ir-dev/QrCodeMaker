import qrcode
from tkinter import *

# TODO: написать комментарии
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
window['bg'] = '#868686'

lb0 = Label(window, text='Введите текст для шифрования:', bg='#868686', font=('Arial', 12))
lb0.pack()

tx_poly = Text(window, width=30, height=10, font='Arial', bg='#4C4C4C', fg='white', wrap=WORD)
tx_poly.pack()

lb1 = Label(window, text='Введите название файла:', bg='#868686', font=('Arial', 12))
lb1.pack()

name_poly = Entry(window, width=30, font='Arial', bg='#4C4C4C', fg='white')
name_poly.pack()

but = Button(window, text='Шифровать', width=10, height=2, bg='#999999', command=qcode)
but.pack()

window.mainloop()
