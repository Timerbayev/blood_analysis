# importing required modules
import re
import PyPDF2
from datetime import datetime, date


class GetVectors:
    def __init__(self, *args):
        self.array = args

    def get_text(self, file, index=0):
        pdf_fileobj = open(file, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_fileobj)
        pageobj = pdf_reader.pages[index]
        return pageobj.extract_text()

    @staticmethod
    def get_sex(texts):
        sex = [i.split()[0] for i in texts.split('\n') if re.findall('Пол', i)][0]
        return 1 if sex == 'м' else 0 if sex == 'ж' else 2

    @staticmethod
    def get_age(files):
        d = files.split('/')[-1].split('.')[0]
        slices = f"{d[:2]} {d[2:4]} {d[4:6]}"
        age = f"20{slices}" if d.startswith('0') else f"19{slices}"
        lst = list(map(int, age.split()))
        return str((date.today() - date(*lst)) // 365).split()[0]

    def get_list(self, file):
        start, lst = None, []
        text = self.get_text(file)
        lst.append([self.get_sex(text)])
        lst.append([self.get_age(file)])
        for key, value in enumerate(text.split('\n')):
            if value.split()[0] == self.array[0]:  # 'B02.061.002':
                start = key
        for i in text.split('\n')[start:]:
            if i.startswith(self.array[0]) or i.startswith(self.array[1]):  # 'B02.110.002'
                continue
            else:
                lst.append(' '.join(re.findall('\d*\.*\d*|\d*', i)).strip().split())

        if len(list(map(float, [i[0] for i in lst if i]))) == 19:
            print(file.split('/')[-1])
            mch = [' '.join(re.findall('\d*\.*\d*|\d*', i)).strip().split() [0]
                   for i in self.get_text(file, 1).split('\n') if re.findall('MCH', i)]
            lst.append(mch)
        return list(map(float, [i[0] for i in lst if i])), file,



