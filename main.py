# coding=utf-8
from pprint import pprint
class world:
    def __init__(self, width, height, debug=False):
        self.debug = debug
        self.width = width
        self.height = height
        self.size = width * height
        self.area = height * [width * ['#']]
        self.pretty_text = None
        self.pretty_text = self.pretty()
        if self.debug: print("Initilazed area is:\n" + self.pretty())

    def pretty(self):
        if self.pretty_text == None:
            temp = ""
            for i in self.area:
                for j in i:
                    temp += f" {j} "
                temp += "\n"
            self.pretty_text = temp
        return self.pretty_text

    def start(self, x, y):
        self.pretty_text = None
        self.area[x][y] = 'X'
        if self.debug: print("Initilazed area is:\n" + self.pretty())
my_test = world(10, 6, True)
my_test.start(2, 3)
