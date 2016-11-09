# -*- coding: utf-8 -*-

from time import sleep
from timeit import default_timer as timer
from operator import itemgetter
import urllib.request
from threading import Thread, enumerate

INTERVAL = 0.01

class RequestThread(Thread):
    def __init__(self,url):
        super(RequestThread, self).__init__()
        self.url = url
        self.size = None
        self.elapsed_time=0
        self.speed=None
        self.error=None
        
    def todictionary(self):
        return {'url':self.url,'size':self.size,'load_time':self.elapsed_time,'speed':self.speed,'error':self.error}
        
    def run(self):
        try:
            self.request = urllib.request.urlopen(self.url);
            start = timer()
            self.size = len(self.request.read())
            end = timer()
            self.elapsed_time=end-start
            self.speed=self.size/self.elapsed_time
        except Exception as e:
            self.elapsed_time=None
            self.speed=None
            self.error=str(e)      
        
def multipleRequest(urls,timeout):
    threads = [ RequestThread(url) for url in urls ]
    for thread in threads:
        thread.start()
    while alive_threads(threads) > 0 and timeout > 0.0:
        timeout = timeout - INTERVAL
        sleep(INTERVAL)
    return present_results_ordered(threads,'speed')
    
def alive_threads(threads):
    alive = map(lambda x : 1 if x.isAlive() else 0, threads)
    return max(alive)
    
def present_results_ordered(threads,order_parameter):
    valid_results=[]
    unvalid_results=[]
    for t in threads:
        if(t.speed is not None):
            valid_results.append(t.todictionary())
        else:
            unvalid_results.append(t.todictionary())
    ordered_results=sorted(valid_results, key=itemgetter(order_parameter),reverse=True)
    return ordered_results,unvalid_results
