import urllib2
import re

def page_scraper(page):
     """
     Simple page scraper that get urls and title from web page
     :param page: page to be scrapered?
     :return: dictionary of {url, title, links}
     :rtype: dictionary
     """
     req = urllib2.Request(page)
     response = urllib2.urlopen(req)
     the_page = response.read()
     descryption = re.search("<title>(.*?)</title>", the_page)
     websites = list(set(re.findall("(https?://[^\s]+\")", the_page)))
     return {'url':page, 'title':descryption.group()[7:-8], 'links':websites}
     

