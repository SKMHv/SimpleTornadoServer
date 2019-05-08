import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup


# link URL
link = "https://kp.gov.sk/pf/_layouts/PFSharePointProject/Login.aspx?ReturnUrl=%2fpf%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252Fpf%252F&Source=%2Fpf%2F"
prox = {'http': 'http://www.someproxy.com:3128'}


try:
    urllib.request.urlopen(link, timeout=10)
    response_link = urlopen(link)
    
    soup = BeautifulSoup(response_link.read())
    print("Som na stranke: " + soup.find('title').text.strip())
    
    if soup.find("input", {"id": "ctl00_PlaceHolderMain_signInControl_Password"}):
        print("HTML obsahuje password input")
    
    else:
        print("HTML neobsahuje password input")
    

except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read()) 


