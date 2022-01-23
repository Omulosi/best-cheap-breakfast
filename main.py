# from scraper import scraper
from best_cheap_breakfast_scraper import scraper
from link_crawler import link_crawler

START_URL = 'https://www.msn.com/en-us/foodanddrink/foodnews/the-best-cheap-breakfast-in-every-state/ss-AAQSiaK'

if __name__ == '__main__': 
    link_crawler(START_URL, scraper_callback=scraper)