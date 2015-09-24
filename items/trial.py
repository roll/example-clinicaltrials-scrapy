import scrapy


class Trial(scrapy.Item):

    # Public

    nct_id = scrapy.Field()
    url = scrapy.Field()
