# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:12:49 2022

@author: DHARMIK
"""

import pandas as pd
import scrapy
import json

#url = 'https://www.olx.in/cars_c84'
from scrapy.crawler import CrawlerProcess

class Olx(scrapy.Spider):
    name='olx'
    url = 'https://www.olx.in/api/relevance/v2/search?category=84&facet_limit=100&lang=en-IN&location=1000001&location_facet_limit=20&platform=web-desktop&size=40&user=17d84a5b44ax162c11d9'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
    
    def start_requests(self):
        pass
        #yield scrapy.Request(url=self.url + '&page=0',headers=self.headers, callback=self.parse)
    
    
    def parse(self,res):
        with open('test.json') as json_file:
            data = json.load(json_file)
            data = json.dumps(data)
            print(data)
        '''
        data=''
         #json_object = json.dumps(res.text)
        with open('res.json','r') as json_file:
            for line in json_file.read():
                data += line
        print(type(data))
        final = json.loads(data)
        print(type(final))
        #for item in data:
        #    print(json.dumps(item,indent=2))
            
        '''
            
        
    
    
#crawler process

#process = CrawlerProcess()
#process.crawl(Olx)
#process.start(stop_after_crawl=False)

#debug
Olx.parse(Olx,'')
