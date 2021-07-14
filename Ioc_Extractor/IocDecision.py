from Ioc_Extractor.IocFilter import *
from Ioc_Extractor.NLP_Process import *
from Ioc_Extractor.IocWriter import *
from nltk import sent_tokenize
from datetime import datetime



def makeDecision(text):

    if not hasIoc(text):#daca nu exista IOC-uri de extras sub formatul respectiv, nu are rost sa cautam
        return False
    validIocList=[]
    props=sentencesplit(text)#daca exista, vom testa fiecare propozitie
    for prop in props:
        iocs=hasIoc(prop)
        if iocs!=[]:
            prop,ref=getRefanged(prop)#daca e in tip defang, propozitia nu o sa fie recunoscuta, va face split aiurea pe cuvinte
            if ref:
                validIocList=validIocList+ref
            for ioc in iocs:
                type=getIocType(ioc)
                if type=="md5" or type=="sha1" or type=="sha256" or type=="sha512":#presupunem ca hash-urile sunt malitioase
                    validIocList.append(ioc)
                else:
                    if NLPisValidIOC(prop,ioc)==True:
                        validIocList.append(ioc)
    return list(set(validIocList))#eliminam dubluri


def create_ioc(lista:list):
    iocs=[]
    for item in lista:
        iocs.append(construct_ioc(item))

    now=datetime.now()
    currenttime=now.strftime("%D %H:%M:%S")
    str="Automatic IOC generated at "+currenttime

    a=create_ioc_object(str,iocs,False)
    return a









#a=makeDecision("29[.]68[.]1[.]2 is malicious. Ip 10.10.1.1 is not.")
#print(create_ioc(a))








