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
    
def get_headlines():
    '''
    Function that gets the json response 
    '''
    get_headline_url = headline_url.format(api_key)
    with urllib.request.urlopen(get_headline_url) as url:
        get_headline_data = url.read()
        get_headline_response = json.loads(get_headline_data)
        
        headline_results = None
        if get_headline_response['results']:
            headline_results_list =get_headline_response['results']
            headline_results = process_headline_results(headline_results_list)
            
    return headline_results

def process_headline_results(headline_list):
    '''
    Function  that processes the headline result and transform them to a list of Objects

    Args:
        headline_list: A list of dictionaries that contain headline details

    Returns :
        headline_results: headlines in the dict
    '''
    
    headline_results=[]
    for headline_item in headline_list:
        image = headline_item.get('url')
        title = headline_item.get ('title')
        author = headline_item.get('author')
        description = headline_item.get('description')
        time = headline_item.get('publishedAt')
        url = headline_item.get('urlToImage')
        
        if url:
            headline_object = Article(image,title,author,description,time,url)
            headline_results.append(headline_object)
            
    
    
def get_category(category):
    '''
    Function that gets the json response to our url request
    '''
    get_category_url = category_url.format(category,api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)
        
        category_results = None
        
        if get_category_response['results']:
            category_results_list =get_category_response['results']
            category_results = process_headline_results(category_results_list)
            
    return category_results

