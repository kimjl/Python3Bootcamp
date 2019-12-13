#http://quotes.toscrape.com
from bs4 import BeautifulSoup
import requests

all_quotes = []
base_url = 'http://quotes.toscrape.com'
url = '/page/1'

while url:
	response = requests.get(f'{base_url}{url}')
	print(f'Scrapping {base_url}{url}...')
	soup = BeautifulSoup(response.text, 'html.parser')
	quotes = soup.find_all(class_='quote')

	#store quotes in a list of dictionaries
	for quote in quotes:
		all_quotes.append({
			'text': quote.find(class_='text').get_text(),
			'author': quote.find(class_='author').get_text(),
			'bio-link': quote.find('a')['href'],
		})

	#find the next button to continue scrapping for quotes
	next_btn = soup.find(class_='next')
	url = next_btn.find('a')['href'] if next_btn else None
print(all_quotes)
