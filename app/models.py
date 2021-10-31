class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,url,description):
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        
class Article:
    '''
   Article class to define article objects
    '''
    def __init__(self,image,title,author,description,publishedAt,url):
        self.image = image
        self.title = title
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.url = url