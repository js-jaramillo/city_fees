# Author: Juan Jaramillo
# Documentation: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CityFeesPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        ## strip all whitespaces from string
        field_names = ['name', 'as_of_date']
        for field_name in field_names:
            value = adapter.get(field_name)
            adapter[field_name] = value[0].strip()


        return item
