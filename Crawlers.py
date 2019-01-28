import re

from Browser import Browser
from EdgePaths import ElementXpath, PathUtils, URL


class EdgeCrawler:
    def crawl_nexon_board():
        raw_data = []
        browser = Browser()

        browser.get_page(URL.BASE_URL)
        browser.click_element_by_xpath(ElementXpath.POST_TITLES_ON_BOARD)
        recent_post_id = int(re.search('n4articlesn=(\d+)', browser.get_current_url()).group(1))

        for i in range(0, 10):
            url = PathUtils.fromTemplate(URL.POST_URL, str(recent_post_id - i))
            browser.get_page(url)

            title = browser.get_element_by_xpath(ElementXpath.TITLE_ON_POST).text
            content = browser.get_element_by_xpath(ElementXpath.CONTENT_ON_POST).get_attribute("content")
            comments = list(map(lambda element: element.text, browser.get_elements_by_xpath(ElementXpath.COMMENTS_ON_POST)))
            raw_data.append(title)
            raw_data.append(content)
            raw_data.extend(comments)

        return raw_data
