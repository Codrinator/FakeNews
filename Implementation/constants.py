
""" Fake news """
# Json for fake news text
fake_news_json = "DataFiles/fakeNews.json"

# Number of fake articles for each site
fake_max_articles = [100, 150, 800, 200]

# Fake news sites links
start_fake_urls = [["https://www.timesnewroman.ro/"],
                   ["https://www.timpurigrele.ro/"],["https://7lucruri.ro/"],
                   ["https://www.catavencii.ro/"]]

# Prefix of desired fake news articles for each site
main_fake_urls = [['https://www.timesnewroman.ro/it-stiinta/','https://www.timesnewroman.ro/politic/',
                   'https://www.timesnewroman.ro/sport/','https://www.timesnewroman.ro/monden/',
                   'https://www.timesnewroman.ro/life-death/',
                   'https://www.timesnewroman.ro/descopera-romania/'],
                   ["https://www.timpurigrele.ro/"],
                   ["https://7lucruri.ro/"],
                   ["https://www.catavencii.ro/"]]

# HTML title tag function call for each fake news site
html_fake_titles = ['soup.find("h1", {"class": "mb-4 mb-xl-5"})',
                    'soup.find("h3", {"class": "post-title entry-title"})',
                    'soup.find("h1", {"class": "entry-title"})',
                    'soup.find("h1", {"class": "post-title"}, {"itemprop":"headline"})']

# HTML content tag function call for each fake news site
html_fake_articles = ['soup.find("div", {"class": "content-container page-editor-content mb-3 mb-md-5"})',
                     'soup.find("div", {"class": "post-body-container"})',
                     'soup.find("div", {"class": "post-inner-wrapper"})',
                     'soup.find("div", {"class": "post-content"})']

# HTML paragraph tags for each fake news site
fake_paragraph_tags = ["p", "span", "li", "p"]


""" True news """
# Json for true news text
true_news_json = "DataFiles/trueNews.json"

# Number of true articles for each site
true_max_articles = [150,150]

# True news sites links
start_true_urls = [["https://www.protv.ro/"], ["https://www.libertatea.ro/"]]

# Prefix of desired true news articles for each site
main_true_urls = [['https://stirileprotv.ro/stiri/auto/', 'https://stirileprotv.ro/stiri/international/',
             'https://stirileprotv.ro/stiri/actualitate/', 'https://stirileprotv.ro/stiri/sanatate/',
             'https://stirileprotv.ro/stiri/socant/', 'https://stirileprotv.ro/stiri/stiinta/',
             'https://stirileprotv.ro/stiri/financiar/'],
            ['https://www.libertatea.ro/stiri/']]

# HTML title tag function call for each true news site
html_true_titles = ['soup.find("h1")', 'soup.find("h1")']

# HTML content tag function call for each true news site
html_true_articles = ['soup.find("div", {"itemprop": "articleBody"})',
                    'soup.find("div", {"class": "article-body js-copy-text"})']

# HTML paragraph tags for each true news site
true_paragraph_tags = ["p","p"]


# Preprocessing data
weird_html_phrases = ["Solicitați un linkSolicitați un linkFacebookFacebookTwitterTwitterPinterestPinterestE-mailE-mailAlte aplicațiiAlte aplicații",
                      "ascultareashare", "interviuripentrurealitate", ]