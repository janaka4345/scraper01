import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "BookscraperSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

# parse get called when the response comes back
    def parse(self, response):
        books=response.css('article.product_pod')
        for book in books:
            yield{
                'name':book.css('h3 a::text').get(),
                'price':book.css('div.product_price p::text').get(),
                'url':book.css('h3 a').attrib['href']
            }
        
        nextPage=response.css('li.next a::attr("href")').get()
        if nextPage is not None:
            if 'catalogue/'  in nextPage:
                nextPageUrl=f"https://books.toscrape.com/{nextPage}"
            else:
                nextPageUrl=f"https://books.toscrape.com/catalogue/{nextPage}"


            yield response.follow(nextPageUrl,callback=self.parse)
