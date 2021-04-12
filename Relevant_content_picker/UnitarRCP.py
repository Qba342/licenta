from Relevant_content_picker.imageExtractor import ImageExtractor
from Relevant_content_picker.FilterHtml import FilterHtml
from Relevant_content_picker.pdfExtractor import pdfExtractor
import utils


def get_name(string):
    st = string.split("/", -1)[-2]  # luam penultima parte din path pentru a ne crea un nou folder
    return st


class UnitarRCP:
    def __init__(self, source=""):
        self.source = source
        if (source != ""):
            self.download_relative_path = source.split("/", -1)[-2]
        self.path = str(utils.getpath()) + "/processed/" + str(utils.Statics.idProc)

    def set_source(self, source):
        self.source = source

    def run(self):
        print(utils.Statics.idProc)
        imgtext = ''
        pdftext=''
        filter = FilterHtml(self.source)
        filter.extract()
        imgHandler = ImageExtractor()
        for img in filter.listaImagini:
            imgHandler.set_link(img)
            imgHandler.extract()
            imgtext = imgtext + imgHandler.text + "\n"

        for pdf in filter.listaPDF:
            pdfHandler=pdfExtractor(pdf)
            pdfHandler.extract()
            pdftext=pdftext+pdfHandler.text+"\n"



        filteredText=filter.content.replace("&nbsp", " ")
        utils.writetofile(filteredText, self.path+"/html", 'w')

        utils.writetofile(imgtext, self.path+"/img", 'w')
        utils.writetofile(pdftext, self.path+"/pdf", 'w')



        utils.Statics.idProc = utils.Statics.idProc + 1
    # print(imgHandler.text)


#RCP = UnitarRCP(
#    "C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/thehackernews/65bc8f398951089f8aa2938c4634a534")
#RCP.run()
