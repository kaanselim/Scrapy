# -*- coding: utf-8 -*-
import scrapy


class SozlukSpider(scrapy.Spider):
    name = 'sozluk'
    allowed_domains = ['tr.wiktionary.org']
    start_urls =[ 
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(A)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(B)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(C)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(Ç)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(D)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(E)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(F)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(G)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(H)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(I)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(İ)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(J)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(K)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(L)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(M)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(N)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(O)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(Ö)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(P)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(R)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(S)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(Ş)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(T)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(U)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(Ü)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(V)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(Y)',
            'https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_(Z)'
    ]
    
    def parse(self, response):
        
        self.log('i just visited' + response.url )
        
           
        for li in response.css("div.mw-parser-output  ul  li "):
            
            yield{
                    'text2': li.css('::text').extract()
                    }
        
       
    
        
       
        
       