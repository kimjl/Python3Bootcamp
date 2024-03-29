#http://quotes.toscrape.com
from bs4 import BeautifulSoup
import requests
from time import sleep
from random import choice

base_url = 'http://quotes.toscrape.com'

def scrape_quotes():
	all_quotes = []
	url = '/page/1'
	while url:
		response = requests.get(f'{base_url}{url}')
		#print(f'Scrapping {base_url}{url}...')
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
		#sleep(2)
	return all_quotes

def start_game(quotes):
	quote = choice(quotes)
	remaining_guesses = 4
	guess = ''
	print('Here is a quote:')
	print(quote['text'])
	# print(quote['author'])

	while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
		guess = input(f'Who said this quote? Guesses remaining: {remaining_guesses}\n')
		remaining_guesses -= 1

		if guess.lower() == quote['author'].lower():
			print('You got it right!')
			break

		if remaining_guesses == 3:
			response = requests.get(f"{base_url}{quote['bio-link']}")
			soup = BeautifulSoup(response.text, 'html.parser')
			birth_date = soup.find(class_='author-born-date').get_text()
			birth_place = soup.find(class_='author-born-location').get_text()
			print(f'Here is a hint: The author was born on {birth_date} {birth_place}')
		elif remaining_guesses == 2:
			first_initial = quote['author'][0]
			print(f"The author's first name starts with {first_initial}")
		elif remaining_guesses == 1:
			last_initial =  quote['author'].split(' ')[1][0]
			print(f"The author's last name starts with {last_initial}")
		else:
			print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

	again = ''
	while again.lower() not in ('y', 'yes', 'n', 'no'):
		again = input('Would you like to play again? [y/n]')
	if again.lower() in ('yes', 'y'):
		return start_game(quotes)
	else:
		print("Ok, bye!")

quotes = scrape_quotes()
start_game(quotes)