from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import requests
import utils


class pdfExtractor:

    def __init__(self, link_to_pdf):
        self.link_to_pdf = link_to_pdf
        self.path=str(utils.getpath())+"/tmp.pdf"#il vom stoca aici, apoi il vom sterge
        self.text=''

    def __del__(self):
        utils.remove_file(self.path)


    def get_pdf(self):
        req=requests.get(self.link_to_pdf,stream=True)
        f=open(self.path,"wb")
        f.write(req.content)
        f.close()


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


    def extract(self):
        self.get_pdf()
        self.get_pdf_writing()







#p=pdfExtractor('https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-china-chopper.pdf')
#p.get_pdf()
#p.get_pdf_writing()