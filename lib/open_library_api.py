import requests
import json

class Search:
  def get_search_results(self,search_term):
    
      
    search_term_formatted = search_term.replace(" ","+")
    fields =["title","author_name"]
    fields_formatted = ",".join(fields)
    limit = 1
    URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
    response = requests.get(URL)
    return response.json()
search_term = input("Enter a book title: ")
results_json = Search().get_search_results(search_term)  
print(json.dumps(results_json,indent=4))
