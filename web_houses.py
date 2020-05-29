import requests
import re
from bs4 import BeautifulSoup
import re
url = "https://matrix.northstarmls.com/Matrix/Public/Portal.aspx?ID=0-2540197860-10"

page = requests.get(url)


soup = BeautifulSoup(page.text , 'lxml')

''' best out put so far
for tag in range (227 , 234):
    pag = soup.find(attrs={"data-reactid" :tag})
    if pag != None:
        print(pag)
'''

#soup.find_all(attrs={"data-foo": "value"})   # search for unusual attripute
#soup.find_all(string="Elsie") # search for string
#soup.find_all(string=re.compile("Dormouse")) # search for spesific word in string
#soup.get_text() # to only get text
pag = soup.find(class_ ="j-resultsPageAsyncDisplays")

for child in pag.descendants: #to go over all tage
    if child.find("data-reactid") == -1:
    #if child.string != None:
        print(child)

#to print prices
for rows in pag.findAll(class_="col-xs-9 col-sm-8 col-lg-8 d-borderWidthRight--1 d-marginRight--7 col-md-9"):
    a = rows.get_text()
    print (a)

#better way to print prices
listings = []
for rows in pag.findAll(class_="multiLineDisplay ajax_display d26489m_show"):
    #find price location
    pre_price = rows.find(class_="col-xs-9 col-sm-8 col-lg-8 d-borderWidthRight--1 d-marginRight--7 col-md-9")
    plist = re.findall(r'\d+',pre_price.find_next().get_text()) #extract numbers
    price = int(plist[0]+plist[1]) # get integer
    others = rows.findAll(class_="d-textStrong d-paddingRight--4")#other attriputes
    bedroom = others[0].get_text()
    pathroom = others[1].get_text()
    garage = others[2].get_text()
    year = others[3].get_text()
    presize = others[4].getText().split(',') # get rid of coma
    if len(presize) > 1:
        sizea = int(presize[0]+presize[1])
    else:
        sizea = int(presize[0])
    listings.append([price,bedroom,pathroom,garage,year,sizea,round(price/sizea,1)])
#for tage in soup.findAll("p" ): #happen 'p' tags are the article
 #   print (tage.string)     # print the article's string
