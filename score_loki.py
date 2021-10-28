# Afficher le score de toutes les règles loki

from os import walk
from posix import listdir
import re
listeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk("/etc/Loki/signature-base/yara/"):
    for file in fichiers:
        rep_file = repertoire+"/"+file
        listeFichiers.append(rep_file)

list_score = []
for file_rule in listeFichiers:
    with open(file_rule,"r") as file:
        content=file.readlines()
        verif = 0
        for lin in content:
            if "meta:" in lin:
                verif = 1
            if verif == 1:
                if "score =" in lin:
                    pattern = "score = (\d*)"
                    score = (re.findall(pattern,lin))[0]

                    list_score.append(int(score))
                    verif = 0

print(sorted(set(list_score)))

print("\nScore |\tRepet")
print("----------------")
for nbr in range(801):
    count = list_score.count(nbr)
    if count != 0:
        print(nbr,"\t",count)



    