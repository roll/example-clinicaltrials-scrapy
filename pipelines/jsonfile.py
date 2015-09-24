import json
import codecs


class Jsonfile(object):

    # Public

    def open_spider(self, spider):
        filename = 'data/%s.json' % spider.name
        self.file = codecs.open(filename, 'w', encoding='utf-8')
        self.sep = '[\n'

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = self.sep + json.dumps(dict(item), ensure_ascii=False, indent=4) + '\n'
        self.file.write(line)
        self.sep = ',\n'
        return item
