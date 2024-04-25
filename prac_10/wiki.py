import wikipedia

while True:
    title = input("Title: ")

    if not title:
        print("Farewell")
        break

    try:
        page = wikipedia.page(title, auto_suggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error")