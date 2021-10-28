
#Ajout d'un score aléatoire Clamav

from random import *

new = []
with open("/var/lib/clamav-score/Clamav_Score.md","r") as file:
    for line in file:
        if line=="\n" or line[:1]=="#":
            new.append(line)
        else:
            new_line = line.strip("\n") + ";"+str(randint(1,30)) + "\n"
            new.append(new_line)

with open("/var/lib/clamav-score/Clamav_Score.md","w") as file:
    for line in new:
        file.write(line)