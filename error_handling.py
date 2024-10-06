import requests
import logging
from bs4 import BeautifulSoup

# Set up logging to log to a file
logging.basicConfig(filename='scraping.log', 
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

url = 'https://easasasnasasasaswikipedia.orasasag/wiki/Python_(programming_language)'

try:
    # Fetch the webpage
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad requests
    logging.info(f"Successfully fetched the page: {url}")
except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching the page: {url} | {e}")
    exit()

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Safely find an element and log if missing
infobox = soup.find('table', {'class': 'infobox'})
if infobox:
    logging.info("Infobox found!")
else:
    logging.warning("Infobox not found!")
