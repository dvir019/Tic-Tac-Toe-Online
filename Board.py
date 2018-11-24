from Button import Button


class Board(object):
    def __init__(self, size=3):
        self.__board = [[Button(j, i) for i in xrange(size)] for j in xrange(size)]  # type: list[list[Button]]
        self.__size = size  # type: int

    def __getitem__(self, pos_tuple):
        line, col = pos_tuple
        return self.__board[line][col]

    def __setitem__(self, pos_tuple, sign):
        line, col = pos_tuple
        self.__board[line][col] = sign

    def __check_line(self, line):
        """
        Check if there is a winner in a given line.
        If there is, return the sign of the winner, else return an empty string.

        :param line: The line to check. range: [0, 2]
        :type line: int

        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[line, 0]
        if sign_0 == '':
            return ''
        for col in xrange(1, self.__size):
            temp_sign = self[line, col]
            if temp_sign == '' or temp_sign != sign_0:
                return ''
        return sign_0

    def __check_col(self, col):
        """
        Check if there is a winner in a given column.
        If there is, return the sign of the winner, else return an empty string.

        :param col: The line to check. range: [0, 2]
        :type col: int

        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[0, col]
        if sign_0 == '':
            return ''
        for line in xrange(1, self.__size):
            temp_sign = self[line, col]
            if temp_sign == '' or temp_sign != sign_0:
                return ''
        return sign_0

    def __check_diagonal_1(self):
        """
        Check if there is a winner in the main diagonal.
        If there is, return the sign of the winner, else return an empty string.

        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[0, 0]
        if sign_0 == '':
            return ''
        for index in xrange(1, self.__size):
            temp_sign = self[index, index]
            if temp_sign == '' or temp_sign != sign_0:
                return ''
        return sign_0

    def __check_diagonal_2(self):
        """
        Check if there is a winner in the secondary diagonal.
        If there is, return the sign of the winner, else return an empty string.

        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[0, self.__size - 1]
        if sign_0 == '':
            return ''
        for index in xrange(1, self.__size):
            temp_sign = self[index, self.__size - 1 - index]
            if temp_sign == '' or temp_sign != sign_0:
                return ''
        return sign_0

    def check_winner(self):
        """
        Check if there is a winner in the whole board.
        If there is, return the sign of the winner, else return an empty string.

        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        for line in xrange(3):
            sign = self.__check_line(line)
            if sign != '':
                return sign
        for col in xrange(3):
            sign = self.__check_col(col)
            if sign != '':
                return sign
        sign = self.__check_diagonal_1()
        if sign != '':
            return sign
        sign = self.__check_diagonal_2()
        if sign != '':
            return sign
        return ''

    def check_full(self):
        """
        Check if the board is full.
        :return: True if the board is full, else False
        :rtype: bool
        """
        for row in xrange(self.__size):
            for col in xrange(self.__size):
                if self[row, col].used=='':
                    return False
        return True


import Tkinter as tk

# class App(tk.Frame, object):
#     def __init__(self, master=None):
#         super(App, self).__init__(master)
#         self.pack()
x = False


def startgame(btn, path, stop=False):
    global x
    if path == '':
        go.config(image='', height=10, width=20)
    else:
        print stop
        if not stop and not x:
            print 'ddd'
            ph = tk.PhotoImage(file=path)
            go.config(image=ph)
            go.image = ph
        elif not x:
            go['command'] = 0
            go['relief'] = 'sunken'
            print 'aaaa'
            x = True
            go.bind("<Enter>", '')
            go.bind("<Leave>", '')
            # import tkMessageBox
            # tkMessageBox.showinfo("Title", "a Tk MessageBox", master=mw)
            another = tk.Frame(master=mw, background='green', height=10, width=10)
            # __frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
            another.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window
            another.grid(row=0, column=0, sticky=tk.NSEW)
            x=tk.Button(master=another, text='aaa', command=mw.destroy)
            x.grid(row=0, column=0)
            another.tkraise()
            # back.grid_remove()
            # back.pack_forget()
            # another.pack_forget()
            # another.tkraise()
            # back.tkraise()




# flat, groove, raised, ridge, solid, or sunken
def change():
    a.grid(row=0, column=0)
    i = 0
    import time
    while True:
        a.config(text='\n\naaa'+'.'*i+' '*(3-i))
        i+=1
        if i==4:
            i=0
        time.sleep(0.5)


if __name__ == '__main__':
    mw = tk.Tk()

    # If you have a large number of widgets, like it looks like you will for your
    # game you can specify the attributes for all widgets simply like this.
    # mw.option_add("*Button.Background", "black")
    # mw.option_add("*Button.Foreground", "red")

    mw.title('The game')
    # You can set the geometry attribute to change the root windows size
    # mw.geometry("500x500")  # You want the size of the app to be 500x500

    window_height = 500
    window_width = 455

    screen_width = mw.winfo_screenwidth()
    screen_height = mw.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    mw.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    mw.resizable(0, 0)  # Don't allow resizing in the x or y direction

    back = tk.Frame(master=mw)
    # __frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
    back.grid(row=0, column=0)
    back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window
    back.grid(row=0, column=0, sticky=tk.NSEW)

    # Changed variables so you don't have these set to None from .pack()
    ph = tk.PhotoImage(file="white.gif")
    go = tk.Button(master=back, command=lambda: startgame(go, 'X.gif', True))
    go.config(image=ph)
    go.image = ph
    # x=False
    go.bind("<Enter>", lambda btn: startgame(btn, 'X.gif'))
    go.bind("<Leave>", lambda btn: startgame(btn, 'white.gif'))
    go.grid(row=1, column=0)
    close = tk.Button(master=back)  # , text='aa', compound="center")
    ph2 = tk.PhotoImage(file="O.gif")
    close.config(image=ph2)
    go.image = ph
    close.grid(row=1, column=1)
    close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
    close.grid(row=1, column=2)

    import threading
    th=threading.Thread(target=change)

    go2 = tk.Button(master=back, text='Start Game', command=th.start, height=10, width=20)
    go2.grid(row=2, column=0)
    close2 = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
    close2.grid(row=2, column=1)
    close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
    close.grid(row=2, column=2)

    close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
    close.grid(row=3, column=0)
    close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
    close.grid(row=3, column=1)
    close = tk.Button(master=back, text='Quit', command=mw.destroy, height=10, width=20)
    close.grid(row=3, column=2)
    print dir(close)
    info = tk.Label(master=back, text='Made by me!', bg='red', fg='black', width=30)
    info.grid(row=0, column=0, columnspan=3)

    lst=["arrow",
         "circle",
         "clock",
         "cross",
         "dotbox",
         "exchange",
         "fleur",
         "heart",
         "heart",
         "man",
         "mouse",
         "pirate",
         "plus",
         "shuttle",
         "sizing",
         "spider",
         "spraycan",
         "star",
         "target",
         "tcross",
         "trek",
         "watch"]
    i=21
    # x=tk.Toplevel(master=mw, height=1000, width=1000, background='red', cursor=lst[i])
    # print lst[i]
    # x.title('')
    # # x.attributes('-topmost', True)
    # x.geometry("{}x{}+{}+{}".format(300, 100, int((screen_width / 2) - (300 / 2)),
    #                                 int((screen_height / 2) - (100 / 2))))
    # # x.attributes('-disabled', True)
    # x.transient(mw)
    p=tk.PhotoImage(file='C:\Users\Horim\Desktop\win.gif')
    a=tk.Label(master=mw, text='\n\naa', compound="center", relief="solid", borderwidth=.556)
    a.config(image=p)
    # a.grid(row=0, column=0)
    # back.config(state=tk.DISABLED)
    for w in back.winfo_children():
        if w['text']!='Start Game':
            w.config(state=tk.DISABLED)
    # x.destroy()
    # x.overrideredirect(1)
    # import tkSimpleDialog
    # aa=tkSimpleDialog.Dialog(mw)
    # mw.overrideredirect(1)
    #
    #
    # def movewindow(event):
    #     mw.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    # mw.bind('', movewindow)
    # z=tk.Label(master=mw, text='aaa', height=10, width=10, background='cyan').grid(row=0, column=0)

    mw.mainloop()




