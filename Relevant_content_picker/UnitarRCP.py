from Relevant_content_picker.imageExtractor import ImageExtractor
from Relevant_content_picker.FilterHtml import FilterHtml
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
        imgtext = ''
        filter = FilterHtml(self.source)
        filter.extract()
        imgHandler = ImageExtractor()
        for img in filter.listaImagini:
            imgHandler.set_link(img)
            imgHandler.extract()
            imgtext = imgtext + imgHandler.text + "\n"

        finaltext = filter.content + "\n" + imgtext
        finaltext = finaltext.replace("\xc2\xa0", " ")  # pentru a curata de caracterul nbsp
        utils.writetofile(finaltext, self.path, 'w')
        utils.Statics.idProc = utils.Statics.idProc + 1
    # print(imgHandler.text)


RCP = UnitarRCP(
    "C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/thehackernews/65bc8f398951089f8aa2938c4634a534")
RCP.run()
