import Tkinter as tk


class Graphics(object):
    paths = {'X': 'X.gif',
             'O': 'O.gif',
             'white': 'white.gif'}  # type: dict[str:str]
    __master_window = None
    __menu_frame = None
    __board__frame = None

    @classmethod
    def initialize(cls):
        cls.__master_window = tk.Tk()
        # cls.__master_window.withdraw()
        # cls.__master_window = tk.Tk()
        cls.__master_window.title('Tic Tac Toe')
        cls.__master_window.geometry("500x500")  # Window size
        cls.__master_window.resizable(0, 0)  # Don't allow resizing in the x or y direction

        cls.__menu_frame = tk.Frame(master=cls.__master_window, background='red')
        # cls.__menu_frame.pack(fill=tk.BOTH, expand=1)
        cls.__menu_frame.grid(row=0, column=0)

        cls.__menu_frame.pack(fill=tk.BOTH, expand=1)
        cls.__board__frame = tk.Frame(master=cls.__master_window, background='green')

    @classmethod
    def __set_menu(cls):
        btn = tk.Button(master=cls.__menu_frame, text='next', command=cls.__show_next)
        btn.grid(row=0, column=0)

    @classmethod
    def __show_next(cls):
        print 'show'
        # cls.__board__frame.pack(fill=tk.BOTH, expand=1)
        cls.__board__frame.grid(row=0, column=0)
        cls.__board__frame.pack(fill=tk.BOTH, expand=1)
        cls.__menu_frame.grid_remove()
        cls.__menu_frame.pack_forget()
        tk.Button(master=cls.__board__frame, width=3).grid(row=0, column=0)
        # cls.__board__frame.grid(row=0, column=0, sticky=tk.NSEW)
        cls.__board__frame.tkraise()

    @classmethod
    def get_board_frame(cls):
        return cls.__board__frame

    @classmethod
    def run(cls):
        cls.initialize()
        cls.__set_menu()
        # cls.__menu_frame.tkraise()
        cls.__master_window.mainloop()


if __name__ == '__main__':
    Graphics.run()

    # __instance = None
    # paths = {'X': 'X.gif',
    #          'O': 'O.gif',
    #          'white': 'white.gif'}  # type: dict[str:str]
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super(Graphics, cls).__new__(cls)
    #     return cls.__instance
    #
    # def __init__(self):
    #     self.__master_window = tk.Tk()
    #     self.__master_window.title('Tic Tac Toe')
    #     self.__master_window.geometry("500x500")  # Window size
    #     self.__master_window.resizable(0, 0)  # Don't allow resizing in the x or y direction
    #     self.__frame = tk.Frame(master=self.__master_window)
    #     self.__frame.pack(fill=tk.BOTH, expand=1)
    #
    # @property
    # def frame(self):
    #     return self.__frame
    #
    # def run(self):
    #     self.__master_window.mainloop()

# If you have a large number of widgets, like it looks like you will for your
# game you can specify the attributes for all widgets simply like this.
# mw.option_add("*Button.Background", "black")
# mw.option_add("*Button.Foreground", "red")


# You can set the geometry attribute to change the root windows size
# You want the size of the app to be 500x500
# Don't allow resizing in the x or y direction


# __frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
# Expand the frame to fill the root window

# Changed variables so you don't have these set to None from .pack()
# ph=tk.PhotoImage(file="X.gif")
# go = tk.Button(master=back, command=startgame, height=10, width=20)
# # go.config(image=ph)
# # go.image=ph
# go.bind("<Enter>", lambda btn: startgame(btn, 'X.gif'))
# go.bind("<Leave>", lambda btn: startgame(btn, ''))
# go.grid(row=0, column=0)
# close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
# close.grid(row=0, column=1)
# close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
# close.grid(row=0, column=2)
# go2 = tk.Button(master=back, text='Start Game', command=startgame, height=10, width=20)
# go2.grid(row=1, column=0)
# close2 = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
# close2.grid(row=1, column=1)
# close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
# close.grid(row=1, column=2)
#
# close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
# close.grid(row=2, column=0)
# close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
# close.grid(row=2, column=1)
# close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
# close.grid(row=2, column=2)
# print dir(close)
# # info = tk.Label(master=__frame, text='Made by me!', bg='red', fg='black')
#
#
# mw.mainloop()
