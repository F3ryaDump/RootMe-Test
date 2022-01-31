import json
import os
import xlsxwriter

def nbr_rules(name_scan):
    list_pe_chill = os.listdir("./PE_Chill/")
    list_pe_hard = os.listdir("./malware/")

    rules_liste=[]
  
    for name in data:
        # Détermination si c'est un PE chill ou malveillant
        
        if data[name]["filename"][1:] in list_pe_chill:
            status = "L"
        elif data[name]["filename"][1:] in list_pe_hard:
            status = "M"
        else:
            #print(data[name]["filename"][1:])
            status = "ERROR"
        
        
        for rule in data[name]["scan"][name_scan]['rules']:
            if rule != "No Match":
                if not any(rule in i for i in rules_liste):
                    # On incrémente en fct du status
                    if status == "M":
                        rules_liste.append([rule,1,1,0])
                    elif status == "L":
                        rules_liste.append([rule,1,0,1])
                    else:
                        rules_liste.append([rule,1,-999,-999])
                else:
                    # Récupération de l'index
                    for i in enumerate(rules_liste):
                        if i[1][0] == rule:
                            index_rule = i[0]
                    rules_liste[index_rule][1]+=1
                    if status == "M":
                        rules_liste[index_rule][2]+=1
                    elif status == "L":
                        rules_liste[index_rule][3]+=1
                    
    #rules_liste.append('math_entropy_6')
    return(rules_liste)

# Récupération du fichier json de résultat du scan
f = open('./Out_Scan_JSON.json')
data = json.load(f)
f.close()



#Traitement des donnés
rules_loki = nbr_rules("loki_scan")
rules_capa = nbr_rules("capa_scan")
rules_clamav = nbr_rules("clamav_scan")


# Création du xlsx
workbook = xlsxwriter.Workbook('Repet_rules.xlsx')

worksheet1 = workbook.add_worksheet('Loki')
worksheet2 = workbook.add_worksheet('Capa')
worksheet3 = workbook.add_worksheet('Clamav')

# Feuille Loki
row = 0
col = 0
for item in rules_loki:
    worksheet1.write(row,col,item[0])
    worksheet1.write(row,col+1,str(item[1]))
    worksheet1.write(row,col+2,str(item[2]))
    worksheet1.write(row,col+3,str(item[3]))
    row+=1

# Feuille Capa
row = 0
col = 0
for item in rules_capa:
    worksheet2.write(row,col,item[0])
    worksheet2.write(row,col+1,str(item[1])) 
    worksheet2.write(row,col+2,str(item[2]))
    worksheet2.write(row,col+3,str(item[3]))
    row+=1

# Feuille Clamav
row = 0
col = 0
for item in rules_clamav:
    worksheet3.write(row,col,item[0])
    worksheet3.write(row,col+1,str(item[1]))  
    worksheet3.write(row,col+2,str(item[2]))  
    worksheet3.write(row,col+3,str(item[3]))  
    row+=1

workbook.close()
