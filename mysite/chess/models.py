import itertools

from django.db import models


class ChessOpening(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    eco = models.CharField(max_length=200)
    epd = models.CharField(max_length=200, default="null")
    algebraic_notation = models.CharField(max_length=200, default="null")

    def translate(self, char):
        if char == 'k':
            return '&#9818;'
        if char == 'q':
            return '&#9819;'
        if char == 'r':
            return '&#9820;'
        if char == 'b':
            return '&#9821;'
        if char == 'n':
            return '&#9822;'
        if char == 'p':
            return '&#9823;'

        if char == 'K':
            return '&#9812;'
        if char == 'Q':
            return '&#9813;'
        if char == 'R':
            return '&#9814;'
        if char == 'B':
            return '&#9815;'
        if char == 'N':
            return '&#9816;'
        if char == 'P':
            return '&#9817;'

    def get_position(self, string, line):
        uni = 97
        index = 0
        list_out = []
        for char in string:
            # print(char)
            if char.isdigit():
                index += int(char)
            else:
                list_out.append((chr(index + uni), line, self.translate(char)))
                index += 1 if index < 8 else index
        return list_out

    def chess_dictionary(self, mylist):
        dictionary = {}
        for i in mylist:
            # print(i)
            dictionary[i[0].capitalize() + str(i[1])] = i[2]
        return dictionary

    def create_chess_board(self):
        mylist = []
        for index, line in enumerate(self.epd.split('/')):
            mylist.append(self.get_position(line, 8 - index))
        mylist = self.chess_dictionary(itertools.chain.from_iterable(mylist))
        return mylist




class Variant(models.Model):
    chess_opening = models.ForeignKey(ChessOpening, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    moves = models.TextField()
    number = models.DecimalField(decimal_places=0, max_digits=2)
    description = models.TextField(blank=True)
