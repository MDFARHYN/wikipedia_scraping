import pandas as pd
import sqlite3

# Wikipedia page URL
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

# Scrape the table using pandas
tables = pd.read_html(url)

# Extract the first table (usually the most relevant one)
df = tables[0]

# Clean the data: Remove any rows with missing 'Population' data
df = df.dropna(subset=['Population'])

# Ensure 'Population' column is treated as string, then remove commas and convert to 64-bit integers
df['Population'] = df['Population'].astype(str).str.replace(',', '').str.extract('(\d+)').astype('int64')

# Select relevant columns
df = df[['Location', 'Population']]

# Connect to SQLite (or create the database if it doesn't exist)
conn = sqlite3.connect('wikipedia_data.db')

# Store the data in a new table called 'countries_population'
df.to_sql('countries_population', conn, if_exists='replace', index=False)

# Confirm the data is stored by querying the database
result_df = pd.read_sql('SELECT * FROM countries_population', conn)
print(result_df.head())

# Close the connection
conn.close()
