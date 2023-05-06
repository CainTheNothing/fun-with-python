import requests
from bs4 import BeautifulSoup

# The URL of the One Piece Fandom Wiki page with the devil fruits
url = 'https://onepiece.fandom.com/wiki/Devil_Fruit'

# Set up headers to make the request appear as if it's coming from a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Make the request to the URL with the headers
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <li> tags within <tr> tags
li_elements = soup.select('tr li')

# Loop through the li elements and extract the devil fruit names that contain "no Mi"
devil_fruits = []
for li in li_elements:
    name = li.text.strip()
    # Remove special characters from the name
    name = name.replace('*', '').replace('≠', '')
    if "no Mi" in name:
        devil_fruits.append(name)

# Print the devil fruits that contain "no Mi"
print("List of Devil Fruits:\n")
for i, fruit in enumerate(devil_fruits, start=1):
    print(f"{i}. {fruit}")
