from extract import collect_news
import Config
import json

def Preprocessing(text,stop_words):
    newData = []
    for item in text.values():
        newData.append(item[0] + item[1])
    for i in range(0,len(newData)):
        newData[i] = [i.lower() for i in word_tokenize(newData[i]) if i.isalpha()]
        newData[i] = [i for i in newData[1][i] if i not in stop_words]
    return newData


def get_news_data(news_file):
    " Read and return news data "
    with open(news_file, "r", encoding="utf-8") as jsonObject:
        news = json.load(jsonObject)
    return news


def news_type_word_count(news_dictionary):
    " Get number of words across the news articles "
    sum = 0
    for key, value in news_dictionary.items():
        sum += value[0].count(" ") + value[1].count(" ")
    return sum


def print_dictionary(dictionary):
    for item in dictionary.items():
        print(item)


if __name__ == "__main__":
    # Gather news from websites and separate in json files
    #collect_news(Config.fake_news_json, Config.start_fake_urls, Config.main_fake_urls, Config.html_fake_titles,
                 #Config.html_fake_articles, Config.fake_max_articles, Config.fake_paragraph_tags)
    #collect_news(Config.true_news_json, Config.start_true_urls, Config.main_true_urls, Config.html_true_titles,
                 #Config.html_true_articles, Config.true_max_articles, Config.true_paragraph_tags)

    # Read news json files
    true_news = get_news_data("trueNews.json")
    fake_news = get_news_data("fakeNews.json")
    true_news_alex = get_news_data("trueNewsAlex.json")
    true_news_digi = get_news_data("trueNewsDigi24.json")


    """# Print news data info
    print("\n   True News\nNumber of articles:", len(true_news), "\nNumber of words:", true_news_words)
    # print_dictionary(true_news)
    print("\n   True News Alex\nNumber of articles:", len(true_news_alex), "\nNumber of words:", true_news_alex_words)
    # print_dictionary(true_news)
    print("\n   True News Digi\nNumber of articles:", len(true_news_digi), "\nNumber of words:", true_news_digi_words)
    # print_dictionary(true_news)
    print("\n   Fake News\nNumber of articles:", len(fake_news), "\nNumber of words:", fake_news_words)
    #print_dictionary(fake_news)
    print("\n   Total News\nNumber of articles:", len(true_news)+len(fake_news))
    print("Number of  words:", fake_news_words + true_news_words + true_news_alex_words + true_news_digi_words)"""

    for item in true_news_alex.items():
        true_news[item[0]] = item[1]
    for item in true_news_digi.items():
        true_news[item[0]] = item[1]

    # Get number of words
    true_news_words = news_type_word_count(true_news)
    fake_news_words = news_type_word_count(fake_news)

    # Print news data info
    print("\n   True News\nNumber of articles:", len(true_news), "\nNumber of words:", true_news_words)
    # print_dictionary(true_news)
    print("\n   Fake News\nNumber of articles:", len(fake_news), "\nNumber of words:", fake_news_words)
    # print_dictionary(fake_news)
    print("\n   Total News\nNumber of articles:", len(true_news) + len(fake_news))
    print("Number of  words:", fake_news_words + true_news_words)
    with open("stopwords.txt",encoding="utf-8") as f:
        stopwords = f.read().split()
    trueNews = Preprocessing(true_news,stopwords)
    print(trueNews)
    """true_news_data = []
    for i in range(0, len(true_news_words[])):
        merged_news[1][i] = [i.lower() for i in word_tokenize(merged_news[1][i]) if i.isalpha()]
        merged_news[1][i] = [i for i in merged_news[1][i] if i not in stop_words]
        news_data.append([merged_news[0][i], merged_news[1][i]])

    vocabulary = dict()
    for item in news_data:
        for word in item[1]:
            if word not in vocabulary.keys():
                vocabulary[word] = 1
            else:
                vocabulary[word] += 1

    vocabulary = {k: v for k, v in sorted(vocabulary.items(), key=lambda item: item[1])}
    print(vocabulary)"""