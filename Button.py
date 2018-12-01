import Tkinter as tk
# from PIL import Image

# from Graphics import Graphics
import paths


class Button(object):
    def __init__(self, master, line, col):
        self.line = line  # type: int
        self.col = col  # type: int
        self.used = ''  # type: str
        self.master=master

        self.btn = tk.Button(master=master, text='aafffffffffa', compound="center", command=self.click)
        self.__initialize_button()
        print self

    def __initialize_button(self):
        self.__change_image('white')
        self.btn.bind("<Enter>", lambda event: self.__change_image('X'))  # change '' to real sign
        self.btn.bind("<Leave>", lambda event: self.__change_image('white'))

    def __change_image(self, sign):
        img = tk.PhotoImage(file=paths.images[sign])
        print '{}, {}'.format(sign, paths.images[sign])
        self.btn.config(image=img)
        self.btn.image=img

    def click(self):
        print 'click!!'
        self.__change_image('')  ##### change according to the real sign !!!!!!!! (not only the user's sign)
        self.used = ''
        self.btn['command'] = 0  # Disable clicking
        self.btn['relief'] = 'sunken'  # Fix the design
        self.btn.bind("<Enter>", '')
        self.btn.bind("<Leave>", '')

    def grid(self):
        self.btn.grid(row=self.line, column=self.col)
        print 'grid: {}'.format(self)

    def __str__(self):
        return "{},{}".format(self.line, self.col)
