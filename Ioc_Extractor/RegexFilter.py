import re
import utils



regex_list={
            "Email":r"\b([a-z][_a-z0-9-.]+@[a-z0-9-]+\[?\.\]?[a-z]+)\b",
            "Domain":r"\b([a-zA-Z\d-]{1,63}\[?\.\]?[a-zA-Z]{2,63}\[?\.?\]?[a-zA-Z]{1,63}?)\b",
            "Filepath":r"\b[A-Z]:\\[A-Za-z0-9-_\.\\]+\b",
            "IP":r"\b(\d{1,3}\[?\.\]?\d{1,3}\[?\.\]?\d{1,3}\[?\.\]?\d{1,3})\b",
            "MD5":r"\b([a-f0-9]{32}|[A-F0-9]{32})\b",
            "Registry":r"\b((HKLM|HKCU)\\[\\A-Za-z0-9-_]+)\b",
            "SHA1":r"\b([a-f0-9]{40}|[A-F0-9]{40})\b",
            "SHA256":r"\b([a-f0-9]{64}|[A-F0-9]{64})\b"}

cve={"CVE":r"\b(CVE\-[0-9]{4}\-[0-9]{4,6})\b"}

class RegexFilter:


    def __init__(self,filepath=''):
        self.filepath=filepath
        self.listaDeTestat = utils.list_filenames(self.filepath)





    def searchforRegex(self,file : str):
        with open(file,encoding="utf8") as f:
            x=f.read()
            for key in regex_list:
                 m=re.findall(regex_list[key],x)
                 if m!=[]:
                     return True
        return False


    def getAll(self,file : str):
        list=[]
        with open(file,encoding="utf8") as f:
            x=f.read()
            for key in regex_list:
                 m=re.findall(regex_list[key],x)
                 if m!=[]:
                     list+=m
        return  list


    def regexRemover(self):
        for itm in self.listaDeTestat:
           if self.searchforRegex(self.filepath+"/"+itm)==False:
               utils.remove_file(self.filepath+"/"+itm)






class Remover:
    def __init__(self,):
        self.path_of_extracted=str(utils.getpath())+"/processed/"
        self.path_list=utils.list_filenames(self.path_of_extracted)


    def run(self):
        for path in self.path_list:
            rf=RegexFilter(self.path_of_extracted+path)
            rf.regexRemover()
            if utils.list_filenames(self.path_of_extracted+path)==[]:
                utils.remove_empty_dir(self.path_of_extracted+path)




a=Remover()
a.run()
#TODO: sa implementez o filtrare mai buna pe baza regex+ implementare nlp

