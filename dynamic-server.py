
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl
import sys
from urllib.parse import urlparse
from urllib.parse import parse_qs

#This class will handles any incoming request from the browser
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
        #Handler for the GET requests
        def do_GET(self):
            # Sending an '200 OK' response
            self.send_response(200)

            # Setting the header
            self.send_header("Content-type", "text/html")

            # Whenever you use 'send_header', you also have to call 'end_headers'
            self.end_headers()

            # Extract url query parameters
            name = 'World'
            query_components = parse_qs(urlparse(self.path).query)
            if 'name' in query_components:
                name = query_components["name"][0]

            # Some custom HTML code, possibly generated by another function
            html = f"<html><head></head><body><h1>Hello {name}!</h1></body></html>"

            # Writing the HTML contents with UTF-8
            self.wfile.write(bytes(html, "utf8"))

            return

                


try:
        separator = "-" * 80
        server_address = ('', 4443)
        # server_address = ('localhost', 4443)
        httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
        # httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket,
                            server_side=True,
                            certfile="certs/cert.pem",
                            keyfile="certs/key.pem",
                            ssl_version=ssl.PROTOCOL_TLS)        
        print(separator)
        print("Server running on https://localhost:4443")
        print(separator)

        # Wait forever for incoming htto requests
        httpd.serve_forever()

except KeyboardInterrupt:
        print ('^C received, shutting down the web server')
        server.socket.close()