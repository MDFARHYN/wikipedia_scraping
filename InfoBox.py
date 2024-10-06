import requests
from bs4 import BeautifulSoup

# Wikipedia page URL
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Fetch the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the infobox table (usually has class "infobox")
    infobox = soup.find('table', {'class': 'infobox'})

    # Find all rows within the infobox
    rows = infobox.find_all('tr')

    # Loop through rows and extract header (th) and data (td)
    for row in rows:
        header = row.find('th')  # Header cell (like "Developer")
        data = row.find('td')    # Data cell (like "Python Software Foundation")

        if header and data:
            print(f"{header.get_text(strip=True)}: {data.get_text(strip=True)}")
else:
    print("Failed to fetch the page")
