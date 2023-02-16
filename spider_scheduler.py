from scraper.scraper.spiders.forecast_spider import ForecastSpider

from twisted.internet.task import LoopingCall
from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

configure_logging()
runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ForecastSpider))
task.start(60)
reactor.run()
