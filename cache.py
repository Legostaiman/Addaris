import pickle


def append_cache(article_name, result):
    """The function saves the received article."""
    try:
        file = open("saved_articles.bin", "rb")
        try:
            saved_articles = pickle.load(file)
            saved_articles[str(article_name)] = str(result)
        finally:
            file.close()
        file = open("saved_articles.bin", "wb")
        try:
            pickle.dump(saved_articles, file)
        finally:
            file.close()

    except FileNotFoundError:
        file = open("saved_articles.bin", "wb")
        saved_articles = {str(article_name): str(result)}
        try:
            pickle.dump(saved_articles, file)
        finally:
            file.close()


def check_cache(article_name):
    """The function checks for the presence of the article locally."""
    try:
        file = open("saved_articles.bin", "rb")

        try:
            saved_articles = pickle.load(file)
            if article_name in saved_articles.keys():
                return saved_articles[article_name]
            else:
                return None
        finally:
            file.close()

    except FileNotFoundError:
        return None
