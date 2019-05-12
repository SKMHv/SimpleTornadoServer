import requests, sys
import os.path
from bs4 import BeautifulSoup
from datetime import datetime
from dataclasses import replace
from turtledemo.clock import datum
import eMail_notification
from _datetime import date

# ==============================================================================================

form_data = {
    '__LASTFOCUS':'',
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE':'/wEPDwULLTEzNjQzNDMwODMPZBYCZg9kFgICAQ9kFgQCAQ9kFgICBQ9kFgJmD2QWAgIBDxYCHgRUZXh0BQxQcmlobMOhc2VuaWVkAgMPZBYKAgMPFgIeB1Zpc2libGVoZAIFDxYCHwFoZAIJD2QWAgIBDxYCHwAFDFByaWhsw6FzZW5pZWQCCw9kFgQCAQ8WAh8ABRlQYXJ0bmVyIGZyYW1ld29yayBwb3J0w6FsZAIDDxYCHwAF2wFVcG96b3JuZW5pZTogVMOhdG8gc3Ryw6Fua2EgbmllIGplIHphxaFpZnJvdmFuw6EgcHJlIHphYmV6cGXEjWVuw7oga29tdW5pa8OhY2l1LiBNZW7DoSBwb3XFvsOtdmF0ZcS+b3YsIGhlc2zDoSBhIG9zdGF0bsOpIGluZm9ybcOhY2llIHNhIGJ1ZMO6IG9kb3NpZWxhxaUgYWtvIG9iecSNYWpuw70gdGV4dC4gxI5hbMWhaWUgaW5mb3Jtw6FjaWUgdsOhbSBwb3NreXRuZSBzcHLDoXZjYS5kAg0PFgIfAWgWAgIBDw8WAh4ISW1hZ2VVcmwFIS9fbGF5b3V0cy8xMDUxL2ltYWdlcy9jYWxwcmV2LnBuZ2RkZNxzwfD0EvoEa4JGrtqimJbYRwND',
    '__VIEWSTATEGENERATOR':'6D812879',
    '__EVENTVALIDATION':'/wEWBQL4oZfuCgKepvWvAQLJ6fSGCQLZv4jIAQKnnOKvCxHQSvpmeomX82MeDsKLLWVO/u13',
    'ctl00$PlaceHolderMain$signInControl$UserName':'upvs.dwcslovakia',
    'ctl00$PlaceHolderMain$signInControl$Password':'dWC89*kso39',
    'ctl00$PlaceHolderMain$signInControl$submitLoginBtn':'Prihlásiť'
    }

req_headers = {
    'Host': 'kp.gov.sk',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://kp.gov.sk/pf/_layouts/PFSharePointProject/Login.aspx?ReturnUrl=%2fpf%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252Fpf%252F&Source=%2Fpf%2F',
    'Connection': 'keep-alive'    
    }



prox = {'http': 'http://www.someproxy.com:3128'}


def loger(text):
    """
    Do lokalneho suboru zapise pozadovany text s aktualnym obsahom
    """
    if  os.path.isfile("logs.txt"):
        with open("logs.txt", 'r') as file_a:
            a = file_a.read()+"\n"
        with open("logs.txt", 'w') as file_b:
            file_b.write(a)
            file_b.write(str(datetime.now())+ " -> "+text)
    else:
        with open("logs.txt", 'w') as file_b:
                file_b.write(text)
        
def porovnaj(new, last="oznamy.txt"):
    """
    Funkcia porovna obsah new s obsahom v last="oznamy.txt",
    ak subor v last existuje a jeho obsah sa zhoduje s obshom v new, 
    tak sa program ukonci. Ak sa nezhoduju, tak sa obsah z new zapise do last.      
    """
    if os.path.isfile(last) and new == open(last, 'r').read():
        print("\nObsahy sa zhoduju. Ukoncujem program....")
        sys.exit()
    else:
        with open(last, 'w') as file_o:
            print("\nObsahy sa nezhoduju idem prepisat povodny obsah.")
            file_o.write(new) 
            loger("Do 'oznamy.txt' som zapisal nove Oznamy ....")

def notifi_oznamy(URL = "https://kp.gov.sk/pf/_layouts/PFSharePointProject/Login.aspx?ReturnUrl=%2fpf%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252Fpf%252F&Source=%2Fpf%2F"):    
    """
    Funkcia sa prihlasi do portalu Partner Framework Portal nacita si oznamy zo stranky oznamy, 
    porovna ich nadpisy a casy upravenia s povodnou verziou 'oznamy.txt', ak sa zhoduju, tak sa ukonci program, 
    ak sa nezhoduju, tak sa zapise nova verzia Nadpisou a casov do 'oznamy.txt' nasledne sa z kazdeho 
    oznamu nacitaju potrebne atributy, vysklada sa HTML tabulka s oznamami a odosle sa email s tabulkou oznamov.   
    """
    try:
        with requests.Session() as s:
            p = s.post(URL, data=form_data, headers=req_headers)
            p = s.get("https://kp.gov.sk/pf/Lists/Oznamy")
            soup = BeautifulSoup(p.text)
            loger("Nacital som stranku ... https://kp.gov.sk/pf/Lists/Oznamy")
            
            print("Som na stranke: " + soup.find('title').text.strip())
            oznamy = soup.find_all("tr", {"class": "ms-alternating ms-itmhover", "class":"ms-itmhover"}) 
            print("Pocet oznamov na stranke: ", len(oznamy))
            print("=============================================")
            
            text_oznamy = []
            for j in oznamy:
                text_oznamy.append(j.text)
            print("\n".join(text_oznamy))
            porovnaj("\n".join(text_oznamy),last="oznamy.txt")       
                     
            oznamy_url = []
            table_data = []
            html_oznam = []
            table = []
            
            html_oznam.append("<h1>Notifikacia oznamov ....</h1>\n")
            
            for i in oznamy:
                predmet_oznamu = i.find("a",{"onfocus":"OnLink(this)"}).text.strip()
                datum_oznamu = i.find("nobr").text.strip()
                datum_oznamu = datum_oznamu.replace(". ", ".")
                url_oznamu = i.find("a", href=True).get("href")
                
                if url_oznamu:
                    oznamy_url.append(url_oznamu)
                    p = s.get(url_oznamu)
                    soup = BeautifulSoup(p.text)
                    
                    nadpis_oznamu = soup.find("td", {"id":"SPFieldText"}).text.strip()
                    text_oznamu = soup.find("div", {"class":"ms-rtestate-field"}).text.strip()
                    koniec_oznamu = soup.find("td", {"id":"SPFieldDateTime"}).text.strip().replace(". ", ".")
                    #vytvoril_oznam = soup.find("a", {"onclick":"GoToLinkOrDialogNewWindow(this);return false;"}).text.strip()
                    vytvoril_dna = soup.find("span", {"id":"ctl00_m_g_d75f40a2_19e3_49ce_9df0_870bf5e6fac7_ctl00_toolBarTbl_RptControls_ctl00_ctl00_ctl00"}).text.strip()
                    #aktualizoval_zmenu = soup.find("a", {"onclick":"GoToLinkOrDialogNewWindow(this);return false;"}).text.strip()
                    aktualizoval_dna = soup.find("span", {"id":"ctl00_m_g_d75f40a2_19e3_49ce_9df0_870bf5e6fac7_ctl00_toolBarTbl_RptControls_ctl00_ctl00_ctl01"}).text.strip()
                    
                    # -------- HTML TABLE DATA ----------
                    table_data.append(["Nadpis", nadpis_oznamu])
                    table_data.append(["Vytvoril", vytvoril_dna])
                    table_data.append(["Aktualizoval", aktualizoval_dna])
                    table_data.append(["Koniec oznamu", koniec_oznamu])
                    table_data.append(["URL oznamu", url_oznamu])
                    
                    table.append("<table style='text-align: left; width: 100%;' border='1' cellpadding='2'cellspacing='2'>\n")
                    table.append("<tbody>\n")
                    
                    
                    for i in table_data:
                        table.append("\t<tr>\n")
                        td = []
                        for j in range(1):
                            td.append("<td style='width: 150px;'><strong>{}</strong></td>".format(i[0]))
                            td.append("<td style='width: 500px;'>{}</td>".format(i[1]))
                        
                        table.append("\t\t"+"".join(td))
                        table.append("\n\t</tr>\n")
                    
            
                    table.append("<tr>\n")
                    table.append("<td colspan='2' rowspan='1' style='vertical-align: top;'>{}<br>\n".format(text_oznamu))
                    table.append("</td>\n")
                    table.append("</tr>\n")
                    
                    table.append("</tbody>\n")
                    table.append("</table>\n")
                    table.append("<p>&nbsp;</p>\n")
                    
                    table_data = []
                    # ------------------------------------
                            
                
                else:
                    print("Odkaz oznamu '{}' z datumu '{}' sa nenasiel!" .format(predmet_oznamu,datum_oznamu))
                    
            html_oznam.append("".join(table))
            html_oznam = "".join(html_oznam)
            return html_oznam
            
               
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def notifi_odstavky(URL = "https://kp.gov.sk/pf/_layouts/PFSharePointProject/Login.aspx?ReturnUrl=%2fpf%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252Fpf%252F&Source=%2Fpf%2F"):
    try:
        
        aktual_datum = datetime.now().strftime("%-d.%-m.%Y")
        print("Aktualny datum ... ", aktual_datum)
        url_odstaviek = ["https://kp.gov.sk/pf/SitePages/technicke-odstavky-fix.aspx", "https://kp.gov.sk/pf/SitePages/technicke-odstavky.aspx"]
        
        for u in url_odstaviek:   
            with requests.Session() as s:
                p = s.post(URL, data=form_data, headers=req_headers)
                p = s.get(u)
                soup = BeautifulSoup(p.text)
                loger("Nacital som stranku ... {}".format(u))
                title_url = soup.find("title").text.strip()                    
                print("Som na stranke: " + title_url)                            
                tabulky_odstavok = soup.find_all("table", {"class":"ms-rteFontSize-1 ms-rteTable-default", "class":"ms-rteTable-default"})
                
                k = 0
                for o in tabulky_odstavok:
                    k += 1
                    odstavky = o.find_all("tr")
                    print("V tabulke {}. - pocet odstavok: {}".format(k,len(odstavky)))    
                
                
                    for r in odstavky: 
                        datum_odstavky = r.find("th", {"class":"ms-rteThemeForeColor-2-2 ms-rteTableFirstCol-default", "class":"ms-rteTableFirstCol-default"})
                        
                        if datum_odstavky:
                            datum_odstavky = datum_odstavky.text.strip().replace(". ", ".")
                            #print(datum_odstavky)
                            
# idem vytriedit odstavky za aktualny rok           
                            odstavky_aktualrok = []                  
                            if datum_odstavky.find(".2019") != -1:
                                print(datum_odstavky)
                                odstavky_aktualrok.append(r)
                            
                        #print("-------------------------------------------------------------")
                
                
                print("=============================================")
             
    except Exception as e:
        print(e)

    

# ==============================================================================================
# odosli mailom
sender_email = "michal.hvila@gmail.com"
receiver_email = "hvila.michal@gmail.com"   
subject_email = "Notifikacia oznamov z NASES ...."

notifi_odstavky()       
#mail_a = eMail_notification.Email(subject_email, sender_email, receiver_email, notifi_oznamy())
#mail_a.odosli()

#loger("Notifikacny email s oznamom bol odoslany ...")
# xlbwwvmcortykbci     

