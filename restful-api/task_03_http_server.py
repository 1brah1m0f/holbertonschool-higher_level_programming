#!/usr/bin/python3
"""mim"""


import json
from http.server import BaseHTTPRequestHandler, HTTPServer
"""base... ni import edirik"""

class MyHandler(BaseHTTPRequestHandler):
    """demeli burda Base... den miras aliriq"""
    def do_GET(self):
        if self.path == "/":
            """hec bir ideam yoxdu duzun desem"""
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            sample_data = {"name":"John","age":30,"city":"New York"}
            json_data= json.dumps(sample_data)

            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json_data.encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
             info_data = {"version": "1.0", "description": "A simple API built with http.server"}
             json_data = json.dumps(info_data)

             self.send_response(200)
             self.send_header("Content-type","application/json")
             self.end_headers()
             self.wfile.write(json_data.encode())

        else:
            self.send_response(404)
            self.send_header("Content-type","text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
PORT = 8000
server = HTTPServer(("localhost", PORT), APIBuilder)
print(f"Server running on http://localhost:{PORT}")
server.serve_forever()
