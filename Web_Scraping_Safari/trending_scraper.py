import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the trending page
url = "https://github.com/trending"
response = requests.get(url)

# Step 2: Parse HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract top 5 repository names and links
repos = soup.find_all('article', class_='Box-row')[:5]

repo_data = []

for repo in repos:
    # Extract repo name (e.g., "username/repo-name")
    full_name = repo.h2.a.get_text(strip=True).replace(' / ', '/')
    
    # Construct full link
    link = "https://github.com" + repo.h2.a['href']
    
    repo_data.append([full_name, link])

# Step 4: Save to CSV
with open('trending_repos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Repository Name', 'Link'])  # Header
    writer.writerows(repo_data)

print("✅ Top 5 trending repositories saved to 'trending_repos.csv'")
