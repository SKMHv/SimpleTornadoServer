import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

# link URL
link1 = "https://reality.bazos.sk/predam/dom/?hledat=&rubriky=reality&hlokalita=82105&humkreis=15&cenaod=&cenado=200000&Submit=H%C4%BEada%C5%A5&kitx=ano"
dnes = datetime.now()

try:
    # urllib.request.urlopen(link1, timeout=10)
    response_link = urlopen(link1)
    soup = BeautifulSoup(response_link.read())
    
    print("Som na stranke: " + soup.find('title').text.strip())
    
    vypisy = soup.find_all("span", {"class": "vypis"}) 
    print("Pocet vypisov na stranke: ", len(vypisy))
    
    vypisy_dnes = []
    vypisy_url = []
    for i in vypisy:
        #soup_vypis = BeautifulSoup(i.read())
        #print(i.find("span", {"class": "velikost10"}).text)
        span_dnes = i.find("span", {"class": "velikost10"}).text
    
        if span_dnes.find(dnes.strftime("%-d")+'.'+ dnes.strftime("%-m")+".")!= -1:
            #print(span_dnes)
            vypisy_dnes.append(span_dnes)
            vypis_a = i.find("a", href=True)
            #print(vypis_a["href"])
            vypisy_url.append("https://reality.bazos.sk" + vypis_a["href"])
            
            
    print("Pocet vypisov za dnesni den: ", len(vypisy_url))
    print("===============================================")
    
    
    # reporty za dnesny den 
    
    for v in vypisy_url:
        response_link = urlopen(v)
        soup = BeautifulSoup(response_link.read())
        title = soup.find('title').text.strip()
        popis = soup.find("div", {"class": "popis"}).text.strip()
        listadvlevo = soup.find("td", {"class": "listadvlevo"})
        cena = listadvlevo.find_all("tr")[3].find_all("td")[1].text.strip()  
        
        print("VYPIS z URL: ", v)
        print("TITLE:   ", title)
        print("POPIS:   ", popis)
        print("CENA:    ", cena)
        print('----------------------------------------')
     
    

except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read()) 


