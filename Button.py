import Tkinter as tk
# from PIL import Image

from Graphics import Graphics


class Button(object):
    def __init__(self, line, col):
        self.line = line  # type: int
        self.col = col  # type: int
        self.used = ''  # type: str

        self.btn = tk.Button(master=Graphics().frame)
        self.__initialize_button()

    def __initialize_button(self):
        self.__change_image('white')
        self.btn.bind("<Enter>", lambda: self.__change_image())  # change '' to real sign
        self.btn.bind("<Leave>", lambda: self.__change_image('white'))

    def __change_image(self, sign):
        img = tk.PhotoImage(file=Graphics.paths[sign])
        self.btn.config(image=img)

    def click(self):
        self.__change_image('')  ##### change according to the real sign !!!!!!!! (not only the user's sign)
        self.used = ''
        self.btn['command'] = 0  # Disable clicking
        self.btn['relief'] = 'sunken'  # Fix the design
        self.btn.bind("<Enter>", '')
        self.btn.bind("<Leave>", '')

    def grid(self):
        self.btn.grid(row=self.line, column=self.col)

    def __str__(self):
        return "{},{}".format(self.line, self.col)
