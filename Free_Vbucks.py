import os
import time
import pyfiglet
from colorama import Fore
from interaction import ProgressBar

rusult = pyfiglet.figlet_format("Free Vbucks")
print(f'{Fore.BLUE}' + rusult + f'{Fore.WHITE}') 

if os.name == "nt":
    os.system('cls')

username = input("What is your epic: ")
time.sleep(1)

if os.name == "nt":
    os.system('cls')

Vbucks = input("How many Vbucks do you want: ")
time.sleep(1)

bar = ProgressBar(total=100)

for i in range(100):
  time.sleep(0.1)
  bar.show(amount=i+1)

print("")
print("Vbucks have been added to your account restart Epic")
time.sleep(1)

a = open("Popup.vbs", "a")
a.write('''
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+16,"Error")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+32,"LUL")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+48,"Get Fucked")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+16,"HAHHAHAAH")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+32,"#Dedsec")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+48,"Lol")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+16,"@dedsec")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+32,"LULZSEC")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+48,"FUCKED")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+16,"Aiden Pearce")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+32,"LOLOLOLOLOLOL")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+48,"DEDSEC")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+16,"011001001010101110000101")
X=MsgBox("A Virus Has been detected, Lmao Dumbass kid",0+32,"DIE")''')
a.close()

os.system("Popup.vbs")
