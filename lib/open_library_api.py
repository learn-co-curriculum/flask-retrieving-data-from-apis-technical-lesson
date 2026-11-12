import requests
import json

class Search:
    def get_search_results(self,search_term):
        
        search_term_formatted=search_term.replace(" ", "+")
        fields=["title","author_name"]
        # formats the list into a comma separated string
        # output: "title,author_name"
        fields_formatted=",".join(fields)
        limit=1

        url=f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response=requests.get(url).json()
        response_formatted=f"Title: {response['docs'][0]['title']}\n Author:{response['docs'][0]['author_name'][0]}"
        return response_formatted

search_term = input("Enter a book title: ")


result = Search().get_search_results(search_term)
print("Search Result: \n")
print(result)