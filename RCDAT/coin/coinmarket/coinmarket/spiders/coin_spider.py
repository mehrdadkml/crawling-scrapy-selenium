import scrapy

class CoinSpider(scrapy.Spider):
    name="coin"


    def start_requests(self):

        url="https://coinmarketcap.com/all/views/all/"
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response, **kwargs):
        for row in response.css("tbody tr"):
            yield{
                "name":row.css("a.cmc-table__column-name--name::text").extract_first(),
                "Abbreviation":row.css("a.cmc-link::text").extract_first()




            }