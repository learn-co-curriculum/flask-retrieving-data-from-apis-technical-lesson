# Retrieving Data from an API

## Overview

A Python program that retrieves book data from the Open Library API. Users enter a book title, and the program returns the title and author of the top matching result.

## Technologies Used

Python, Requests library, Open Library API

## Installation

Fork and clone this repository. Install dependencies using your preferred environment manager and activate the environment.

## Usage

Run the program from your terminal. When prompted, enter a book title. The program sends a request to the Open Library API and prints the matching book's title and author.

## API Reference

This project uses the Open Library Search API at openlibrary.org/dev/docs/api/search, requesting the search.json endpoint with query parameters for title, fields, and limit.

## Considerations

Remove spaces from URLs before sending requests, since spaces are not valid in URLs. Test constructed URLs in a browser first to confirm they return the expected data.

## License

Open source and available for use and modification.