import argparse
import run
import MyApis
import time

parser=argparse.ArgumentParser()
parser.add_argument("-sM","--showMon",help="Arata ce site-uri sunt tinute sub monitorizare",action="store_true")
parser.add_argument("-a","--addSite",help="Adauga site-ul")
parser.add_argument("-sV","--showVis",help="Arata ce a fost analizat",action="store_true")


parser.add_argument("-d","--deleteSite",help="Sterge din lista de urmariri")

parser.add_argument("-fr","--fastRun",help="Face o verificare rapida asupra site-urilor de sub monitorizare",action="store_true")

parser.add_argument("-r","--run",help="Ruleaza programul la infinit iar odata la o perioada de timp va face update cu ce a gasit",metavar=("Perioada(min)"))


parser.add_argument("-misp","--mispconf",help="Seteaza cheia si link-ul spre instanta de MISP",nargs=2,metavar=("CHEIE","LINK"))





args=parser.parse_args()
api=MyApis.IOXApi()
if args.fastRun:
   run.run()


if args.showMon:
   list=api.getMonitoredSites()
   i=0
   for mon in list:
      if mon!="":
         print(str(i)+" "+mon)
      i=i+1

if args.addSite:
   api.addSite(args.addSite)

if args.showVis:
   list=api.getVisited()
   for a in list:
      if a!="":
         print(a)

if args.deleteSite:
   if args.deleteSite.isnumeric():
      api.removeSite(index=int(args.deleteSite))
   else:
      api.removeSite(baseLink=args.deleteSite)


if args.run:
   if args.run.isnumeric():
      perioada=int(args.run)
      try:
         while True:
            run.run()
            time.sleep(perioada*60)
      except KeyboardInterrupt:
         print("Ati intrerupt rularea")



