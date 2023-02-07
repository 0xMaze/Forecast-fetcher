from core.celery_app import celery_app
from scraper.scraper.spiders.forecast_spider import ForecastSpider


@celery_app.task
def scrape_cities():
    pass
