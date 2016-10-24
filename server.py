#!/usr/bin/python
# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 3000
SERVER = "127.0.0.1"

# This class will handle any incoming request from
# a browser 
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_POST(self):
        print('Post request received')
        length = int(self.headers["Content-Length"])
        post_body = self.rfile.read(length).decode("utf-8")
        print(post_body)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        #self.wfile.write("Hello World !")
        return

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer((SERVER, PORT_NUMBER), myHandler)
    print ('Started httpserver on port ' , PORT_NUMBER)

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()
