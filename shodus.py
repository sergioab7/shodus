#!/usr/bin/python3
#coding:utf-8

#Autor: xaxxjs (https://sergioab7.github.io/)


import sys,os,time
from colorama import Fore,Style
from argparse import ArgumentParser
import argparse
import shodan 
from time import sleep
import requests


from beautifultable import BeautifulTable
import warnings
warnings.filterwarnings("ignore")

def api():
    f=open("api.txt", "w")
    comando=input(Fore.BLUE + "\n\t\tINSERTA TU API>>" + Fore.RESET)
    while(len(comando)<29):
         comando=input(Fore.BLUE + "\n\t\tINSERTA TU API>>" + Fore.RESET)
    print(Fore.YELLOW + "\n\t\t[API AGREGADA CON ÉXITO]" + Fore.RESET)
    print(Fore.YELLOW + "\n\tReiniciando el servicio para que se apliquen los cambios\n\n" + Fore.RESET)
    f.write(comando)
    f.close()
    sys.exit()

if(os.path.isfile("api.txt")):
    with open("api.txt", "r") as app:
        API = app.read()
    app.close()
else:
    api()

shodus=shodan.Shodan(API)

print("""
                         _               _           
                        | |             | |          
                     ___| |__   ___   __| |_   _ ___ 
                    / __| '_ \ / _ \ / _` | | | / __|   
                    \__ \ | | | (_) | (_| | |_| \__ |   
                    |___/_| |_|\___/ \__,_|\__,_|___/ v.1
                    """+Fore.RED+"by:xaxxjs (https://sergioab7.github.io/)"+Fore.RESET+"""                           
    """)
parser=argparse.ArgumentParser(description="¡Welcome to shodus!", epilog="Example: sudo python3 shodus.py -H 8.8.8.8 -S || sudo python3 shodus.py -s apache --show")
parser.add_argument("-H","--host",dest="host",type=str, help="Insert IP to search")
parser.add_argument("-S","--simple", dest="simple",help="simple search", action="store_const", const=True)
parser.add_argument("-A","--advanced", dest="advanced",help="advanced search",action="store_const", const=True)
parser.add_argument("-s","--search",dest="search",type=str,help="Insert some search")
parser.add_argument("-show","--show", dest="show",help="Muestra todas las IP",action="store_const", const=True)
results=parser.parse_args()



def shodan_search_ip(busqueda):
    try: 
        busqueda=busqueda.lower()
        print(Fore.YELLOW+"[>] "+Fore.RESET+"Búsqueda: "+Fore.MAGENTA+"%s"%busqueda+Fore.RESET)
        results = shodus.search(busqueda)
        print(Fore.BLUE+"[i]"+Fore.RESET+" Resultados encontrados: "+Fore.MAGENTA+"%s"%results['total']+Fore.RESET)
        sleep(2)
        print("")
        for service in results['matches']:
            print(Style.BRIGHT)
            print(Fore.GREEN+"\t[+] "+Fore.RESET+"%s"%(service['ip_str']))
            print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED+"[!]"+Fore.RESET+" Error: ", e)

def shodan_search(busqueda):
    try: 
        busqueda=busqueda.lower()
        print(Fore.YELLOW+"[>] "+Fore.RESET+"Búsqueda: "+Fore.MAGENTA+"%s"%busqueda+Fore.RESET)
        results = shodus.search(busqueda)
        print(Fore.BLUE+"[i]"+Fore.RESET+" Resultados encontrados: "+Fore.MAGENTA+"%s"%results['total']+Fore.RESET)
        sleep(2)
        print("")
        for result in results['matches']:
            print(Style.BRIGHT)
            print(Fore.YELLOW+'[+] IP:'+Fore.RESET+' {}'.format(result['ip_str']))
            print(result['data'])
            print('')
            print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED+"[!]"+Fore.RESET+" Error: ", e)

def shodan_simple(busqueda):
    try:
        print(Fore.GREEN+"[+]"+Fore.RESET+"Iniciando búsqueda "+Fore.MAGENTA+"simple"+Fore.RESET)
        sleep(1.5)
        host_machine = shodus.host(results.host)
        for item in host_machine['data']:
            print(Style.BRIGHT)
            print("""[>] Port:"""+Fore.YELLOW+f"{item['port']}"+Fore.RESET + """
[>] Banner: """+Fore.YELLOW +f"{item['data']}"+Fore.RESET+"""
[>] Domains: """+Fore.YELLOW +f"{item['domains']}"+Fore.RESET+"""
    --------------------------------------------------------     
    """)
        print(Style.RESET_ALL)
    except:
        print(Fore.RED + "[-]Error" + Fore.RESET)

def shodan_avanzado(busqueda):
    try:
        print(Fore.GREEN+"[+]"+Fore.RESET+"Iniciando búsqueda "+Fore.MAGENTA+"avanzada"+Fore.RESET)
        sleep(1.5)
        host_machine = shodus.host(results.host)
        for item in host_machine['data']:
            print(Style.BRIGHT)
            print("""[>] Port:"""+Fore.YELLOW+f"{item['port']}"+Fore.RESET + """
[>] Banner: """+Fore.YELLOW +f"{item['data']}"+Fore.RESET+"""
[>] Domains: """+Fore.YELLOW +f"{item['domains']}"+Fore.RESET+"""
[>] Organization: """+Fore.YELLOW +f"{item['org']}"+Fore.RESET+"""
[>] Transport: """+Fore.YELLOW +f"{item['transport']}"+Fore.RESET+"""
    --------------------------------------------------------     
    """)
        print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED+"[!]"+Fore.RESET+" Error: ", e)


if(results.host):
    if(results.simple):
        shodan_simple(results.host)
    elif(results.advanced):
        shodan_avanzado(results.host)
    elif(results.search):
        sys.exit(1)
    else:
        print(Fore.RED+"[!]"+Fore.RESET+" Debes añadir parametro:")
        print("\tBúsqueda simple: "+Fore.MAGENTA+"-S"+Fore.RESET)
        print("\tBúsqueda avanzada: "+Fore.MAGENTA+"-A"+Fore.RESET)
    

if(results.search):
    if(results.show):
        shodan_search_ip(results.search)
    else:
        shodan_search(results.search)