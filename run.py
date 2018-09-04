import threading
import time
import SimpleHTTPServer
import SocketServer
import requests
from mako.template import Template
from mako import exceptions
import io

class RssRefreshThread(object):

    def __init__(self, url, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.url = url
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
        
    def run(self):
        while True:

            print "refreshing feed"
            
            response = requests.get(self.url)
            json = response.json()
            
            try:
                template = Template(filename='rss.mako')
                rss = template.render(blogs=json)
                
                with io.open('barstool.rss', 'w', encoding='utf-8') as file:
                    file.write(rss)
                    
            except:
                print(exceptions.text_error_template().render())
            
            time.sleep(self.interval)

refreshRss = RssRefreshThread('https://union.barstoolsports.com/v2/stories/category/97?limit=100&page=1', 900)

class Handler( SimpleHTTPServer.SimpleHTTPRequestHandler ):
    def do_GET( self ):
        self.send_response(200)
        self.send_header( 'Content-type', 'text/html' )
        self.end_headers()
        self.wfile.write( open('./barstool.rss').read() )

PORT = 8000
httpd = SocketServer.TCPServer( ('0.0.0.0', 8000), Handler )
print "serving at port", PORT
httpd.serve_forever()