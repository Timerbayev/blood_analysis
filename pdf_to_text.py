# importing required modules
import re
import PyPDF2


class GetVectors:
    def __init__(self, *args):
        self.array = args

    def get_vectors(self, file):
        pdf_fileobj = open(file, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_fileobj)
        pageobj = pdf_reader.pages[0]
        text = pageobj.extract_text()
        start, lst = None, []
        for key, value in enumerate(text.split('\n')):
            if value.split()[0] == self.array[0]:  # 'B02.061.002':
                start = key
        for i in text.split('\n')[start:]:
            if i.startswith(self.array[0]) or i.startswith(self.array[1]):  #'B02.110.002'
                continue
            else:
                lst.append(' '.join(re.findall('\d*\.*\d*|\d*', i)).strip().split())
        pdf_fileobj.close()
        if len(list(map(float, [i[0] for i in lst if i]))) == 17:
            print(file.split('/')[-1])
        return list(map(float, [i[0] for i in lst if i])), file,
