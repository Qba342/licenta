from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import requests
import utils
import tabula





class pdfExtractor:

    def __init__(self, link_to_pdf):
        self.link_to_pdf = link_to_pdf
        self.path=str(utils.getpath())+"/tmp.pdf"#il vom stoca aici, apoi il vom sterge
        self.text=''

    def delete(self):
        utils.remove_file(self.path)


    def get_pdf(self):
        try:
            req=requests.get(self.link_to_pdf,stream=True)
            f=open(self.path,"wb")
            f.write(req.content)
            f.close()
        except:
            pass


    def get_pdf_writing(self):
        output_string = StringIO()
        count=1
        with open(self.path, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                if count>2:
                  interpreter.process_page(page)
                count=count+1

        self.text=output_string.getvalue()

    def get_tables(self):


        file = self.path

        tables = tabula.read_pdf(file, pages="all", multiple_tables=True,stream=True)
        #tabula.convert_into(file,"aaa.csv",all)


        print(tables)




    def extract(self):
        self.get_pdf()
        try:
         self.get_pdf_writing()
        except:
            print("Pdf corupt")
        #self.get_tables()







#p=pdfExtractor('https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf')

#p.extract()

# path="../processed/"
#
# for i in range(200):
#     f=open(path+str(i+1)+"/pdf","rt",encoding="utf8")
#     print(f.read())
#     f.close()