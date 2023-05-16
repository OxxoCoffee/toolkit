
import os, socket, metadata, portscan, scapping, argparse, subprocess
import vt_scan_website, gobuster

parser = argparse.ArgumentParser()
parser.add_argument("-ur", dest="url", help="URL del scrapping y escaneo")
parser.add_argument("-ap", dest="ap1", help="Api Key VirusTotal")
parser.add_argument("-pl", dest="portl", help="Lista de puertos a escanear")
args = parser.parse_args()

hn = socket.gethostname()
ipa = socket.gethostbyname(hn)

x=1
portlist = [80, 84, 243, 135, 445]
urlimg = args.url
apik = args.ap1
banditc = "bandit ../toolkit.py"


pathimg = '../toolkit/Images'

if __name__ == "__toolkit__":
    if args.url == None:
        print("Hay que agregar una URL")
    else:
        if args.ap1 == None:    
            scapping.scrapeo(urlimg, pathimg, x)
            metadata.metaextract(pathimg)
            portscan.techscan(urlimg)
            gobuster.dirscan(urlimg)
        else:
            vt_scan_website.vt_website_analysis(urlimg, args.ap1)
            scapping.scrapeo(urlimg, pathimg, x)
            metadata.metaextract(pathimg)
            portscan.techscan(urlimg)
            gobuster.dirscan(urlimg)
    portscan.puertoscan(ipa, portlist)
    print("\nRealizando escaneo de vulnerabilidades del script\n")
    subprocess.run(banditc, shell=True, universal_newlines=True)