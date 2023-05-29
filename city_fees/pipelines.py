# Author: Juan Jaramillo
# Documentation: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CityFeesPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        ## strip all whitespaces from the beginning and end of the string for the following fields
        field_names = ['name', 'as_of_date']
        for field_name in field_names:
            value = adapter.get(field_name)
            adapter[field_name] = value[0].strip()
        
        ## Replace N/A value with None for the as_of_date field
        if adapter.get('as_of_date') == 'N/A':
            adapter['as_of_date'] = None

        return item
