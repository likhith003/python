import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
cou = 0
while True:
        if cou == 0:
            url = 'http://py4e-data.dr-chuck.net/known_by_Callia.html'
        else:
            url = tag.get('href', None)
        cou = cou +1

        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        tags = soup('a')
        count = 0
        for tag in tags:
            tag.get('href',None)
            count = count +1
            if count == 18: 
                print(tag.get('href', None))
                print ('Contents:',tag.contents[0])
                break
        url = tag.get('href', None)
        if cou ==7:
            break

    
    
