from flask import Flask
from markupsafe import escape
from webcrawler.crawler import Crawler

app = Flask(__name__)

@app.route("/<search>")
async def hello_world(search):
    search_key_word = escape(search)
    crawler = Crawler(search_key_word.replace(' ', '+'))
    await crawler.crawl()
    return {search_key_word: crawler.products}
    