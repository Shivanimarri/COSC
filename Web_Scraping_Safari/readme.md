This script scrapes the top 5 trending repositories from GitHub Trending using Python, and saves the results to a CSV file.

🧠 What the Script Does
Uses the requests library to fetch the GitHub Trending page.

Parses the HTML using BeautifulSoup (from bs4).

Extracts the top 5 repository names and their GitHub links.

Writes the results into a CSV file named trending_repos.csv