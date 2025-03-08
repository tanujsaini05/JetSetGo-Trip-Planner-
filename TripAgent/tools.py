from crewai_tools import SerperDevTool,ScrapeWebsiteTool
from key import gooogle_api_key,serper_api_key
import os

os.environ["GOOGLE_API_KEY"] = gooogle_api_key
os.environ["SERPER_API_KEY"] = serper_api_key
scraper = ScrapeWebsiteTool()
serper = SerperDevTool()