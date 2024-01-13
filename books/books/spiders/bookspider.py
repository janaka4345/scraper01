import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "BookscraperSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    
    def parse_books(self,response):
        yield{
                'name':response.css('div.product_main h1::text').get(),
                'price':response.css('div.product_main p::text').get(),
                'url':f'https://books.toscrape.com/',
                'productdisc':response.css('div.sub-header h2::text').get()
            }

# parse get called when the response comes back
    def parse(self, response):
        bookUrls=response.css('ol.row div.image_container')
        for bookUrl in bookUrls:
            book_rel_url=bookUrl.css('a::attr("href")').get()
            if 'catalogue/'  in book_rel_url:
                nextBookUrl=f"https://books.toscrape.com/{book_rel_url}"
            else:
                nextBookUrl=f"https://books.toscrape.com/catalogue/{book_rel_url}"
            
            yield response.follow(nextBookUrl,callback=self.parse_books)
            
               
        nextPage=response.css('li.next a::attr("href")').get()
        if nextPage is not None:
            if 'catalogue/'  in nextPage:
                nextPageUrl=f"https://books.toscrape.com/{nextPage}"
            else:
                nextPageUrl=f"https://books.toscrape.com/catalogue/{nextPage}"


            yield response.follow(nextPageUrl,callback=self.parse)
