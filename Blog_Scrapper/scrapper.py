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


def GetBlogsFromPage(base_url, url):
    listaBloguriPePagina = []
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    for link in soup.find_all("a"):
        redirect = xstr(link.get("href"))
        print(redirect)
        if (is_in_same_domain(get_domain(base_url), redirect)):  # verificam daca este in acelasi domeniu
            listaBloguriPePagina.append(RemoveComFromString(redirect))
    for blog in listaBloguriPePagina:
        if (blog.find("?") != -1):
            listaBloguriPePagina.remove(blog)
    return listaBloguriPePagina


def GetPagesList(base_url, nrPagini):
    listaPaginiFinala = []
    for i in range(nrPagini):
        url = base_url + "page/" + str(i + 1)
        listaPaginiFinala = listaPaginiFinala + GetBlogsFromPage(base_url, url)
        # time.sleep(2)
    listaPaginiFinala = list(dict.fromkeys(listaPaginiFinala))
    return listaPaginiFinala


def download(url, downloadSource):
    r = requests.get(url, allow_redirects=True)
    # print(url+": "+r.headers.get('content-type'))
    # if(url[-1]=='/'):
    #    url=url[:-1]
    # name=url.rsplit("/",1)[1]

    os.makedirs(os.path.dirname(downloadSource), exist_ok=True)
    with open(downloadSource, 'wb') as f:
        f.write(r.content)


def DownloadResources(base_url, older_search):
    base_download = base_url.split("/", 2)[-1].rsplit(".", 1)[0]
    if (base_download.find(".")):
        base_download = base_download.rsplit(".", 1)[-1]
    DownloadAdress = "downloads/" + base_download + "/"
    if (older_search == True):  # daca dorim o cautare printre paginile mai vechi
        listaPagini = GetPagesList(base_url, 1)  # aici trebuie sa setam numarul paginilor

        for pagina in listaPagini:
            #  ListaImagini=GetImages(base_url,pagina)
            md5 = hashlib.md5(pagina.encode()).hexdigest()
            DownloadAdress2 = DownloadAdress + md5  # pentru a tine evidenta
            download(pagina, DownloadAdress2)
    else:
        listaBloguri = GetBlogsFromPage(base_url, base_url)
        for blog in listaBloguri:
            md5 = hashlib.md5(blog.encode()).hexdigest()
            DownloadAdress2 = DownloadAdress + md5  # pentru a tine evidenta
            download(blog, DownloadAdress2)

    # GetImages(base_url,listaPagini[10])# vom prelucrea imaginile astfel incat sa preluam scrisul din ele


DownloadResources("https://thehackernews.com/", False)  # vom pune True daca vrem sa cautam si in postari mai vechi
