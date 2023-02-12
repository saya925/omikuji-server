import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/path1":
           body = "This is /path1".encode()
           status_code = 200
        elif self.path == "/path2":
           body = "This is /path2".encode()
           status_code = 200
        else:
           body = "ページが見つかりません！".encode()
           status_code = 404

        self.send_response(status_code)
        self.send_header("Content-type", "text/html; charset=UTF-8;")
        self.end_headers()
        self.wfile.write(body)

httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()