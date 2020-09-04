# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class WildberriesPipeline:
    def __init__(self):
        self.f = open('wildberries.json', 'a', encoding='utf-8')

    def add_to_json(self, product):
        self.f.write(json.dumps(product, indent=2, ensure_ascii=False))
        # self.f.write(str(product))
        # self.f.close()
        pass

    def process_item(self, item, spider):
        product = {
            'timestamp': item['timestamp'],
            'url': item['url'],
            'title': item['title'],
            'color': item['color'],
            'brand': item['brand'],
            'section': item['section'],
            'price_current': self.get_price_info(item)[0],
            'price_original': self.get_price_info(item)[1],
            'discount':  self.get_price_info(item)[2],
            'in_stock': self.get_in_stock_info(item),
            'count': item['count'],
            'main_image': item['main_image'],
            'set_images': item['set_images'],
            'description': item['description'],
            'article': item['article'],
            'composition': item['composition'],
            'spec': self.get_spec(item),
            'city': item['city']
        }

        print(product['spec'])

        self.add_to_json(product)

        return item

    def get_spec(self, item):
        if 'keys_list' not in item:
            return None
        elif 'values_list' not in item:
            return None
        else:
            keys_list = item['keys_list']
            values_list = item['values_list']

            if len(keys_list) != len(values_list):
                return 'mapping error'
            else:
                # for key in keys_list:
                #     i = keys_list.index(key)
                #     for letter in key:
                #         if letter == ' ':
                #             keys_list[i] = key[1:]

                for value in values_list:
                    i = values_list.index(value)
                    for letter in value:
                        if letter == ' ':
                            values_list[i] = value[1:]

                spec = dict(zip(keys_list, values_list))

                return spec

    def get_price_info(self, item):
        price_current = item['price_current']
        price_original = item['price_original']

        price_current = float(price_current.replace(' ', '').replace('\xa0', '').replace('\n', '').replace('₽', ''))

        if price_original is not None:
            price_original = float(price_original.replace(' ', '').replace('\xa0', '').replace('\n', '').replace('₽', ''))
            discount = int((price_original - price_current) / price_original * 100)
        else:
            price_original = price_current
            discount = 0

        return [price_current, price_original, discount]

    def get_in_stock_info(self, item):
        in_stock = item['in_stock']
        if in_stock == 'Добавить в корзину':
            in_stock = True
        else:
            in_stock = False
        return in_stock

    def __del__(self):
        self.f.close()
        pass
