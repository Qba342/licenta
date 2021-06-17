from bs4 import BeautifulSoup
import requests
import hashlib
import utils


from Blog_Scrapper.IBlog_Scrapper import IBlog_Scrapper

# site-urile pe care vom face crawl sunt de forma site/page/i
# vom lua prima data un numar de pagini
# vom obtine paginile respective si le vom adauga intr-o lista

class Usual_blog_scrapper(IBlog_Scrapper):
    def __init__(self,base_url,older_posts):
        self.base_url=base_url
        self.older_search=older_posts
        self.listaBloguri=[]

    def __GetBlogsFromPage(self):

        html_content = requests.get(self.base_url).text
        soup = BeautifulSoup(html_content, "html.parser")
        for link in soup.find_all("a"):
            redirect = utils.xstr(link.get("href"))
            if (utils.is_in_same_domain(utils.get_domain(self.base_url), redirect)):  # verificam daca este in acelasi domeniu
                self.listaBloguri.append(utils.RemoveComFromString(redirect))
        for blog in self.listaBloguri:
            if (blog.find("?") != -1):
                self.listaBloguri.remove(blog)



    def __GetPagesList(self, nrPagini):
        listaPaginiFinala = []
        for i in range(nrPagini):
            url = self.base_url + "page/" + str(i + 1)
            listaPaginiFinala = listaPaginiFinala + self.__GetBlogsFromPage(self.base_url, url)
            # time.sleep(2)
        listaPaginiFinala = list(dict.fromkeys(listaPaginiFinala))
        return listaPaginiFinala



    def DownloadResources(self):
        base_download = self.base_url.split("/", 2)[-1].rsplit(".", 1)[0]
        if (base_download.find(".")):
            base_download = base_download.rsplit(".", 1)[-1]
        DownloadAdress = "downloads/" + base_download + "/"
        if (self.older_search == True):  # daca dorim o cautare printre paginile mai vechi
            listaPagini = self.__GetPagesList(self.base_url, 1)  # aici trebuie sa setam numarul paginilor

            for pagina in listaPagini:
                #  ListaImagini=GetImages(base_url,pagina)
                md5 = hashlib.md5(pagina.encode()).hexdigest()
                DownloadAdress2 = DownloadAdress + md5  # pentru a tine evidenta
                utils.download(pagina, DownloadAdress2)
        else:
            self.__GetBlogsFromPage()

            for blog in self.listaBloguri:
                md5 = hashlib.md5(blog.encode()).hexdigest()
                DownloadAdress2 =str(utils.getpath())+"/"+ DownloadAdress + md5  # pentru a tine evidenta
                utils.download(blog, DownloadAdress2)


    def MEMrun(self):
        self.__GetBlogsFromPage()
        print(self.listaBloguri)



scrap=Usual_blog_scrapper("https://thehackernews.com/", False)
scrap.MEMrun()
