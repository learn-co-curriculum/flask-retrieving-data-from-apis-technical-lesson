import requests
import json

class Search:
    def get_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        try:
            response = requests.get(URL).json()
            response_formatted = f"Title: {response['docs'][0]['title']} \n Author: {response['docs'][0]['author_name'][0]}"
            return response_formatted
        except IndexError as er:
            print(f"There is an fetching request: {er}")

search_term = input("Enter a book title: ")
results = Search().get_search_results(search_term)
print(json.dumps(results, indent=1))