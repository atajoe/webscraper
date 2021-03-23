import scrapy


class Emirates1Spider(scrapy.Spider):
    name = 'emirates1'
    allowed_domains = ['www.verimatrix.com/careers/']
    start_urls = ['https://www.verimatrix.com/careers/']

    def parse(self, response):
        products = response.css('div.resumator-job-description-text.resumator-jobs-text')
        for product in products:
            item = {
            'name':  product.css('u::text').getall(),
            'description':product.css('span::text').getall(),
            'price': products.css('strong::text').getall()
            }
        yield item
    pass




        pass