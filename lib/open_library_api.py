
import requests
import json

class Search:
    def get_search_results(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")

        fields = ["title", "author"]
        fields_formatted = ",".join(fields)

        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL)
        response.raise_for_status()

        return response.json()


results = Search().get_search_results()
print(json.dumps(results, indent=1))
