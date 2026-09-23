import json
import requests


class Search_book:

    def retrieve_book_from_api(self,query):
  
        formatted_searched_book = query.replace(" ","+")

        search_fields = ["title","author_name","first_publish_year"]
        formatted_fields = ",".join(search_fields)

        api_url=f"https://openlibrary.org/search.json?title={formatted_searched_book}&fields={formatted_fields}&limit=1"

        res = requests.get(api_url).json()
        """{json.dumps(res,indent=1)}"""

        return f"""

            Book title: {res['docs'][0]['title']}
            Author's name: {res['docs'][0]['author_name'][0]}
            Year of publish: {res['docs'][0]['first_publish_year']}

        """

    def retrieve_more_than_one_book(self,query):
        formatted_query=query.replace(" ","+")
        fields=["title","author_name"]
        formatted_fields=",".join(fields)
        api_url=f"https://openlibrary.org/search.json?title={formatted_query}&fields={formatted_fields}&limit=2"
        response = requests.get(api_url).json()

        return response['docs']

result = Search_book()
query = input("Enter the book title >> ")
book = result.retrieve_book_from_api(query)
print(book)


books=result.retrieve_more_than_one_book(query)
for book in books:
    print(f"""
        Title of the book; {book['title']}
        Author of the book; {book['author_name'][0]}
    """)
