

import json 
import requests
from bs4 import BeautifulSoup

URL ="https://www.codewithharry.com/"
r = requests.get(URL)
value = r.content

soup = BeautifulSoup(value, 'html.parser')

orderList = []
dicts ={}
listData = soup.find_all('li')

for i in listData:
    orderList.append(i.get_text())

# Data with frequency        
for i in orderList:  
    dicts[i]=dicts.get(i,0)+1   


# Unique data(non-repeated)
uniqueData =[]
for i in dicts:
    if dicts[i] == 1:
        uniqueData.append(i)
print(uniqueData)    

# json format Data
json_object = json.dumps(dicts, indent = 4) 
print(json_object)

    
    
