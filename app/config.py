from app.instance.config import NEWS_API_KEY


class Config:
    '''
    Configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2021-08-06&sortBy={}&apiKey={}'

class ProdConfig(Config):
    '''
    production configuration class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class
    '''
    DEBUG = True
    