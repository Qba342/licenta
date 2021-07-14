import utils
from Blog_Scrapper.usual_blog_scrapper import Usual_blog_scrapper
from Ioc_Extractor.ExtractorRoutine import IoC_Rout
from Relevant_content_picker.FinalRCP import RCP
from Ioc_Extractor.IocDecision import create_ioc
from Ioc_Extractor.IocWriter import write_to_file
from Ioc_Extractor.mispUploader import uploadToMisp
import MyApis


import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def run():
    api=MyApis.IOXApi()
    base_urls=api.getMonitoredSites()
    for url in base_urls:
        scrappy=Usual_blog_scrapper(url,False)
        scrappy.DownloadResources()
    rcp=RCP(str(utils.getpath())+"/downloads/")
    rcp.process()
    iocExtr=IoC_Rout("processed",True)
    iocs=iocExtr.do()
    if len(iocs)!=0:
        ioc=create_ioc(iocs)
        write_to_file(ioc)
        list=os.listdir()
        blockPrint()
        for item in list:
            if utils.get_extension(item)==".ioc":
                uploadToMisp(item)
                utils.remove_file(item)
                break




#run()