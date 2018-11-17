class Board(object):
    def __init__(self, size=3):
        self.__board = [['' for i in xrange(size)] for j in xrange(size)]  # type: list[list[str]]
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
