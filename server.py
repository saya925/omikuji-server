import http.server
import socketserver
import random

kuji = ["☆彡大吉", "中吉", "小吉", "☠凶"]

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/omikuji":
           omikuji = random.choice(kuji)
           body = omikuji.encode()
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