#Chap09_ChatGPT로생성한_네이버신문기사검색.py 
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# Request the page
response = requests.get(url)
response.raise_for_status()  # Raise an exception if the request was unsuccessful

# Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Find and print article titles
titles = soup.find_all('a', class_='news_tit')
article_titles = [title.get_text() for title in titles]

# Print the article titles
for i, title in enumerate(article_titles, 1):
    print(f"{i}. {title}")
