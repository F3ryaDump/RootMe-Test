import os
import wget
import time

f = open("./name.txt","r")
content = f.read().rstrip()[1:][:-1].split(", ")
f.close()

liste_file=[]

for i in content:
    liste_file.append(i[1:][:-1])

for file in liste_file:
	url = "http://10.10.30.11/"+str(file)
	try:

		file_download = wget.download(url, out="/home/yanis/Téléchargements")
		print(url)
	
		time.sleep(3)
	except:
		print(str(url)+str("ERROR\n"))
		pass
