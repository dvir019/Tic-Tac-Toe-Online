import Tkinter as tk
from PIL import Image

from Graphics import Graphics


class Button(object):
    def __init__(self, line, col):
        self.line = line  # type: int
        self.col = col  # type: int
        self.used = ''  # type: str
        img = tk.PhotoImage(file=Graphics.paths['white'])

        self.btn = tk.Button(master=Graphics().frame, image=img)
        self.btn.config(image=img)
        self.btn.image = img

    def __change_image(self, sign):
        img = tk.PhotoImage(file=Graphics.paths[sign])
        self.btn.config(image=img)

    def click(self):
        self.__change_image('')  ##### change according to the real sign !!!!!!!!
        self.used=''
        self.btn['command'] = 0  # Disable clicking
        self.btn['relief'] = 'sunken'  # Fix the design
