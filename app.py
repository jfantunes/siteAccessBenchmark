# -*- coding: utf-8 -*-

import os
from requestthread import multipleRequest
from url_reader import get_urls
from bottle import route, run, template

@route('/benchmarking')
def index():
    try:
        urls=get_urls('urls.txt')
        requests,not_valid_requests = multipleRequest(urls,3.0)
        return template('list', valid=requests,not_valid=not_valid_requests)
    except Exception as e:
        return template("Error doing the benchmark, caused by {{exception}}",exception=str(e))
        
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)