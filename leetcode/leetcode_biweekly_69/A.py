def capitalizeTitle(title):
    title = title.split()

    for i in range(len(title)):

        if len(title[i]) <= 2:
            title[i] = title[i].lower()
        else:
            word = title[i]
            title[i] = word[0].upper() + word[1:].lower()
            print(word, word[0].upper() + word[1:].lower(), "pp")
    return title


title = "L hV"
print(capitalizeTitle(title))
