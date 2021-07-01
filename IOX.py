import argparse
import run
import MyApis

parser=argparse.ArgumentParser()
parser.add_argument("-sM","--showMon",help="Arata ce site-uri sunt tinute sub monitorizare",action="store_true")
parser.add_argument("-a","--addSite",help="Adauga site-ul")
parser.add_argument("-sV","--showVis",help="Arata ce a fost analizat",action="store_true")


parser.add_argument("-d","--deleteSite",help="Sterge din lista de urmariri")

parser.add_argument("-fr","--fastRun",help="Face o verificare rapida asupra site-urilor de sub monitorizare",action="store_true")

parser.add_argument("-r","--run",help="Ruleaza programul pe o perioada de timp",metavar=("Perioada(min)"))

parser.add_argument("-b","--background",help="Daca programul este setat sa ruleze, acesta o va face in background",action="store_true")


parser.add_argument("-misp","--mispconf",help="Seteaza cheia si link-ul spre instanta de MISP",nargs=2,metavar=("CHEIE","LINK"))



args=parser.parse_args()
if args.run:
   print(args.run)