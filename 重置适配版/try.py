# from PySide6.QtWidgets import QApplication, QDialog
# from MainWIndow import Ui_Dialog
# import sys

# class MainInputMas(Ui_Dialog,QDialog):
#     def __init__(self): 
#         self.setupUi(self)
#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainInput = MainInputMas()
#     sys.exit(app.exec())


# Copyright (c) 2017-7-21 ZhengPeng All rights reserved.
number = None
def pop_up_box():
    num = None
    import tkinter
    from tkinter import Text,INSERT,END
    def inputint():
        nonlocal num
        global number
        if len(var.get().strip()) < 1 or type(var.get().strip()) != int or var.get().strip().isdisgit() == False:
            text = Text(root, width=50, height=30, undo=True, autoseparators=False)
            text.pack()
            text.insert(INSERT, '输入错误或为空')
        try:
            num = int(var.get().strip())
            root.destroy()
            number = num
        except:
            var.set('')
            num = False
    def inputclear():
        nonlocal num
        var.set('')
        num = 0
    root = tkinter.Tk(className='班级人数输入')
    root.geometry('270x100')
    var = tkinter.StringVar()
    var.set('请输入班级人数')
    entry1 = tkinter.Entry(root, textvariable=var)
    entry1.pack()
    btn1 = tkinter.Button(root, text='确认', command=inputint)
    btn2 = tkinter.Button(root, text='清除', command=inputclear)
    btn2.pack(side='right')
    btn1.pack(side='right')
    root.mainloop()
pop_up_box()
print(number)