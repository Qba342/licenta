from bs4 import BeautifulSoup


def listToString(str):
    str1=" "
    return(str1.join(str))


class FilterHtml:


    def __init__(self,source):
        self.source=source
        self.soup=BeautifulSoup(open(self.source),'html.parser')
        self.listaClase=[]
        self.listaImagini=[]

    def setClassList(self):


        divs= self.soup.find_all("div", class_=True)
        for div in divs:
            self.listaClase.append(listToString(div['class']))



    def setBestDiv(self):

        tupleList=[]

        for div in self.listaClase:
            res= self.soup.find("div", {"class":div})
            children=res.findChildren("p",recursive=False)
            tupleList.append((len(children),div)) #creeam o lista cu copii care contin cele mai multe paragrafe
        tupleList.sort(key=lambda tup: tup[0],reverse=True)#sortam lista descrescator
        bestDiv=tupleList[0][1]
       # res = soup.find("div", {"class": tupleList[1][1]})
        #print(res.text)
        longFinal=0

        if(tupleList[0][0]==tupleList[1][0]):#verificam daca primele doua intrari au valori egale (in contextul in care art este scris cu un singur paragraf)
            n=0
            while(tupleList[n][0]==tupleList[n+1][0]):
                res = self.soup.find("div", {"class": tupleList[n][1]})
                long=len(res.text)
                if(long>longFinal):
                    longFinal=long
                    bestDiv=tupleList[n][1]
                n=n+1

        self.div=bestDiv



    def extractUsefullResources(self, type):

        divToSearch= self.soup.find("div", {"class": self.div})
        images=divToSearch.find_all(type)
        for image in images:
            self.listaImagini.append(image['src'])

    def print_content(self):
        to_print= self.soup.find("div", {"class": self.div})
        print(to_print.text)

    def extract(self):
        self.setClassList()
       # difs=differences(blogList,baseList)
        self.setBestDiv()
        self.extractUsefullResources("img")

        #TODO: Trebuie sa procesam si fisierele de tip pdf. Acestea se gasesc folosind a href="blabla.pdf"
        #TODO: O sa incepem sa facem parsarea imaginilor
        #print(div)


#extractor("C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/krebsonsecurity/7a3c42a708726ac7534008355eae270f")
#extractor("C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/thehackernews/65bc8f398951089f8aa2938c4634a534")
filter=FilterHtml("C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/thehackernews/65bc8f398951089f8aa2938c4634a534")
filter.extract()
filter.print_content()