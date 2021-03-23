import scrapy
import pandas as pd
import csv 

class Emirates2Spider(scrapy.Spider):
    name = 'emirates2'
    allowed_domains = ['emirates.com/ae/english/experience/shop-emirates/duty-free/']
    start_urls = ['http://emirates.com/ae/english/experience/shop-emirates/duty-free//']

    def parse(self, response):
        Items =[]
        ul = response.css('ul.image-list__group')
        for u in ul:
            products =u.css('li')

            for product in products:
                
                name =  product.css('h3.image-list__title::text').get()
                description = product.css('p.image-list__body.reset-p::text').get()
                price = product.css('p.image-list__price::text').get()
                name=''.join(name)
                description = ''.join(description)
                print(price)
                
                Items.append([name,description,price])
        f= open('Data_2.csv',mode='a+',encoding='utf8' )
        write = csv.writer(f,delimiter= ','  ,quotechar='"',quoting=csv.QUOTE_MINIMAL )
        for item in Items:
            write.writerow(item)
            
        f.close()
        print('All Done')
        #github test

        
        
    pass
