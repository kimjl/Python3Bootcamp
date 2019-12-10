import requests
import colorama
from termcolor import colored
import pyfiglet
from random import choice

colorama.init()
#Display Title
ascii_msg = pyfiglet.figlet_format('Dad Joke Generator')
colored_ascii = colored(ascii_msg, color='white')
print(colored_ascii)

url = 'https://icanhazdadjoke.com/search'
user_input = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
	url, 
	headers={'Accept': 'application/json'},
	params={'term': user_input}
).json()

num_jokes = response['total_jokes']
results = response['results']
if num_jokes > 1:
	print(f'There are {num_jokes} {user_input} jokes')
	print(choice(results)['joke'])
elif num_jokes == 1:
	print(f'There is only one {user_input} joke')
	print(results[0]['joke'])
else:
	print(f'There are no {user_input} jokes')

# print(results[0]['joke'])