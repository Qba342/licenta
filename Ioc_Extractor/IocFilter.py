import iocextract


def getRefanged(sentence:str):#aici sunt IOC 100%
    lista=[]
    a=sentence
    refanged=list(iocextract.extract_iocs(sentence))
    for ioc in refanged:
        type=getIocType(ioc)
        if type=="ipv4":
            ref=iocextract.refang_ipv4(ioc)
            if ref!=ioc:
                a=a.replace(ioc,ref)
                lista.append(iocextract.refang_ipv4(ioc))
        if type=="url":
            ref=iocextract.refang_url(ioc)
            if ref!=ioc:
                a=a.replace(a,ioc)
                lista.append(iocextract.refang_url(ioc))

    lista=list(set(lista))
    return a,lista



def getIocType(text:str):
    res=list(iocextract.extract_ipv4s(text))
    if res != []:
        return "ipv4"

    res = list(iocextract.extract_ipv6s(text))
    if res != []:
        return "ipv6"

    res=list(iocextract.extract_urls(text))
    if res != []:
        return "url"


    res=list(iocextract.extract_emails(text))
    if res != []:
        return "email"

    res = list(iocextract.extract_md5_hashes(text))
    if res != []:
        return "md5"

    res=list(iocextract.extract_sha1_hashes(text))
    if res != []:
        return "sha1"

    res = list(iocextract.extract_sha256_hashes(text))
    if res != []:
        return "sha256"

    res = list(iocextract.extract_sha512_hashes(text))
    if res != []:
        return "sha512"

    res=list(iocextract.extract_custom_iocs(text, [r"\b((HKLM|HKCU)\\[\\A-Za-z0-9-_]+)\b"]))
    if res!= []:
        return "registry"

    res=list(iocextract.extract_custom_iocs(text,[r"\b([A-Za-z0-9-_\.]+\.(exe|dll|bat|sys|htm|html|js|jar|jpg|png|vb|scr|pif|chm|zip|rar|cab|pdf|doc|docx|ppt|pptx|xls|xlsx|swf|gif))\b"]))
    if res!=[]:
        return "filename"
    res = list(iocextract.extract_custom_iocs(text, [r"\b[A-Z]:\\[A-Za-z0-9-_\.\\]+\b"]))
    if res != []:
        return "path"






def hasIoc(text):
    res1=[]
    res2=[]
    res3=[]
    res4=[]
    try:
        res1 =list(iocextract.extract_iocs(text))
        res2 = list(iocextract.extract_custom_iocs(text, [r"\b((HKLM|HKCU)\\[\\A-Za-z0-9-_]+)\b"]))
        res3 = list(iocextract.extract_custom_iocs(text, [r"\b([A-Za-z0-9-_\.]+\.(exe|dll|bat|sys|htm|html|js|jar|vb|scr|pif|chm|zip|rar|cab|pdf|doc|docx|ppt|pptx|xls|xlsx|swf|gif))\b"]))
        res4 = list(iocextract.extract_custom_iocs(text, [r"\b[A-Z]:\\[A-Za-z0-9-_\.\\]+\b"]))
    except:
        pass
    return res1+res2+res3+res4



#a,b=getRefanged("102.22.22.22 is malicious")
#print(a,"\n",b)






