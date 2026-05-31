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

        html = "<html><head>"
        html += '<meta http-equiv="refresh" content="30">'
        html += "</head><body>"
        html += "<h1>Website Monitor Status</h1>"

        for line in lines[-20:]:
            if "STATUS=UP" in line:
                html += f'<div style="color:green;">{line}</div>'
            elif "STATUS=DOWN" in line:
                html += f'<div style="color:red;">{line}</div>'

        html += "</body></html>"
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        pass

server = HTTPServer(("0.0.0.0", 80), StatusHandler)
print("Server running on port 80")
server.serve_forever()
