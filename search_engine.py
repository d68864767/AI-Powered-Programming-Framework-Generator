```python
import requests
from bs4 import BeautifulSoup

class SearchEngine:
    def __init__(self):
        self.base_url = "https://www.google.com/search?q="

    def search(self, query):
        # Replace spaces in the query with '+'
        query = query.replace(' ', '+')

        # Send a GET request to Google Search
        response = requests.get(self.base_url + query)

        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first search result and return its text
        result = soup.find('div', {'class': 'BNeawe'}).text

        return result
```
