import json


def get_news_data(news_file):
    """ Read and return news data """
    with open(news_file, "r", encoding="utf-8") as jsonObject:
        news = json.load(jsonObject)
    return news


def news_type_word_count(news_dictionary):
    """ Get number of words across the news articles """
    sum = 0
    for key, value in news_dictionary.items():
        sum += value[0].count(" ") + value[1].count(" ")
    return sum


def get_corpus():
    """ Read and merge corpus data from files """
    true_news = get_news_data("DataFiles/trueNews.json")
    fake_news = get_news_data("DataFiles/fakeNews.json")
    true_news_alex = get_news_data("DataFiles/trueNewsAlex.json")
    true_news_digi = get_news_data("DataFiles/trueNewsDigi24.json")

    # Combine true news data from all json files
    for item in true_news_alex.items():
        true_news[item[0]] = item[1]
    for item in true_news_digi.items():
        true_news[item[0]] = item[1]

    return true_news, fake_news


