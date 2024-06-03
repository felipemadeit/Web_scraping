import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


# Create your views here.


def scrape_website(url):

    # Make a get request to the url
    response = requests.get(url)

    # if have a ok status
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser') 

        title = soup.text.title()

        print(title)
        
    # if something goes wrong
    else:
        print("Error",  response.status_code)
    
    

scrape_website('https://www.ktronix.com/')