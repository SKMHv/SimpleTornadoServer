import urllib
from html.parser import HTMLParser
from html.entities import name2codepoint

import re # alter parser

from urllib.request import urlopen
# link URL
link = "https://kp.gov.sk/pf/_layouts/PFSharePointProject/Login.aspx?ReturnUrl=%2fpf%2f_layouts%2fAuthenticate.aspx%3fSource%3d%252Fpf%252F&Source=%2Fpf%2F"
prox = {'http': 'http://www.someproxy.com:3128'}

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a" and 'href' in attrs:
            self.links.append(attrs['href'])



try:
    urllib.request.urlopen(link, timeout=10)
    response_link = urlopen(link)
    myfile = response_link.read()
    print("Link som nacital:\n" + str(response_link.getcode()) )
    print("-----------------------")
    parser = MyHTMLParser()
    parser.feed(response_link)
    
#    input_pass = re.findall(r'<span id="ctl00_PlaceHolderMain_signInControl_LblPassword">Heslo:</span>', str(myfile))
#    data_pass = parser.handle_data(input_pass[0])
    print(parser.links)
    parser.close()

except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read()) 








