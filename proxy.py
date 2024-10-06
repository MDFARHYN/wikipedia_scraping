import requests
import logging
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Proxy setup (replace with your proxy details)
proxies = {
   
    'https': 'https://username:password:server_name:port'
}

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

try:
    # Send request through a proxy
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # Check if the request was successful
    logging.info(f"Successfully fetched the page: {url} using proxy")
except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching the page with proxy: {e}")
    exit()

# Parse the content
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.string)  # Example: print the title of the page
