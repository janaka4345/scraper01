import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "BookscraperSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

# parse get called when the response comes back
    def parse(self, response):
        pass
