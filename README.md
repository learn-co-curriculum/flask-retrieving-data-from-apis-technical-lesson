# Technical Lesson: Retrieving data from an API

## Introduction 

Different APIs expose their data and functionalities in different ways. However, there are commonalities among them and there are common approaches that we'll discuss here. Generally speaking, there are two main uses for APIs––getting data and adding functionality (i.e. signing in with Facebook or posting to Instagram). We'll be discussing the "getting data" part of working with APIs here.
<br /><br />
Many APIs are built on what is referred to as a RESTful framework. That means that the "endpoints", or URLs to which we can send a request for data, follow certain conventions. These URLs should allow you to request information, send information, update information and delete information. Let's focus on the "getting information" request.

## Scenario

You are working to build an app where users can search for books and look up information on them. We can make a custom request to the Open Library API for the exact information we want to present to the user.

## Tools & Resources 
- [GitHub repo](https://github.com/learn-co-curriculum/flask-retrieving-data-from-apis-technical-lesson)
- [Flask](https://flask.palletsprojects.com/en/stable/quickstart)
- [Open Library API](https://openlibrary.org/dev/docs/api/search)
- [GET - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [HTTP methods - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [requests](https://requests.readthedocs.io/en/latest/)
- [Python JSON](https://docs.python.org/3/library/json.html)

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson: 
* Fork and Clone
  * For this lesson, you will need the following [GitHub Repo](https://github.com/learn-co-curriculum/flask-retrieving-data-from-apis-technical-lesson)
  * Go to the provided GitHub repository link.
  * Fork the repository to your GitHub account.
  * Clone the forked repository to your local machine.
* Open and Run File
  * Open the project in VSCode.
  * Run pipenv install to install all necessary dependencies.
  * Run pipenv shell to open instance of python shell

### Task 1: Define the Problem

You are working to build an app where users can search for books and look up information on them. We can make a custom request to the Open Library API for the exact information we want to present to the user.

### Task 2: Determine the Design

Review API docs and familiarize yourself with how the data is structured. Focus on what data you need to determine what endpoints you’ll need.

We’ll use: "https://openlibrary.org/search.json" with query parameters for title, fields, and limit.

### Task 3: Develop, Test, and Refine the Code 

#### Step 1: Create a Feature Branch

```bash
git checkout -b api_interaction
```

#### Step 2: Identify the & Construct the API Endpoint URL

* Take a few minutes and familiarize yourself with the linked Open Library API docs. 
* The data is laid out in what looks like a big list of nested dictionaries. This is actually a JSON object, which behaves just like a Python dictionary. Working with the JSON data returned to you by requests to an API.
* You should see the following upon going to the api endpoint of ```https://openlibrary.org/search.json?title=the+lord+of+the+rings&fields=title,author_name&limit=1``` in your browser

```json
{
  "numFound": 522,
  "start": 0,
  "numFoundExact": true,
  "docs": [
    {
      "title": "The Lord of the Rings",
      "author_name": ["J.R.R. Tolkien"]
    }
  ],
  "num_found": 522,
  "q": "",
  "offset": null
}
```

* For our app, we would like to show selected fields and a single book to our users. We can use query parameters to control the response format. We can define the query parameters through adding variables such as title in the URL after ```?``` symbol. By adding the ```&``` symbol we can chain multiple query parameters.

#### Step 3: Receive and Validate the Response

* Now that we understand what an API is and have even dealt with a URL that takes us to a real API endpoint, let's use that same URL to send a request for data from a Python program. We will do this by using the requests library which allows your program or application to send HTTP requests
* All code changes will happen in ```lib/open_library_api.py```:

```python
import requests
import json

class Search:

    def get_search_results(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        # formats the list into a comma separated string
        # output: "title,author_name"
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL)
        return response.content

results = Search().get_search_results()
print(results)
```

* We define a ```get_search_results()``` method that assigns our API endpoint to a variable name URL. The method submits a request with that URL using the ```get()``` method defined in the requests library, and returns the content of the response.
* Now, in your terminal in the directory of this lab, run ```python lib/open_library_api.py```.

#### Step 4: Receive and parse the response

* When looking at the request data you may notice the formatting looks difficult to parse at a glance. This is known as plaintext format which contains many items such as the ```\n``` that we don’t necessarily need. We need to convert the data to something easier for us to use!

```
b'{\n    "numFound": 522,\n    "start": 0,\n    "numFoundExact": true,\n    "docs": [\n        {\n            "title": "The Lord of the Rings",\n            "author_name": [\n                "J.R.R. Tolkien"\n            ]\n        }\n    ],\n    "num_found": 522,\n    "q": "",\n    "offset": null\n}'
```

* Let's update our method called ```get_search_results``` that returns the response formatted as JSON! To do this we need to apply a ```.json()``` method to our data to get it to an easier to use and see state.

```python
import requests
import json

class Search:

    def get_search_results(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        # formats the list into a comma separated string
        # output: "title,author_name"
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL)
        return response.json()

results_json = Search().get_search_results()
print(json.dumps(results_json, indent=1))
```

* We have used ```.json``` on the response to transform that data and proceeded to use ```json.dumps``` in order to validate our results and see the data in a clearer manner, make sure to test this out.

#### Step 5: Working with User Data

* To make our endpoint connection more interactive we can prompt a user input by adding a user input variable.

```python
import requests
import json

class Search:

    def get_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL).json()
        response_formatted = f"Title: {response['docs'][0]['title']}\nAuthor: {response['docs'][0]['author_name'][0]}"
        return response_formatted

search_term = input("Enter a book title: ")
result = Search().get_search_results(search_term)
print("Search Result:\n")
print(result)
```

* By adding a ```search_term``` we have prompted the user to enter a search, we then replace all the spaces with a ```+``` to match the search url and with that we can prompt the user for a search and search it. We also reformat the data to make an even cleaner response that is easy to parse from the user's end.
* Once you have verified that our search works, commit changes:

```bash
git commit -am "Finish api interaction"
```

#### Step 6: Push changes to GitHub and Merge Branches

* Push the branch to GitHub:

```bash
git push origin api_interaction
```

* Create a Pull Request (PR) on GitHub.
* Merge the PR into main after review.
* Pull the new merged main branch locally and delete merged feature branch (optional):

```bash
git checkout main
git pull origin main

git branch -d api_interaction
```

* If the last command doesn’t delete the branch, it’s likely git is not recognizing the branch as having been merged. Verify you do have the merged code in your main branch, then you can run the same command but with a capital D to ignore the warning and delete the branch anyway.

```bash
git branch -D api_interaction
```

### Task 4: Document and Maintain 

Best Practice documentation steps:
* Add comments to code to explain purpose and logic, clarifying intent / functionality of code to other developers.
* Add screenshot of completed work included in Markdown in README.
* Update README text to reflect the functionality of the application following https://makeareadme.com. 
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

## Considerations 
1. Spaces
  * Ensure there are no spaces in the url, similarly to a web browser spaces are not quite understood so ensure you remove any spaces
2. Testing URLs
  * It is always a good idea to test the url on your own browser first to ensure that it works with no issue. If an issue arises that implies that the api likely cannot connect.
