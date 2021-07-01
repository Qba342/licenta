from pymisp import PyMISP
from pymisp.tools import load_openioc_file
def uploadToMisp(iocFile):
    ioc=load_openioc_file(iocFile)
    f=open("conf/mispApi.txt")
    mi=f.read().split("\n")

    pymisp=PyMISP(mi[0],mi[1],False,False)
    pymisp.add_event(ioc)


#uploadToMisp("../readme.txt")

#uploadToMisp("8ae9b854-448d-4d9f-a7dd-e72f0b1139bd.ioc")