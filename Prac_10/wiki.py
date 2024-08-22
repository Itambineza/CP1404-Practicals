"""
CP1404 Practical 10 - Testing, APIs, and Flask
Wikipedia API interaction
"""

import wikipedia

def search_wikipedia():
    """
    Prompt the user for a page title or search phrase and print details of the page.
    The function continues prompting until the user enters blank input.
    Handles DisambiguationError and PageError exceptions.
    """
    while True:
        search_term = input("Enter page title: ")
        if not search_term:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_term, autosuggest=False)
            print(f"\n{page.title}\n{page.summary}\n{page.url}\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    search_wikipedia()
