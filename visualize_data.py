import pandas as pd
import matplotlib.pyplot as plt

# Wikipedia page URL
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

# Scrape the table using pandas
tables = pd.read_html(url)

# Extract the first table (usually the most relevant one)
df = tables[0]

# Clean the data: Remove any rows with missing 'Population' data
df = df.dropna(subset=['Population'])

# Ensure 'Population' column is treated as string, then remove commas and convert to integers
df['Population'] = df['Population'].astype(str).str.replace(',', '').str.extract('(\d+)').astype(int)

# Select the top 10 countries by population
top_10 = df[['Location', 'Population']].head(10)  # Use 'Location' as the country name

# Plot a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_10['Location'], top_10['Population'], color='skyblue')

# Add labels and title
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Top 10 Most Populated Countries')
plt.xticks(rotation=45)  # Rotate country names for better readability
plt.tight_layout()  # Adjust layout to prevent label cutoff

# Show the plot
plt.show()
