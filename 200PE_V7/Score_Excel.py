import json
import os
import xlsxwriter

# Check if file exists
filename_json = "./Out_Scan_JSON.json"

cmd = 'cat ./Out_Scan_JSON.json | jq ".[].filename"'
eve_json = os.popen(cmd,"r").read().rstrip().split("\n")

for i in eve_json: eve_json[eve_json.index(i)] = i[:-1][1:]

list_final = []
for name in eve_json:
    # Score total
    cmd = 'cat ./Out_Scan_JSON.json | jq \'.[] | select(.filename == \"'+name+'\") | .score_total\''
    score = os.popen(cmd,"r").read().rstrip()[:-1][1:]

    # Score Loki
    cmd = 'cat ./Out_Scan_JSON.json | jq \'.[] | select(.filename == \"'+name+'\") | .scan.loki_scan.score\''
    loki = os.popen(cmd,"r").read().rstrip()[:-1][1:]

    # Score Clavav
    cmd = 'cat ./Out_Scan_JSON.json | jq \'.[] | select(.filename == \"'+name+'\") | .scan.clamav_scan.score\''
    clamav = os.popen(cmd,"r").read().rstrip()[:-1][1:]

    # Score Capa
    cmd = 'cat ./Out_Scan_JSON.json | jq \'.[] | select(.filename == \"'+name+'\") | .scan.capa_scan.score\''
    capa = os.popen(cmd,"r").read().rstrip()[:-1][1:]

    # MalwareBazaar
    cmd = 'cat ./Out_Scan_JSON.json | jq \'.[] | select(.filename == \"'+name+'\") | .scan.malware_bazaar\''
    malware_bazaar = os.popen(cmd,"r").read().rstrip()[:-1][1:]
    
    # VirusTotal
    cmd = 'cat ./Out_Scan_JSON.json | jq \'.[] | select(.filename == \"'+name+'\") | .scan.virus_total.score\''
    virus_total = os.popen(cmd,"r").read().rstrip()[:-1][1:]
    
    # MalShare
    cmd = 'cat ./Out_Scan_JSON.json | jq \'.[] | select(.filename == \"'+name+'\") | .scan.malshare\''
    malshare = os.popen(cmd,"r").read().rstrip()[:-1][1:]

    try:
        elem = [name,float(score),"-",float(clamav),float(loki),float(capa),float(malware_bazaar),float(virus_total),float(malshare)]
        list_final.append(elem)
    except:
        print(name)
        
    

print(list_final)

list_final.sort(key=lambda x: x[1])

list_final.insert(0,["","","","","","","","",""])
list_final.insert(0,["FILENAMES","SCORES","-","CLAMAV","LOKI","CAPA","MALWAREBAZAAR","VT","MALSHARE"])


workbook = xlsxwriter.Workbook('New_Score.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for item in list_final:
    worksheet.write(row,col,item[0])
    worksheet.write(row,col+1,str(item[1]))
    worksheet.write(row,col+2,str(item[2]))
    worksheet.write(row,col+3,str(item[3]))
    worksheet.write(row,col+4,str(item[4]))
    worksheet.write(row,col+5,str(item[5]))
    worksheet.write(row,col+5,str(item[6]))
    worksheet.write(row,col+5,str(item[7]))
    worksheet.write(row,col+5,str(item[8]))

    row +=1

workbook.close()
