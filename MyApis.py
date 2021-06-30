import os
import requests


#import Blog_Scrapper.usual_blog_scrapper
#import Blog_Scrapper
#import Relevant_content_picker.FinalRCP
#import Ioc_Extractor.IocDecision


class IOXApi():
    def __init__(self,confpath=""):
        self.monitor="monitor.txt"
        self.visited="visited.txt"
        self.mispApi="mispApi.txt"

        if confpath=="":
            self.confpath="conf/"
        else:
            self.confpath=confpath+"/"

        try:
            x=os.listdir(self.confpath)
        except:
            print("Calea specificata nu este buna")



    def getMonitoredSites(self):
        f=open(self.confpath+self.monitor,"rt")
        lista=list(f.read().split("\n"))
        f.close()
        return lista

    def addSite(self, baseLink):
        listaSiteuri=self.getMonitoredSites()
        if(baseLink in listaSiteuri):
            print("Deja exista acest site")
            return 1
        else:
            try:
                r=requests.head(baseLink)
                cod=r.status_code
                if cod==200:
                    f=open(self.confpath+self.monitor,"a")
                    f.write(baseLink+"\n")
                    f.close()
                    print("Site adaugat cu succes")
                    return 0

            except:
                print("Nu e ok")
                return 1

    def removeSite(self, baseLink="",index=-1):
        listasiteuri=self.getMonitoredSites()
        if baseLink not in listasiteuri:
            print("Site-ul pe care doriti sa il eliminati nu exista")
        else:
            if(baseLink!=""):
                listasiteuri.remove(baseLink)
            elif index!=-1:
                if(index<len(listasiteuri)):
                    listasiteuri.pop(index)
            f=open(self.confpath+self.monitor,"w")
            for site in listasiteuri:
                f.write(site+"\n")
            f.close()
            print("Site eliminat cu succes")

    def addMisp(self,key,link):
        f=open(self.confpath+self.mispApi,"w")
        f.write(key+"\n"+link)
        f.close()

    def getVisited(self):
        f=open(self.confpath+self.visited,"r")
        lista = list(f.read().split("\n"))
        f.close()
        return lista

    def addVisited(self,site):
        if self.verifyVisited(site)==True:
            f=open(self.confpath+self.visited,"a")
            f.write(site+"\n")
            f.close()
            print("Site updatat cu succes")


    def verifyVisited(self,site):
        lista=self.getVisited()
        if site in lista:
            return False
        else:
            return True


    def fastRun(self):
        pass



#i=IOXApi("conf")
#i.addSite('https://www.kite.com/')
#i.removeSite('https://www.kite.com/')
#i.removeSite(index=7)
