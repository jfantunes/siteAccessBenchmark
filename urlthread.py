class RequestThread(Thread):
    def __init__(self,url):
        super(RequestThread, self).__init__()
        self.url = url
        self.response = None
        self.elapsed_time=0
        self.speed=0

    def run(self):
        self.request = urllib.request.urlopen(self.url);
        start = time.time()
        self.response = len(self.request.read())
        end = time.time()
        self.elapsed_time=end
        self.speed=self.response/self.elapsed_time

def multi_get(uris,timeout=2.0):
    def alive_count(lst):
        alive = map(lambda x : 1 if x.isAlive() else 0, lst)
        a = 0
        for t in alive:
            a+=t
        return a
    threads = [ RequestThread(uri) for uri in uris ]
    for thread in threads:
        thread.start()
    while alive_count(threads) > 0 and timeout > 0.0:
        timeout = timeout - UPDATE_INTERVAL
        sleep(UPDATE_INTERVAL)
    results=[]
    for t in threads:
        results.append(t.url +" " + str(t.response)+ " "+str(t.elapsed_time))
    return results
