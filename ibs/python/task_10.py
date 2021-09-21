import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search(unittest.TestCase):

    def setUp(self) -> None:
        # step #1
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get('http://google.com/ncr')

    def test_search(self):
        assert 'Google' in self.drv.title

        # step #2
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)

        assert 'No results found' not in self.drv.page_source

        # step #3
        link_01 = self.drv.find_element_by_xpath('//div[@class="g"]//div[@class="g"]//a[@href]')
        assert 'selenide.org' in link_01.text

        # step #4
        link_images = self.drv.find_element_by_xpath('//div/a[text()="Images" or text()="Картинки"]')
        link_images.click()

        # step #5
        link_image_01 = self.drv.find_elements_by_xpath('//div[@data-ri=0]/a[@href]')
        check_image_01 = False
        for i in link_image_01:
            if 'selenide.org' in i.text:
                check_image_01 = True
                break
        assert check_image_01

        # step #6
        link_all = self.drv.find_element_by_xpath('//div/a[text()="Все"]')
        link_all.click()

        # step #7
        link_01 = self.drv.find_element_by_xpath('//div[@class="g"]//div[@class="g"]//a[@href]')
        assert 'selenide.org' in link_01.text

    def tearDown(self) -> None:
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
