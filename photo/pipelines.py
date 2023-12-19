# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import random
import requests
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PhotoPipeline:
    def __init__(self):
        self.path = os.path.abspath('.')

    def process_item(self, item, spider):
        self.save_image(item['src'])
        return item

    def save_image(self, url):
        file_name = f"{int(random.random()*10000)}.jpg"
        res = requests.get(url)
        if 200 == res.status_code:
            with open(fr"{self.path}\img\{file_name}", "wb") as file:
                file.write(res.content)
