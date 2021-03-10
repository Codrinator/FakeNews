from bs4 import SoupStrainer, BeautifulSoup
import httplib2
import requests
import json


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
        if status == 200:
            print("Main website couldn't be reached: " + str(search_url))
        else:
            # Get viable, article links
            for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a'),from_encoding="utf-8"):
                if link.has_attr('href'):
                    for news_type in main_urls_list:
                        if "kmkz" in news_type:
                            new_link = "https://www.kmkz.ro" + link['href']
                            print(new_link)
                            if len(link['href'])>30:
                                link_list.add(new_link)
                                new_links.add(new_link)
                                if len(link_list) > max_articles:
                                    return
                        elif link['href'].startswith(news_type) and len(link['href'])-len(news_type)>30 and "more" not in link['href']:
                            link_list.add(link['href'])
                            new_links.add(link['href'])
                            if len(link_list) > max_articles:
                                return
    # Recall the function
    if counter < 20:
        crawlOnPage(new_links, main_urls_list, link_list, counter, max_articles)


def extractText(myUrl, titleClass, articleClass, tag):
    ''' Extract title and text from article link '''

    # Request link access
    page = requests.get(myUrl)
    soup = BeautifulSoup(page.content, 'html.parser')

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
    paragraphs_tags = article_content.find_all(tag) # Find all row tags in that table
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


def collect_news(news_json, start_urls, main_urls, html_titles, html_articles, max_articles, tags):
    ''' Collect the news from all the provided web sites '''
    ''' Separate articles in true/fake news json files'''

    # Site iterator
    counter = 0

    # Iterate through the information of each site
    for start_url, main_url, html_article, html_title, tag in zip(start_urls, main_urls, html_articles, html_titles, tags):
        # Link and content dictionary for current site
        data = {}
        # All links found in current site
        final_link_list = set()

        # Crawl and get links for current site
        crawlOnPage(start_url, main_url, final_link_list, 0, max_articles[counter])

        # Add over true/fake news if already there
        if counter != 0:
            with open(news_json, "r", encoding="utf-8") as jsonObject:
                data = json.load(jsonObject)

        # Get content for current site links
        for link in final_link_list:
            data[link] = extractText(link, html_title, html_article, tag)
            if data[link] is None: # or "nothing here" in data[link]:
                del data[link]

        # Add news in site's category json file
        with open(news_json, "w+", encoding="utf-8") as jsonObject:
            json.dump(data, jsonObject, sort_keys=True, ensure_ascii=False, indent=1)

        # Add to site iterator
        counter += 1


def scrape_data():
    """ Scrape data from chosen sites and store in json files """
    # Collect fake news
    """collect_news(constants.fake_news_json, constants.start_fake_urls, constants.main_fake_urls,
                 constants.html_fake_titles, constants.html_fake_articles, constants.fake_max_articles,
                 constants.fake_paragraph_tags)"""
    # Collect true news
    """collect_news(constants.true_news_json, constants.start_true_urls, constants.main_true_urls,
                 constants.html_true_titles, constants.html_true_articles, constants.true_max_articles,
                 constants.true_paragraph_tags)"""
