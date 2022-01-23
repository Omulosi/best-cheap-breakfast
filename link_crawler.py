
import socket
from throttle import Throttle
import pandas as pd

socket.setdefaulttimeout(120)


DATA = []

def link_crawler(start_url, scraper_callback=None):
    
    for values in scraper_callback(start_url):
        name, state, website, city = values.get('name'), values.get('state'), values.get('website'), values.get('city')
        DATA.append((name, state, website, city))
        
    df  = pd.DataFrame(DATA, columns=['name', 'state', 'website', 'city'])
    df.to_csv('best_cheap_breakfast.csv')