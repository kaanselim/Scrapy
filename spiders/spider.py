import scrapy


class QuotesSpider(scrapy.Spider):
    name = "FirstSpider"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
            page = response.url.split('/')[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield   {
            response.follow(next_page, callback=self.parse)
        }
