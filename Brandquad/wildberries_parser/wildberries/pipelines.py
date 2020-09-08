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
        self.f.write('[')

    def add_to_json(self, product):
        self.f.write(json.dumps(product, indent=2, ensure_ascii=False))
        self.f.write(',')
        pass

    def process_item(self, item, spider):
        product = {
            'timestamp': item['timestamp'],
            'RPC': self.get_RPC(item),
            'url': item['url'],
            'title': self.space_wings_fix_str(item['title']),
            'color': item['color'],
            'brand': item['brand'],
            'section': item['section'],
            'price_data': self.get_price_data(item),
            'in_stock': self.get_in_stock_info(item),
            'count': item['count'],
            'assets': self.get_assets(item),
            'description': item['description'],
            'article': item['article'],
            'composition': item['composition'],
            'spec': self.get_spec(item),
            'city': item['city']
        }

        # print(product['spec'])

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
                keys_list = self.space_wings_fix_list(keys_list)
                values_list = self.space_wings_fix_list(values_list)

                spec = dict(zip(keys_list, values_list))

                return spec

    def get_price_data(self, item):
        price_current = item['price_current']
        price_original = item['price_original']

        price_current = float(price_current.replace(' ', '').replace('\xa0', '').replace('\n', '').replace('₽', ''))

        if price_original is not None:
            price_original = float(price_original.replace(' ', '').replace('\xa0', '').replace('\n', '').replace('₽', ''))
        else:
            price_original = price_current

        discount = int((price_original - price_current) / price_original * 100)

        if discount != 0:
            return {'current': price_current, 'original': price_original, 'sale_tag': f'Скидка {discount} %'}
        else:
            return {'current': price_current, 'original': price_original, 'sale_tag': 'Скидки нет'}

    def get_in_stock_info(self, item):
        in_stock = item['in_stock']
        if in_stock == 'Добавить в корзину':
            in_stock = True
        else:
            in_stock = False
        return in_stock

    def space_wings_fix_str(self, items_str):
        if type(items_str) == str:
            while len(items_str) > 0:
                if items_str[0] == ' ':
                    items_str = items_str[1:]
                else:
                    break
            while len(items_str) > 0:
                if items_str[-1] == ' ':
                    items_str = items_str[:-1]
                else:
                    break
        return items_str

    def space_wings_fix_list(self, items_list):
        if type(items_list) == list:
            for item in items_list:
                i = items_list.index(item)
                items_list[i] = self.space_wings_fix_str(items_list[i])
        return items_list

    def get_assets(self, item):
        set_images = item['set_images']

        # set_images = list(map(lambda x: x.replace('//', ''), set_images))
        set_images = list(map(lambda x: 'https:' + x, set_images))

        main_image = set_images.pop(0)

        return {'main_image': main_image, 'set_images': set_images}

    def get_RPC(self, item):
        RPC = item['tag_params']
        RPC = RPC.replace('\xa0', '').replace('\n', '').replace(';', '')
        RPC = RPC.split('=')[1]
        RPC = eval(RPC)
        RPC = str(RPC['ProdID'][0])
        return RPC

    def __del__(self):
        self.f.write(']')
        self.f.close()
        pass
