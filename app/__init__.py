from flask import Flask
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='9b0fb733452547c38680f08afc5b853b')

app = Flask(__name__)
from app import views