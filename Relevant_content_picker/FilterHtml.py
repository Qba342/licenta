from bs4 import BeautifulSoup


def listToString(str):
    str1=" "
    return(str1.join(str))



def getClassList(source):
    listaClase=[]#lista in care vom stoca toate clasele

    soup=BeautifulSoup(open(source),'html.parser')
    divs=soup.find_all("div",class_=True)
    for div in divs:
        listaClase.append(listToString(div['class']))
    return listaClase



def getBestDiv(source,divList):
    soup=BeautifulSoup(open(source),'html.parser')
    tupleList=[]

    for div in divList:
        res=soup.find("div",{"class":div})
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
            res = soup.find("div", {"class": tupleList[n][1]})
            long=len(res.text)
            if(long>longFinal):
                longFinal=long
                bestDiv=tupleList[n][1]
            n=n+1

    return (bestDiv)



def getUsefullResources(source,div,type):
    listaImagini = []
    soup = BeautifulSoup(open(source), "html.parser")
    divToSearch=soup.find("div",{"class":div})
    images=divToSearch.find_all(type)
    for image in images:
        listaImagini.append(image['src'])
    return listaImagini


def extractor(blog_File):
    blogList=getClassList(blog_File)
   # difs=differences(blogList,baseList)
    div=getBestDiv(blog_File,blogList)
    getUsefullResources(blog_File,div,"img")
    getUsefullResources(blog_File, div, "img")
    #TODO: Trebuie sa procesam si fisierele de tip pdf. Acestea se gasesc folosind a href="blabla.pdf"
    #TODO: O sa incepem sa facem parsarea imaginilor
    #print(div)


#extractor("C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/krebsonsecurity/7a3c42a708726ac7534008355eae270f")
extractor("C:/Users/Iulian/Desktop/Proiect Licenta/Blog_Scrapper/downloads/thehackernews/521bf76645b5cda738822771799e4dc3")