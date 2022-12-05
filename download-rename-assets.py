import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

#url of the domain
domain = "http://example.com/"

#specify the name for renamed assets
prefix = "example_"

#get the html of the domain
res = requests.get(domain)

#create a beautiful soup object
soup = BeautifulSoup(res.text, "html.parser")

#find all elements with src attribute
for element in soup.find_all(src=True):
    #get the source of the element
    src = element['src']
    
    #extract the name of the asset
    asset_name = src.split("/")[-1]
    
    #rename the asset
    asset_name = prefix + asset_name
    
    #construct the url of the asset
    asset_url = urljoin(domain, src)
    
    #download the asset
    asset_res = requests.get(asset_url)
    
    #write the asset to the file
    with open(asset_name, "wb") as f:
        f.write(asset_res.content)

print("All assets have been downloaded and renamed.")
