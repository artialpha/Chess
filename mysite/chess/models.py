import itertools

from django.db import models


class ChessOpening(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    eco = models.CharField(max_length=200)
    epd = models.CharField(max_length=200, default="null")
    algebraic_notation = models.CharField(max_length=200, default="null")

    @classmethod
    def translate(cls, char):
        if char == 'k':
            return '♚'
        if char == 'q':
            return '♛'
        if char == 'r':
            return '♜'
        if char == 'b':
            return '♝'
        if char == 'n':
            return '♞'
        if char == 'p':
            return '♟'

        if char == 'K':
            return '♔'
        if char == 'Q':
            return '♕'
        if char == 'R':
            return '♖'
        if char == 'B':
            return '♗'
        if char == 'N':
            return '♘'
        if char == 'P':
            return '♙'

    @classmethod
    def get_position(cls, string, line):
        uni = 97
        index = 0
        list_out = []
        for char in string:
            # print(char)
            if char.isdigit():
                index += int(char)
            else:
                list_out.append((chr(index + uni), line, cls.translate(char)))
                index += 1 if index < 8 else index
        return list_out

    @staticmethod
    def chess_dictionary(mylist):
        dictionary = {}
        for i in mylist:
            # print(i)
            dictionary[i[0].capitalize() + str(i[1])] = i[2]
        return dictionary

    @classmethod
    def create_chess_board(cls, epd):
        mylist = []
        for index, line in enumerate(epd.split('/')):
            mylist.append(cls.get_position(line, 8 - index))
        mylist = cls.chess_dictionary(itertools.chain.from_iterable(mylist))
        return mylist

    @classmethod
    def start_position(cls):
        return cls.create_chess_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    def number_to_algebraic(self):
        alg_with_numbers = self.algebraic_notation.split(" ")
        alg_with_numbers = [str(i+1)+". "+e for i,e in enumerate(alg_with_numbers)]
        return alg_with_numbers




class Variant(models.Model):
    chess_opening = models.ForeignKey(ChessOpening, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    moves = models.TextField()
    number = models.DecimalField(decimal_places=0, max_digits=2)
    description = models.TextField(blank=True)
