from dotenv import dotenv_values
from requests_project.scraper import call_scraper

config = dotenv_values(".env")


call_scraper(config)
