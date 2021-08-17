import wikipedia
wikipedia.set_lang("cz")


def response_article(article_name):
    response = wikipedia.search(str(article_name))
    if str(response[0]).lower().replace(',', '') == article_name.lower().replace(',', ''):
        result = wikipedia.summary(str(article_name))
        return result
    result = "Možná jste hledali následující články: " + str(response)
    return result
