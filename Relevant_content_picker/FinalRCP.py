from Relevant_content_picker.UnitarRCP import UnitarRCP
import utils
import MyApis

class RCP:
    def __init__(self,downloads_path):
        self.downloads_path=downloads_path
        self.api = MyApis.IOXApi("conf")

    def process(self):
        lista_site=utils.list_filenames(self.downloads_path)
        processed=self.api.getProcessed()


        for site in lista_site:
            lista_bloguri=utils.list_filenames(self.downloads_path+site+"/")
            for blog in lista_bloguri: #md5-ul blogurilor
                if blog not in processed:
                    self.api.addProcessed(blog)
                    ur = UnitarRCP(self.downloads_path+site+"/"+blog)
                    ur.run()


#rcp=RCP("C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/")
#rcp=RCP(str(utils.getpath())+"/downloads/")
#rcp.process()

