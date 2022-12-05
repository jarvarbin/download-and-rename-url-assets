import requests
from bs4 import BeautifulSoup
import re
import os

# Get the URL
url = input("Please enter the URL: ")

# Get the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Get all the static assets
assets = soup.find_all(src=re.compile('^(http|https)'))

# Create a folder to store the assets
domain_name = url.split('/')[2]
folder = 'assets_' + domain_name
os.mkdir(folder)

# Download the assets and rename it with a specific domain
for asset in assets:
    file_url = asset.get('src')
    file_name = file_url.split('/')[-1]
    renamed_file_name = domain_name + '_' + file_name
    full_file_path = os.path.join(folder, renamed_file_name)
    with open(full_file_path, 'wb') as f:
        response = requests.get(file_url)
        f.write(response.content)

# Save the HTML content
html_path = os.path.join(folder, domain_name + '.html')
with open(html_path, 'w') as f:
    f.write(html_content)

print("All assets have been successfully downloaded and renamed with a specific domain.")
