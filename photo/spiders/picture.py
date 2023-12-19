import json

import scrapy
from scrapy import Selector

from photo.items import PhotoItem


class PictureSpider(scrapy.Spider):
    name = "picture"
    allowed_domains = ["pixabay.com"]
    key = '风景'
    start_urls = [f"https://pixabay.com/zh/images/search/{key}/?min_width=1920&min_height=1080"]

    def parse(self, response, **kwargs):
        sel = Selector(response)
        pics = sel.css('#app > div:nth-child(1) > div > div.container--wYO8e > div.results--mB75j > div > div > div > '
                       'div')

        for pic in pics:
            item = PhotoItem()
            content = pic.css('script::text').get()
            jsonText = json.loads(content)
            item['src'] = jsonText.get('contentUrl')
            yield item
