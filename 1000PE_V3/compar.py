import os
import re
import json

log = open("./Out_Log_Inotify_Service.log","r")
log_text = log.read()
log.close()


liste_name = re.findall("Real Name:(.*)",log_text)


log_text_split = log_text.split("\n")
liste_score = []
for i in range(len(log_text_split)):
    if log_text_split[i] == "===================[ Vérification Virus Total ]===================":
        if "Detecté par:" in log_text_split[i+1]:
            liste_score.append((log_text_split[i+1])[13:])
        else:
            liste_score.append("N/A")

# Read JSON file
with open("./Out_Scan_JSON.json",'r') as file:
    listObj = json.load(file)

for i in range(len(liste_score)):
    for j in listObj:
        if listObj[j]["filename"] == liste_name[i].replace("\t",""):
            print(listObj[j]["scan"]["virus_total"]["detection"]+'\t'+liste_score[i]+"\t"+liste_name[i])
            

