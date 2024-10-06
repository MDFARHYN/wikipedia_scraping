import pandas as pd

# Wikipedia page URL
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

# Use pandas' read_html to scrape all tables from the page
tables = pd.read_html(url)

# Check how many tables were found
print(f"Total tables found: {len(tables)}")

# Display the first table
df = tables[0]
print(df.head())

# Save the DataFrame to a CSV file 
df.to_csv('wikipedia_data.csv', index=False)