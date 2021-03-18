from .imageExtractor import ImageExtractor

class rcp:
    def __init__(self,source,output_path):
        self.source=source
        self.output_path=output_path

    def run(self):
        imgHandler=ImageExtractor(self.source,self.output_path)
        imgHandler.extract()
