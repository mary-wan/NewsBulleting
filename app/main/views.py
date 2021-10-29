from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_headlines,get_category

@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    # sources= get_source()
    categories= get_category('sports')
    headlines = get_headlines()
    return render_template('index.html',categories=categories)