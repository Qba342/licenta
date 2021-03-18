from bs4 import BeautifulSoup
import requests
import hashlib
import os


# site-urile pe care vom face crawl sunt de forma site/page/i
# vom lua prima data un numar de pagini
# vom obtine paginile respective si le vom adauga intr-o lista


def xstr(s):
    if s is None:
        return ''
    return str(s)


def get_domain(url):
    if url.count('.') == 2:
        return url.split('.', 1)[1]
    return url


def is_in_same_domain(url, link):
    get_domain(url)
    val = link.find(url)
    if (val == -1):
        return False
    return True


def RemoveComFromString(string):
    sep = '#'
    return (string.split(sep, 1)[0])

class BlogScrapper:
    def __init__(self,base_url,older_posts):
        self.base_url=base_url
        self.older_search=older_posts
        self.listaBloguri=[]

    def GetBlogsFromPage(self):

        html_content = requests.get(self.base_url).text
        soup = BeautifulSoup(html_content, "html.parser")
        for link in soup.find_all("a"):
            redirect = xstr(link.get("href"))
            print(redirect)
            if (is_in_same_domain(get_domain(self.base_url), redirect)):  # verificam daca este in acelasi domeniu
                self.listaBloguri.append(RemoveComFromString(redirect))
        for blog in self.listaBloguri:
            if (blog.find("?") != -1):
                self.listaBloguri.remove(blog)



    def GetPagesList(self, nrPagini):
        listaPaginiFinala = []
        for i in range(nrPagini):
            url = self.base_url + "page/" + str(i + 1)
            listaPaginiFinala = listaPaginiFinala + self.GetBlogsFromPage(self.base_url, url)
            # time.sleep(2)
        listaPaginiFinala = list(dict.fromkeys(listaPaginiFinala))
        return listaPaginiFinala


    def download(self,url, downloadSource):
        r = requests.get(url, allow_redirects=True)

        os.makedirs(os.path.dirname(downloadSource), exist_ok=True)
        with open(downloadSource, 'wb') as f:
            f.write(r.content)


    def DownloadResources(self):
        base_download = self.base_url.split("/", 2)[-1].rsplit(".", 1)[0]
        if (base_download.find(".")):
            base_download = base_download.rsplit(".", 1)[-1]
        DownloadAdress = "downloads/" + base_download + "/"
        if (self.older_search == True):  # daca dorim o cautare printre paginile mai vechi
            listaPagini = self.GetPagesList(self.base_url, 1)  # aici trebuie sa setam numarul paginilor

            for pagina in listaPagini:
                #  ListaImagini=GetImages(base_url,pagina)
                md5 = hashlib.md5(pagina.encode()).hexdigest()
                DownloadAdress2 = DownloadAdress + md5  # pentru a tine evidenta
                self.download(pagina, DownloadAdress2)
        else:
            self.GetBlogsFromPage()

            for blog in self.listaBloguri:
                md5 = hashlib.md5(blog.encode()).hexdigest()
                DownloadAdress2 = DownloadAdress + md5  # pentru a tine evidenta
                self.download(blog, DownloadAdress2)

    # GetImages(base_url,listaPagini[10])# vom prelucrea imaginile astfel incat sa preluam scrisul din ele


#DownloadResources("https://thehackernews.com/", False)  # vom pune True daca vrem sa cautam si in postari mai vechi

#scrap=BlogScrapper("https://thehackernews.com/", False)
#scrap.DownloadResources()
