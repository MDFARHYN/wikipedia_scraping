import requests
from bs4 import BeautifulSoup
import time
import re

# The URL of the Wikipedia page you want to scrape
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Start the timer to measure how long the request takes
start_time = time.time()

# Send an HTTP GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    print(f"Page fetched in {time.time() - start_time} seconds")  # Print the time taken to fetch the page
else:
    print("Unable to download the page")  # Print an error message if the request fails

# Parse the page content using BeautifulSoup and 'html.parser' to process the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the first <h1> tag (usually the title of the Wikipedia article)
h1_title = soup.find('h1').get_text().strip()  # .strip() removes any extra spaces or newlines
print("h1--->", h1_title)  # Print the extracted title

# Extract the 3rd <p> (paragraph) tag from the page
# We use nth-of-type(3) to select the 3rd paragraph, and get its text content, then clean up newlines and extra spaces
pragraph = soup.select('p:nth-of-type(3)')[0].get_text().strip().replace('\n', ' ')
print("pragraph--->", pragraph)  # Print the raw paragraph text

# Define a regular expression pattern to find and remove references like [1], [2] from the text
reg_ppattern = r'\[\d+]'

# Use re.sub() to substitute and remove any matches of the regex pattern (i.e., the reference numbers)
cleaned_pragraph = re.sub(reg_ppattern, '', pragraph)

# Print the cleaned paragraph, which now has no reference numbers
print("cleaned_pragraph--->", cleaned_pragraph)


 