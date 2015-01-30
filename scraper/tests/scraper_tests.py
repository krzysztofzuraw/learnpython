from nose.tools import *
import Scraper.scraper as scr

def test_scraper():
    w_page1 = 'http://www.voidspace.org.uk'
    w_page2 = 'http://www.onet.pl'
    w_page3 = 'http://www.tutorialspoint.com'
    assert_equals(scr.page_scraper(w_page1).keys(), ['url','links','title'])
    assert_equals(scr.page_scraper(w_page2)['url'], 'http://www.onet.pl')
    assert_in('Tutorials', scr.page_scraper(w_page3)['title'])
    assert_false(scr.page_scraper(w_page2)['links'] == None) 
