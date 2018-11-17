class Board(object):
    def __init__(self):
        self.__board = [['', '', ''], ['', '', ''], ['', '', '']]

    def __getitem__(self, pos_tuple):
        line, col = pos_tuple
        return self.__board[line][col]

    def __setitem__(self, pos_tuple, sign):
        line, col = pos_tuple
        self.__board[line][col] = sign

    def __chek_line(self, line):
        """
        Check if there is a winner in a given line.
        If there is, return the sign of the winner, else return an empty string
        :param line: The line to check. range: [0, 2]
        :type line: int
        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[line, 0]
        if sign_0 == '':
            return ''
        if sign_0 == self[line, 1] == self[line, 2]:
            return sign_0
        return ''

    def __chek_col(self, col):
        """
        Check if there is a winner in a given column.
        If there is, return the sign of the winner, else return an empty string
        :param col: The line to check. range: [0, 2]
        :type col: int
        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[0, col]
        if sign_0 == '':
            return ''
        if sign_0 == self[1, col] == self[2, col]:
            return sign_0
        return ''

    def __check_diagonal_1(self):
        """
        Check if there is a winner in the main diagonal.
        If there is, return the sign of the winner, else return an empty string
        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[0, 0]
        if sign_0 == '':
            return ''
        if sign_0 == self[1, 1] == self[2, 2]:
            return sign_0
        return ''

    def __check_diagonal_2(self):
        """
        Check if there is a winner in the secondary diagonal.
        If there is, return the sign of the winner, else return an empty string
        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        sign_0 = self[0, 2]
        if sign_0 == '':
            return ''
        if sign_0 == self[1, 1] == self[2, 0]:
            return sign_0
        return ''

    def check_winner(self):
        """
        Check if there is a winner in the whole board.
        If there is, return the sign of the winner, else return an empty string
        :return: If there is a winner, return his sign, else return an empty string
        :rtype: str
        """
        for line in xrange(3):
            sign = self.__chek_line(line)
            if sign != '':
                return sign
        for col in xrange(3):
            sign = self.__chek_col(col)
            if sign != '':
                return sign
        sign = self.__check_diagonal_1()
        if sign != '':
            return sign
        sign = self.__check_diagonal_2()
        if sign != '':
            return sign
        return ''
