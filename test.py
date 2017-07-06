# import tkinter as tk
# import barcode
# from barcode.writer import ImageWriter
# from hubarcode.code128 import Code128Encoder
#
#
# window = tk.Tk()
# window.title('BARCODE_V1')
# window.geometry('400x550')
#
#
# for lf in ['red','blue','yellow']:
#     #可以使用text属性指定Frame的title
#     tk.LabelFrame(height = 200,width = 300,text = lf, bg = lf).pack()
# def show_barcode():
#     # encoder = Code128Encoder('CJF 202423')
#     # encoder.save("test.png")
#     ean = barcode.get('ean13', '275402423', writer=ImageWriter())
#     filename = ean.save('test')
# show_barcode()
# window.mainloop()

from tkinter import *

master = Tk()

v = StringVar()


def test(content, reason, name):
    if content == "123":
        print("正确！")
        print(content, reason, name)
        return True
    else:
        print("错误！")
        print(content, reason, name)
        return True


testCMD = master.register(test)
e1 = Entry(master, textvariable=v, validate="key", validatecommand=(testCMD, '%P', '%v', '%W'))
e2 = Entry(master)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

mainloop()