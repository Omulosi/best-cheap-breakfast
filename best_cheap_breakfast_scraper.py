from lxml.html import fromstring
import time
import random
import selenium
from url_downloader import get_driver

# Name, website, city, state

NAME_XPATH = '//h2[contains(@class,"typography-DS-EntryPoint2-5")]//text()'
STATE_PATH = ''
WEBSITE_XPATH = '//div[contains(@class,"slideMetadata_content-DS-EntryPoint2-4")]//a/@href'
CITY_XPATH = '//div[contains(@class,"slideMetadata_content-DS-EntryPoint2-4")]//b//text()'


NEXT_BTN_XPATH = '//button[@title="Next Slide"]'

TOTAL_STATES = 51

def scraper(start_link):
    """[summary]

    Args:
        query_link ([type]): [description]

    Returns:
        [type]: [description]
    """
    driver = get_driver()
    driver.get(start_link)
    
    image_count = None
    
   
    while True:
        time.sleep(random.randint(2,4))
        current_url = driver.current_url
        url_info = current_url.split('#')[1:]
        
        if url_info and 'image' in url_info[0]:
            split_items = url_info[0].split('=')
            if len(split_items) > 1:
                image_count = int(split_items[1])
        
        if url_info and 'image' in url_info[0]:
            # Extract metadata.
            tree = fromstring(driver.page_source)
            
            # scrape the fields: name, website, city, state
            name_state = tree.xpath(NAME_XPATH)
            website = tree.xpath(WEBSITE_XPATH)
            city = tree.xpath(CITY_XPATH)
            
            name_state = name_state and name_state[0].split(':')
            state, name = name_state or ('','')
            website = website and website.pop(0)
            city = city and city.pop(0).strip()
       
            # yield the results
            values = dict(name=name, website=website, city=city, state=state)
            
            print()
            print()
            print(f"URL: {driver.current_url}")
            print(f"Count: {image_count}")
            print(f"Values: {values}")
            print()
            yield values
        
        try:
            next_btn = driver.find_element_by_xpath(NEXT_BTN_XPATH)
            driver.implicitly_wait(10)
            next_btn.click()
        
        except selenium.common.exceptions.NoSuchElementException:
            # End of crawl
            pass
        
        if image_count and image_count >= TOTAL_STATES:
                break
            
    driver.quit()
