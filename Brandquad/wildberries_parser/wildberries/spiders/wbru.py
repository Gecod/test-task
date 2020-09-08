import scrapy
from scrapy.http import HtmlResponse
from wildberries.items import WildberriesItem
import time
# from scrapy import Request
# import datetime

class WbruSpider(scrapy.Spider):
    name = 'wbru'
    allowed_domains = ['wildberries.ru']
    start_urls = ['https://www.wildberries.ru/catalog/zhenshchinam/bele-i-kupalniki/termobele']
    # request_with_cookies = Request(url=start_urls[0],
    #                                cookies={'__wbl': 'cityId%3D77%26regionId%3D77%26city%3D%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%26phone%3D84957755505%26latitude%3D55%2C7247%26longitude%3D37%2C7882',
    #                                         '__region': '33_75_63_69_68_48_30_1_4_40_31_71_22_38_65_66_70_64',
    #                                         '__store': '116433_115577_117501_507_3158_119400_2737_117986_1699_6158_117673_119261_117413_119070_118106_119798_119781',
    #                                         'method': 'POST'})

    def parse(self, response:HtmlResponse):
        next_page = response.xpath('//div[@class="pageToInsert"]/a[@class="pagination-next"]/@href').extract_first()
        item_links = response.xpath('//div[contains(@class, "catalog_main_table")]//a[contains(@class, "open-full-product-card")]/@href').extract()
        global section__
        section__ = response.xpath('//li[contains(@class, "breadcrumbs-item")]//span[@itemprop]/text()').extract()
        for link in item_links:
            yield response.follow(link, callback=self.item_parse)

        yield response.follow(next_page, callback=self.parse)

    def item_parse(self, response:HtmlResponse):
        # offset = datetime.timezone(datetime.timedelta(hours=3))
        # time_format = "%Y-%m-%d %H:%M:%S"
        # timestamp_ = datetime.datetime.now(offset)
        # timestamp_ = f"{timestamp_:{time_format} {offset}}"
        # timestamp_ = datetime.datetime.now(offset)
        timestamp_ = time.time()
        url_ = response.xpath('//link[@rel="canonical"]/@href').extract_first()
        title_ = response.xpath('//div[contains(@class, "brand-and-name")]/span[@class="name"]/text()').extract_first()
        color_ = response.xpath('//div[contains(@class, "color")]/span[contains(@class, "color")]/text()').extract_first()
        brand_ = response.xpath('//div[contains(@class, "brand-and-name")]/span[@class="brand"]/text()').extract_first()
        global section__
        section_ = section__
        price_current_ = response.xpath('//span[@class="final-cost"]/text()').extract_first()
        price_original_ = response.xpath('//span[@class="old-price"]/del/text()').extract_first()
        in_stock_ = response.xpath('//div[@class="cart-btn-wrap"]/button[contains(@class, "add-to-card")]/text()').extract_first()
        count_ = "Can't find"
        set_images_ = response.xpath('//a[@class="j-photo-link"]/@href').extract()
        description_ = response.xpath('//div[contains(@class, "description-text")]/p/text()').extract_first()
        article_ = response.xpath('//div[@class="article"]/span/text()').extract_first()
        composition_ = response.xpath('///div[contains(@class, "composition")]/span/text()').extract_first()
        keys_list_ = response.xpath('//div[contains(@class, "params")]//div[@class="params"]//b/text()').extract()
        values_list_ = response.xpath('//div[contains(@class, "params")]//div[@class="params"]//span/text()').extract()
        city_ = response.xpath('//span[@class="delivery-cond-locality"]/text()').extract_first()
        tag_params_ = response.xpath('//script[@type="text/javascript" and not(@id)][contains(text(), "ProdID")]/text()').extract_first()
        yield WildberriesItem(timestamp=timestamp_, url=url_, title=title_, color=color_, brand=brand_,
                              section=section_, price_current=price_current_, price_original=price_original_,
                              in_stock=in_stock_, count=count_, set_images=set_images_,
                              description=description_, article=article_, composition=composition_,
                              keys_list=keys_list_, values_list=values_list_, city=city_, tag_params=tag_params_)
