from bs4 import BeautifulSoup
import requests
import os
base = 'https://sv.dcnm.ir/Serial/Foreign/'

for season in range(1,11):
    os.mkdir(f'season{season}')
    f = open(f'./season{season}/season{season}.txt',"w")
    # there is a  problem when range reaches to 10 
    url = f'https://sv.dcnm.ir/Serial/Foreign/?dir=Friends/720/S{f"0{season}" if season<10 else season}'
    page = requests.get(url).text
    soup = BeautifulSoup(page,features="html5lib")
    links = soup.find_all('a',class_='clearfix')
    for link in links[1:] :
        print(f"{base}{link['href']}\n")
        f.write(f"{base}{link['href']}\n")
    f.close()
    
    