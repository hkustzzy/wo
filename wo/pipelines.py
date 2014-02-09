# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class WoPipeline(object):

    def __init__(self):
        self.file = open('item.txt', 'wb')

    def process_item(self, item, spider):
        print item['category']
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line)
        #return item
        self.file.write(str(item['level']) + "\t" + item['ranking'] + '\t' + item['name'] + '\t' +
                        "".join(item['fullname'].split()).strip() + "\t"
                        + item['url'] + '\t' + item['category'] + '\n')
        #item['category'].decode['ascii'].encode['utf8']