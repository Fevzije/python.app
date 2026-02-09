from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 3000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World from Python + Docker \xf0\x9f\x90\x8d")

server = HTTPServer(("0.0.0.0", PORT), Handler)

print(f"Server running on http://localhost:{PORT}")
server.serve_forever()