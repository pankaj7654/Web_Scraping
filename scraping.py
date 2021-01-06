import requests 
from bs4 import BeautifulSoup 
import csv 
   
#Here in URL we can use any link of website for copy of that website table data.
url = "https://www.website.com"
agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
page = requests.get(url, headers=agent)
htmlContent = page.content
   
soup = BeautifulSoup(htmlContent, 'html5lib') 
spacification = soup.prettify()  

#heading = soup.find('h2')
#print(heading.prettify())

filename = 'filename.csv'

csv_writer = csv.writer(open(filename,'w'))

#run a for loop to extract the data and store it in csv file

for tr in soup.find_all('tr'):
    print(tr)
    data = []
    #for extracting the table heading will execute only once

    for th in tr.find_all('th'):
        data.append(th.text)
        print(th)
    if data:
        print("inserting headers:{}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    #for scraping the actual table data values 
    for td in tr.find_all('td'):
        data.append(td.text.strip())
    if data:
        print("inserting table data:{}".format(','.join(data)))
        csv_writer.writerow(data)



