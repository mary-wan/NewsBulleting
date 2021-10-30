from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_headlines,get_category,get_source,get_source_aricles

@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    sources= get_source()
    categories= get_category('business')
    headlines = get_headlines()
    return render_template('index.html',categories=categories,headlines=headlines,sources=sources)

@main.route('/categories/<category>')
def category(category):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(category)
    sources= get_source()

    return render_template('categories.html',category = category,sources=sources)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = get_source_aricles(id)
    sources= get_source()
    category = get_category('health')
    return render_template('article.html',articles= articles,id=id,sources=sources,category=category)   



