# Author: Juan Jaramillo

# Define here the models for your scraped items
import scrapy
from city_fees.items import CityFeesItem

class FeespiderSpider(scrapy.Spider):
    name = "feespider"
    allowed_domains = ["cohweb.houstontx.gov"]
    start_urls = ["https://cohweb.houstontx.gov/FIN_FeeSchedule/default.aspx"]

    def parse(self, response):

        rows = response.css('table.soft tr.d0, table.soft tr.d1')
        
        for row in rows:
            fee_item = CityFeesItem()
            fee_item['name'] = row.css('td')[0].css('.helpline ::text').get(),
            fee_item['description'] = row.css('td')[1].css('.helpline ::text').get(),
            fee_item['statutory_authority'] = row.css('td')[2].css('.helpline ::text').get(),
            fee_item['amount'] = row.css('td')[3].css('.helpline ::text').get(),
            fee_item['as_of_date'] = row.css('td')[4].css('.helpline ::text').get(),

            yield fee_item
                


            
       
