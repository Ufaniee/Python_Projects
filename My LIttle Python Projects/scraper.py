#Creating an endless scraper
#Alright, let's make the scraper actually scrape the new link.
#To do this we move everything into a scrapeWikiArticle function

import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
	response = requests.get(
		url=url,
	)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title)

	allLinks = soup.find(id="bodyContent")
	linkToScrape = 0

	for link in allLinks:
		# We are only interested in other wiki articles
		if link['href'].find("/wiki/") == -1: 
			continue

		# Use this link to scrape
		linkToScrape = link
		break

	scrapeWikiArticle("https://twitter.com/anie_ufan" + linkToScrape['href'])
