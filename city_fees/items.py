# Author: Juan Jaramillo
# See documentation: https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CityFeesItem(scrapy.Item):
    
    name = scrapy.Field()
    description = scrapy.Field()
    statutory_authority = scrapy.Field()
    amount = scrapy.Field()
    as_of_date = scrapy.Field()

