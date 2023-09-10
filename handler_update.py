import sys

import csv

from pdf_to_text import GetVectors

from walks import Walker

files = Walker(sys.path[0], 'store_pdf')

with open('heads.txt', 'r') as heads:
    h = heads.read().split()

with open('names.csv', 'a', newline='') as csvfile:
    fieldnames, dic = h, {}
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    get_result = GetVectors('B02.061.002', 'B02.110.002')
    writer.writeheader()
    for f in files.get_files():
        r = get_result.get_vectors(f)
        dic = dict(zip(h, r[0]))
        dic.update({'file':f})
        try:
            writer.writerow(dic)
        except:
            print(f)



