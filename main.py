from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

spider_name = "quotes"

process = CrawlerProcess(get_project_settings())
process.crawl(spider_name, domain="scrapy.org")
process.start()
