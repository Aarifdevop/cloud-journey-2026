from http.server import HTTPServer, BaseHTTPRequestHandler

LOG_FILE = "/app/logs/status.log"

class StatusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = ["No data yet."]

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = "<h1>Website Monitor Status</h1><pre>"
        html += "".join(lines[-20:])
        html += "</pre>"

        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        pass

server = HTTPServer(("0.0.0.0", 80), StatusHandler)
print("Server running on port 80")
server.serve_forever()
