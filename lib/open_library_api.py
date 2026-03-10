import requests, json

class Search:
    def get_search_results(self, search_term):
        #spaces are not allowed in urls so i replace the string with +
        search_term_formatted = search_term.replace(" ", "+")
         # formats the list into a comma separated string and tells the API which data 'keys' we want back
        # output: "title,author_name"
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        #limit is set to avoid getting a massive list of books
        limit = 1
        
        #construct the full url
        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        #make the network call and convert the result to a dictionary
        response = requests.get(URL).json()
        response_formatted = f"Title: {response['docs'][0]['title']}\nAuthor: {response['docs'][0]['author_name'][0]}"
        return response_formatted
    
search_term = input("Enter a book title: ")   
result = Search().get_search_results(search_term)
print("Search Result: \n")
print(result)

