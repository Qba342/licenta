from ioc_writer import ioc_api
import Ioc_Extractor.IocFilter as If


def create_ioc_object(ioc_name, items, and_or=True):
    ioc = ioc_api.IOC(name=ioc_name,author="iulianhalmagean@gmail.com",description="Ioc generated automatically from blogs")
    top_level_or_node = ioc.top_level_indicator
    # build the definition
    if and_or:
        second_level_and_node = ioc_api.make_indicator_node('AND')
        top_level_or_node.append(second_level_and_node)
    for item in items:
        condition, document, search, content_type, content = tuple(item)
        # print condition, document, search, content_type, content
        ii_node = ioc_api.make_indicatoritem_node(condition, document, search, content_type, content)
        if and_or:
            second_level_and_node.append(ii_node)
        else:
            top_level_or_node.append(ii_node)
    # update the last modified time
    ioc.set_lastmodified_date()
    return ioc


def write_to_file(ioc:ioc_api.IOC):
    ioc_api.IOC.write_ioc_to_file(ioc)


def construct_ioc(ioc:str):
    ioctype=If.getIocType(ioc)
    if ioctype=="url":
        tup=("contains","Network","Network/URI","string",ioc)#asta o sa includa inclusiv dns
    elif ioctype=="ipv4":
        tup=("is","DnsEntryItem","DnsEntryItem/RecordData/IPv4Address","domain|ip",ioc)
    elif ioctype=="ipv6":
        tup = ("is", "DnsEntryItem", "DnsEntryItem/RecordData/IPv6Address", "IP", ioc)
    elif ioctype=="email":
        tup=("is","Email","Email/From","string",ioc)
    elif ioctype=="md5":
        tup=("is","FileItem","FileItem/MD5Sum","string",ioc)
    elif ioctype=="sha1":
        tup=("is","FileItem","FileItem/Sha1Sum","string",ioc)
    elif ioctype=="sha256":
        tup=("is","FileItem","FileItem/Sha256Sum","string",ioc)
    elif ioctype=="sha512":
        tup=("is","FileItem","FileItem/Sha512Sum","string",ioc)
    elif ioctype=="registry":
        tup=("contains","RegistyItem","RegistryItem/Path","string",ioc)
    elif ioctype=="filename":
        tup=("contains","FileItem","FileItem/FileName","string",ioc)
    elif ioctype=="path":
        tup=("contains","FileItem","FileItem/FullPath","string",ioc)


    return tup





#a=create_ioc_object("ccc",{construct_ioc("19.2.43.144")},False)
#write_to_file(a)