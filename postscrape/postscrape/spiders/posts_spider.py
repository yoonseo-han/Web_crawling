import scrapy

class PostSpider(scrapy.Spider): 
    name = "posts"
    
    start_urls = [
        # URL of page to scrape
        'https://en.wikipedia.org/wiki/Apple_Inc.'
    ]
    
    def parse(self, response):
        for posts in response.css('div.post-item'):
            yield {
                'title' : posts.css('.post-header h2 a::text')[0].get(),
                'date' : posts.css('.post-header a::text')[1].get(),
                'author' : posts.css('.post-header a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)