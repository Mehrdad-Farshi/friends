from bs4 import BeautifulSoup
import requests
base = 'https://sv.dcnm.ir/Serial/Foreign/'

for season in range(1,11):
    f = open(f'season{season}',"w")
    url = f'https://sv.dcnm.ir/Serial/Foreign/?dir=Friends/720/S0{season}'
    page = requests.get(url).text
    soup = BeautifulSoup(page,features="html5lib")
    links = soup.find_all('a',class_='clearfix')
    for link in links[1:] :
        print(f"{base}{link['href']}\n")
        f.write(f"{base}{link['href']}\n")
    f.close()