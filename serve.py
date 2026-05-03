import os, http.server, socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', 3000), Handler) as httpd:
    print('Serving on http://localhost:3000')
    httpd.serve_forever()
