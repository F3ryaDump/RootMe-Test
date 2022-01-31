#!/bin/python3
# Comparaison des hash du filestore suricata avec les downloads
from ctypes import sizeof
import os

liste = sorted(os.listdir("/var/log/suricata/filestore/"))

cpt = 0

for rep in liste:
    if os.listdir("/var/log/suricata/filestore/"+rep) != [] and rep != "tmp":
        print("----------------------------------------------------------------------------------------------------------")
        print("/var/log/suricata/filestore/"+rep)
        name = os.popen("cat /var/log/suricata/filestore/"+rep+"/*.json | jq '.fileinfo.filename'","r").read().rstrip().replace('"',"").replace(" ","\ ")
        sha256 = os.popen("cat /var/log/suricata/filestore/"+rep+"/*.json | jq '.fileinfo.sha256'","r").read().rstrip().replace('"',"")
        size = os.popen("cat /var/log/suricata/filestore/"+rep+"/*.json | jq '.fileinfo.size'","r").read().rstrip().replace('"',"")

        print(name+" : "+sha256+" : "+size)

        
        cpt += 1

        sha256_download = os.popen("sha256sum /home/yanis/Téléchargements"+name+" | awk '{print $1}'","r").read().rstrip()

        if sha256_download == sha256:
            print(sha256_download+" -> HASH VALIDE !")
        else:
            print(sha256_download+" -> HASH INVALIDE...")

        size_download = os.popen("wc -c /home/yanis/Téléchargements"+name+" | awk '{print $1}'").read().rstrip()

        if size_download == size:
            print(size_download+" -> SIZE VALIDE !")
        else:
            print(size_download+" -> SIZE INVALIDE...")

print("\n"+str(cpt)+" fichiers ont été téléchargés")