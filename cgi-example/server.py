from http.server import HTTPServer, CGIHTTPRequestHandler

print("Server has been started")
httpd = HTTPServer(("localhost", 8000), CGIHTTPRequestHandler)
httpd.serve_forever()
