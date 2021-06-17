from pymisp import PyMISP
from pymisp.tools import load_openioc_file

def uploadToMisp(iocFile):
    ioc=load_openioc_file(iocFile)
    pymisp=PyMISP("https://localhost:8443/","TtrXguGOZjcdBHmEH6kBEXsanymScfvuVG0rY7pl",False,False)
    pymisp.add_event(ioc)


uploadToMisp("8ae9b854-448d-4d9f-a7dd-e72f0b1139bd.ioc")