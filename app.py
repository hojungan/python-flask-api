from flask import Flask, send_file, send_from_directory
from markupsafe import escape
from webcrawler.crawler import Crawler
import os

app = Flask(__name__)

@app.route("/<search>")
async def hello_world(search):
    _FILE_DOWNLOAD_NAME = f"{search.replace(' ', '_')}"
    c = await Crawler(search.replace(' ', '+')).crawl()
    file_loc = c.get_file_loc(_FILE_DOWNLOAD_NAME)
    return send_from_directory(file_loc[0], file_loc[1], as_attachment=True)

    # return send_file("file/path", as_attachment=True, download_name="downloadname.file")
    # return {"Page": "test", "URL": "test.com", "Products": [{"Name": "Prod 1", "Price": 299.99}, {"Name": "Prod 2", "Price": 29.99}, {"Name": "Prod 3", "Price": 99.99}, {"Name": "Prod 4", "Price": 199.99}, {"Name": "Prod 5", "Price": 259.99},]}