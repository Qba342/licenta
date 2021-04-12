import iocextract


def getRefanged(sentence:str):#aici sunt IOC 100%
    refanged=list(iocextract.extract_iocs(sentence,refang=True))
    notrefanged=list(iocextract.extract_iocs(sentence))
    return list(set(notrefanged)-set(refanged))


def getIocType(text:str):
    res=list(iocextract.extract_urls(text,refang=True))
    if res != []:
        return "url"
    res=list(iocextract.extract_ipv4s(text,refang=True))
    if res != []:
        return "ipv4"

    res = list(iocextract.extract_ipv6s(text, refang=True))
    if res != []:
        return "ipv6"

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
    return "other"



def hasIoc(text):
        res1 =list(iocextract.extract_iocs(text,refang=True))
        res2 = list(iocextract.extract_custom_iocs(text, [r"\b((HKLM|HKCU)\\[\\A-Za-z0-9-_]+)\b"]))
        res3 = list(iocextract.extract_custom_iocs(text, [r"\b([A-Za-z0-9-_\.]+\.(exe|dll|bat|sys|htm|html|js|jar|vb|scr|pif|chm|zip|rar|cab|pdf|doc|docx|ppt|pptx|xls|xlsx|swf|gif))\b"]))
        res4 = list(iocextract.extract_custom_iocs(text, [r"\b[A-Z]:\\[A-Za-z0-9-_\.\\]+\b"]))

        return res1+res2+res3+res4










