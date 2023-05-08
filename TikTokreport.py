import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()
print(Fore.GREEN + """ 
print("a report is sent every 10 seconds")
print("")
print("")

x = input('Enter the request URL from Inspect Element: ')
print("")
print("")

print('Reporting...')
print('')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('reported :D')

    time.sleep(10)


input()

