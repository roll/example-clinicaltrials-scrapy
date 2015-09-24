from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from items import Trial


class Trials(CrawlSpider):

    # Public

    name = 'trials'
    allowed_domains = ['clinicaltrials.gov']
    start_url_base = 'https://www.clinicaltrials.gov/ct2/results'
    start_urls = [
        start_url_base + r'?lup_s=07%2F01%2F2005&lup_e=08%2F01%2F2005',
    ]
    rules = [
        Rule(LinkExtractor(
            allow=r'ct2/results?lup_s=.*&lup_e=.*(pg=\d+)?',
        )),
        Rule(LinkExtractor(
            allow=r'ct2/show/NCT\d+',
            process_value=lambda value: value+'&resultsxml=true',
        ), callback='parse_item'),
    ]

    def parse_item(self, response):
        item = Trial()
        return item
