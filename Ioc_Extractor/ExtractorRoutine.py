import utils
from Ioc_Extractor.IocDecision import makeDecision,create_ioc


class IoC_Rout():
    def __init__(self,path,remove:bool):
        self.path=path
        self.toScanList=['/html','/pdf','/img']
        self.remove=remove

    def do(self):
        toScan=utils.list_filenames(self.path)
        ioclist=[]
        print(toScan)
        for dir in toScan:
            path2=self.path+"/"+dir
            for tosc in self.toScanList:
                file=open(path2+tosc,"r",encoding="utf-8")
                text=file.read()
                file.close()
                if self.remove==True:
                    utils.remove_file(path2+tosc)
                a=makeDecision(text)
                if a!=False:
                    ioclist=ioclist+a
            if self.remove==True:
             utils.remove_empty_dir(path2)
            print("Am incercat sa extrag din ",dir)
        return ioclist








#a=IoC_Rout("../processed",False)
