# Needed packages: BeautifulSoup, time, Requests, Date, termcolor
from cgitb import text
from pkg_resources import resource_stream
import requests
import time
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from termcolor import colored
import re


print("\n##### RuzGer's MAL parser #####")
print("## https://github.com/RuzsaGergely/ ##\n")

while True:
    try:
        print("ID of Genre (eg. 27 is Shonuen) [Default is 27]:")
        GENRE = int(input() or "27")
    except ValueError:
        print(colored("Sorry, I didn't catch it...", 'red'))
        continue
    else:
        break

while True:
    try:
        print("Start of the pages [default 1]: ")
        PAGEFROM = int(input() or "1")
    except ValueError:
        print(colored("Sorry, I didn't catch it...", 'red'))
        continue
    else:
        break

while True:
    try:
        print("End of the pages [default 20]: ")
        PAGETO = int(input() or "20")
    except ValueError:
        print(colored("Sorry, I didn't catch it...", 'red'))
        continue
    else:
        break

while True:
    try:
        print("Minimum number of episodes [default 24]: ")
        MINEPS = int(input() or "24")
    except ValueError:
        print(colored("Sorry, I didn't catch it...", 'red'))
        continue
    else:
        break

while True:
    try:
        print("Maximum number of episodes [default 1000]: ")
        MAXEPS = int(input() or "1000")
    except ValueError:
        print(colored("Sorry, I didn't catch it...", 'red'))
        continue
    else:
        break

URL = "https://myanimelist.net/anime/genre/" + str(GENRE) + "/?page="

array_epsnum = []
array_title = []
array_output = []

for x in range(PAGEFROM, PAGETO+1):
    URLmod = str(URL) + str(x)
    print(colored("Currently being processed: " + str(URLmod), 'yellow'))
    response = requests.get(URLmod)
    soup = BeautifulSoup(response.text, 'html.parser')

    cards = soup.find_all('div', {"class": "js-anime-category-producer"})
    for res in cards:
        for res2 in res.find_all('a', {"class": "link-title"}):
            array_title.append(res2.text.strip())
    for res in cards:
        for res2 in res.find_all('span',text=re.compile('.*ep.*')):
            array_epsnum.append(res2.text.strip().split(' ')[0])

array_epsnum = [w.replace('?', '0') for w in array_epsnum]

file = open("G"+str(GENRE) + "_" + str(datetime.now().strftime("%d_%m_%Y_%H_%M_%S")) + ".txt", "w", encoding="utf-8")
if(len(array_epsnum) == len(array_title)):
    print(colored("Episodes: " + str(len(array_epsnum)) + " Titles: " + str(len(array_title)) + " - Everything is good in my arrays :)", 'green'))
    try:
        for tit, eps in zip(array_title, array_epsnum):
            try:
                if(MINEPS <= int(eps) <= MAXEPS):
                    #print(tit + " -- " + eps)
                    array_output.append(tit + " -- " + eps)
            except:
                pass
    except:
        pass
else:
    print("Episodes: " + str(len(array_epsnum)) + " Titles: " + str(len(array_title)))
    print(colored("The numbers are not equal, something went wrong... I'm so sorry... :(", 'red'))

print(colored("\nWriting results out...", 'white'))

try:
    file.write("#### RuzGer's MAL Parser ####\n")
    file.write("Genre ID: " + str(GENRE) + " Number of find titles: " + str(len(array_title)) + " Fitted titles: " + str(len(array_output))+" Timestamp: " + str(datetime.now().strftime("%d_%m_%Y_%H_%M_%S")) + "\n\n")

    for x in array_output:
        try:
            file.write(str(x) + "\n")
        except:
            pass
    print(colored("Result writed out!\n", 'green'))
except:
    print(colored("Something went wrong... :(\n", 'red'))
    exit()
