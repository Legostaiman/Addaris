import api
import cache


def main(article_name):
    """The function returns the requested article."""
    looking_in_cache = cache.check_cache(article_name)
    if looking_in_cache is not None:
        result = looking_in_cache
    else:
        result = api.response_article(article_name)
        cache.append_cache(article_name, result)
    return result


if __name__ == "__main__":
    search_article = input("zadejte název článku\n")
    print(main(search_article))
