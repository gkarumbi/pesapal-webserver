import http.server
import socketserver

PORT_IN_USE = 9000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT_IN_USE),handler) as httpd:
    print("Server started at localhost:" +str(PORT_IN_USE))
    httpd.serve_forever()