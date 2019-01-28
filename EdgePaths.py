import re

class URL:
    BASE_URL = "http://needforspeed-edge.nexon.com/community/free"
    POST_URL = "http://needforspeed-edge.nexon.com/community/free?n4articlesn={post_id}"

class ElementXpath:
    POST_TITLES_ON_BOARD = "//li[not(@class)]/div[@class = 'tit']/a/span[@class='text']"
    POST_TITLE_ON_BOARD = "//li[not(@class)]/div[@class = 'tit']/a/span[@class='text' and contains(text(), '{title}')]"
    TITLE_ON_POST = "//div[@class ='view_content']/div[@class = 'tit']/h3[@class = 'title']"
    CONTENT_ON_POST = "//meta[@property = 'og:description']"
    COMMENTS_ON_POST = "//div[@class = 'comment_content']/p"

class PathUtils:
    def fromTemplate(path, *params):
        for param in params:
            path = re.sub("\{[a-zA-Z0-9_]*\}", param, path, count=1)

        return path