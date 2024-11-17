import requests
import string, json, requests, random
from os import system
from time import sleep
import socket
import time
from pystyle import Colorate, Colors, Center


print(Colorate.Horizontal(Colors.red_to_blue, """

██╗   ██╗██╗██████╗ ██╗   ██╗███████╗   ███████╗██╗  ██╗███████╗
██║   ██║██║██╔══██╗██║   ██║██╔════╝   ██╔════╝╚██╗██╔╝██╔════╝
██║   ██║██║██████╔╝██║   ██║███████╗   █████╗   ╚███╔╝ █████╗  
╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║   ██╔══╝   ██╔██╗ ██╔══╝  
 ╚████╔╝ ██║██║  ██║╚██████╔╝███████║██╗███████╗██╔╝ ██╗███████╗
  ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                          
"""))

print(Colorate.Horizontal(Colors.red_to_blue, "================================================================"))
print(Colorate.Horizontal(Colors.red_to_blue, '                         made by flacis '))
print(Colorate.Horizontal(Colors.red_to_blue, "================================================================"))


rainbow_colors = [
    '\033[31m', 
    '\033[38;5;214m',
    '\033[33m',
    '\033[32m', 
    '\033[34m', 
    '\033[38;5;57m',
    '\033[35m',  
    '\033[0m' 
]

print('                                                                                                                 ')
how_much_code = int(input(Colorate.Horizontal(Colors.red_to_blue,"How much code do you want me to inject to your PC?: ")))
are_you_sure = input(Colorate.Horizontal(Colors.red_to_blue,"Are you sure? (LAST CHANCE): "))

host_name = socket.gethostname() 
ip_address = socket.gethostbyname(host_name) 

if are_you_sure.lower() == "yes":      
        for i in range(how_much_code):
            time.sleep(0.03)
            
            color = rainbow_colors[i % len(rainbow_colors)]

            print(f"{color}LOL GET HACKED {host_name}, YOUR IP IS {ip_address}\033[0m")
    
elif are_you_sure.lower() == "no":
        for i in range(how_much_code):
            time.sleep(0.03)

            color = rainbow_colors[i % len(rainbow_colors)]
            
            print(f"{color}HOW DARE YOU SAY NO TO ME {host_name}! Your IP is {ip_address} \033[0m")