import os
import sys
from pprint import pprint


class Walker:
    def __init__(self, path, top, file=None):
        self.path = path
        self.top = top
        self.file = None

    def get_files(self):
        for root, dirs, files in os.walk(self.top, topdown=False):
            self.file = (root, dirs, files)
        return [self.path + '/' + self.file[0] + '/' + i for i in self.file[2]]


if __name__ == '__main__':
    ex = Walker(sys.path[0], 'store_txt')
    print(ex.get_files())

