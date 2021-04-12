import os
import requests
import pathlib
import re
def getpath():
    return (pathlib.Path(__file__).parent)

class Statics:
    idProc=1

def replace(substrToBeRepalced,substrToReplace,string :str):
    return re.sub(substrToBeRepalced,substrToReplace,string)


def get_extension(string):
    split_tup = os.path.splitext(string)
    return split_tup[1]

def remove_file(path):
    os.remove(path)

def remove_empty_dir(path):
    os.rmdir(path)

def get_rid_of_spaces(string):
    return(" ".join(string.split()))

def list_filenames(path):
    return os.listdir(path)


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


def writetofile(data,path,mode):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if(mode=="wb"):
        with open(path, mode) as f:
            f.write(data)
    else:
        with open(path, mode,encoding="utf-8") as f:
            f.write(data)

def download(url, downloadSource):
    r = requests.get(url, allow_redirects=True)
    writetofile(r.content,downloadSource,"wb")


