import wikipedia

while True:
    page_title = input("Enter page title or search phrase: ")

    if not page_title:
        break

    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(f"Page Title: {page.title}")
        print(f"Page Summary: {page.summary}")
        print(f"Page URL: {page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
    except wikipedia.exceptions.PageError:
        print("Page not found.")


