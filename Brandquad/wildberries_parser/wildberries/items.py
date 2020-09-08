# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WildberriesItem(scrapy.Item):
    # define the fields for your item here like:
    timestamp = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    color = scrapy.Field()
    brand = scrapy.Field()
    section = scrapy.Field()
    price_current = scrapy.Field()
    price_original = scrapy.Field()
    in_stock = scrapy.Field()
    count = scrapy.Field()
    set_images = scrapy.Field()
    description = scrapy.Field()
    article = scrapy.Field()
    composition = scrapy.Field()
    keys_list = scrapy.Field()
    values_list = scrapy.Field()
    city = scrapy.Field()
    tag_params = scrapy.Field()
    # pass
