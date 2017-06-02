from urllib import urlencode
from bs4 import BeautifulSoup

import re
import requests

GOOGLE_SEARCH = 'https://www.google.co.in/search?'
BASE_URL = 'https://www.google.co.in'


def filter_text(data):
    """ filter text based on regular expression """
    regex = re.compile(r'href')
    links = regex.findall(str(data))
    print len(links)


def preetify_html(text):
    """ prettify the html data for better reading """
    preetify_data = BeautifulSoup(text, "html.parser")
    return preetify_data


def main():
    """ Driver function """
    search_text = {'q': 'very funny PJ\'s'}
    query_text = urlencode(search_text)
    SEARCH_QUERY = GOOGLE_SEARCH + query_text
    res = requests.get(SEARCH_QUERY)
    data = preetify_html(res.text)
    filter_text(data)


if __name__ == '__main__':
    main()
