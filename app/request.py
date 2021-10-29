from app import app
import urllib.request,json
from .models import Article,Source

api_key = None
category_url = None
source_url = None
headline_url = None

def configure_request(app):
    global api_key, source_url, category_url,headline_url
    api_key = app.config['NEWS_API_KEY']
    category_url=app.config['CATEGORY_URL']
    source_url= app.config['SOURCE_URL']
    headline_url= app.config['HEADLINE_URL']
    
