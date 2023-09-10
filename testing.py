import unittest
import re
from pdf_to_text import GetVectors

vector = GetVectors('B02.061.002', 'B02.110.002')
with open('test_list.txt', 'r') as test:
    test_files = test.readlines()
path, lst = [], []
for i in test_files:
    path += [i.split()[0]]
    lst += [list(map(float, i.split()[1:]))]
for key, value in enumerate(path):
    assert vector.get_vectors(path[key])[0] == lst[key]


# class TestDataBlood(unittest.TestCase):
#     def test_rle(self):
#         self.assertEqual(1, 1)
#
#     # def test_data(self, l1, l2):
#     #     self.assertEqual(l1, l2)
#
#
# if __name__ == "__main__":
#     pass
#     # unittest.main()
