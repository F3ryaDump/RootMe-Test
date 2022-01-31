import json
import os
import xlsxwriter

eve_json = os.listdir("./PE_Chill/")
        
print(eve_json)

workbook = xlsxwriter.Workbook('Pe_liste_malveillant.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for item in eve_json:
    worksheet.write(row,col,item)
    row +=1

workbook.close()


eve_json = os.listdir("./malware/")
        
print(eve_json)

workbook = xlsxwriter.Workbook('Pe_liste_sain.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for item in eve_json:
    worksheet.write(row,col,item)
    row +=1

workbook.close()