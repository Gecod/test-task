from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from wildberries import settings
from wildberries.spiders.wbru import WbruSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(WbruSpider)

    process.start()
