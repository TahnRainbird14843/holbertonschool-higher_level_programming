"""
this is documented
"""

from http.server import *
import json


class Server(BaseHTTPRequestHandler):
    """this class handles server requests"""
    def display_content(self):
        """displayed when base site is accessed"""
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello, this is a simple API!'.encode())

    def display_data(self):
        """displayed when /data is accessed"""
        self.send_response(200)
        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def display_status(self):
        """displayed when /status is accessed"""
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        """runs the get request"""
        endpoint = self.path
        endpoint_paths  = {
            '/': self.display_content,
            '/data': self.display_data,
            '/status': self.display_status
        }
        try:
            endpoint_paths[endpoint]()
        except:
            self.send_response(404)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Endpoint Not Found'.encode())




port = HTTPServer(('', 8000), Server)
port.serve_forever()