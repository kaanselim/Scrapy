# -*- coding: utf-8 -*-
import scrapy


class A9gagSpider(scrapy.Spider):
    name = 'sozluk'
    allowed_domains = ['tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi']
    start_urls = ['https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(A)']

    def parse(self, response):
        
        
        for li in response.css('div table tbody tr td ul li'):
             yield {
                
                    'text': li.css('::text').extract(),
                    'text2': li.css('::text').extract()
                       
                    }
    
    
        
        
       
        
       