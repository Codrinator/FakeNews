from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import requests
import json

# News sites links
start_urls = [["https://www.protv.ro/"], ["https://www.libertatea.ro/"],
              ["https://www.timesnewroman.ro/"], ["https://www.catavencii.ro/"]]

# Prefix of desired news articles for each site
mainUrls = [['https://stirileprotv.ro/stiri/auto/', 'https://stirileprotv.ro/stiri/international/',
             'https://stirileprotv.ro/stiri/actualitate/', 'https://stirileprotv.ro/stiri/sanatate/',
             'https://stirileprotv.ro/stiri/socant/', 'https://stirileprotv.ro/stiri/stiinta/',
             'https://stirileprotv.ro/stiri/financiar/'],
            ['https://www.libertatea.ro/stiri/'],
            ['https://www.timesnewroman.ro/it-stiinta/','https://www.timesnewroman.ro/politic/',
             'https://www.timesnewroman.ro/sport/','https://www.timesnewroman.ro/monden/',
             'https://www.timesnewroman.ro/life-death/',
             'https://www.timesnewroman.ro/descopera-romania/'],
            ["https://www.catavencii.ro/"]]

# HTML title tag function call for each site
listClassTitle = ['soup.find("h1")', 'soup.find("h1")', 'soup.find("h1", {"class": "mb-4 mb-xl-5"})',
                  'soup.find("h1", {"class": "post-title"}, {"itemprop":"headline"})']

# HTML content tag function call for each site
listClassArticle = ['soup.find("div", {"itemprop": "articleBody"})',
                    'soup.find("div", {"class": "article-body js-copy-text"})',
                    'soup.find("div", {"class": "content-container page-editor-content mb-3 mb-md-5"})',
                    'soup.find("div", {"class": "post-content"})'
                    ]
# Number of desired articles from each site
max_articles = [8,5,19,10]

# Json file names for the two news categories
json_files = ["trueNews.json", "fakeNews.json"]


def crawlOnPage(search_urls, main_urls_list, link_list, counter, max_articles):
    """ Crawl the links of a certain page and add them to a set """
    """ Recursively fill desired number of link for each news site """
    # Recursion counter
    counter += 1
    # Links found during this iteration
    new_links = set()
    # Crawl this page's URL's
    for search_url in search_urls:
        # Request site access
        http = httplib2.Http()
        status, response = http.request(search_url)
        if(status != 200):
            # Get viable, article links
            for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a'),from_encoding="utf-8"):
                if link.has_attr('href'):
                    for news_type in main_urls_list:
                        if link['href'].startswith(news_type) and len(link['href'])-len(news_type)>30:
                            link_list.add(link['href'])
                            new_links.add(link['href'])
                            if (len(link_list) > max_articles):
                                return
        else:
            print("Main website couldn't be reached: " + str(search_url))
    # Recall the function
    if counter < 8:
        crawlOnPage(new_links, main_urls_list, link_list, counter, max_articles)


def extractText(myUrl, titleClass, articleClass):
    ''' Extract title and text from article link '''
    # Request link access
    page = requests.get(myUrl)

    # Get title from specific parameter function call
    find_title = eval(titleClass)
    if find_title != None:
        title = find_title.text.strip()
    else:
        title = 'nothing here'

    # Get article text from specific parameter function call
    article_content = eval(articleClass) # Locate that table tag
    if not article_content:
        print("Nothing found")
        return

    # Get the article content paragraphs
    paragraphs_tags = article_content.find_all('p') # Find all row tags in that table
    if not paragraphs_tags:
        paragraphs = 'nothing here'
    else:
        paragraphs = ""
        if (find_title == None) and (not paragraphs_tags):
            return
        for tag in paragraphs_tags:
            paragraphs += tag.text.strip()

    # Return tile, content tuple
    return title, paragraphs


def collect_news():
    ''' Collect the news from all the provided web sites '''
    ''' Separate articles in true/fake news json files'''

    # Site iterator
    counter = 0

    # Iterate through the information of each site
    for start_url, mainUrl, articleClass, titleClass in zip(start_urls, mainUrls, listClassArticle, listClassTitle):
        # Link and content dictionary for current site
        data = {}
        # All links found in current site
        finalLinkList = set()
        # Crawl and get links for current site
        crawlOnPage(start_url, mainUrl, finalLinkList, 0, max_articles[counter])

        # Add over true/fake news if already there
        if counter % 2 == 1:
            with open(json_files[counter//2], "r", encoding="utf-8") as jsonObject:
                data = json.load(jsonObject)

        # Get content for current site links
        for link in finalLinkList:
            data[link] = extractText(link, titleClass, articleClass)
            if data[link] is None:
                del data[link]

        # Add news in site's category json file
        with open(json_files[counter//2], "w+",encoding="utf-8") as jsonObject:
            json.dump(data, jsonObject, sort_keys=True, ensure_ascii=False, indent=1)

        # Add to site iterator
        counter += 1